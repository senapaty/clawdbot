#!/usr/bin/env python3
"""
Rocco's Email Client - Simple Gmail IMAP/SMTP wrapper
"""
import os
import sys
import json
import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Config from env
EMAIL = os.getenv('ROCCO_EMAIL', 'rocco_bot@akashsenapaty.in')
PASSWORD = os.getenv('ROCCO_GMAIL_APP_PASSWORD', '')

def send_email(to, subject, body, html_body=None):
    """Send email via Gmail SMTP"""
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = EMAIL
        msg['To'] = to
        msg['Subject'] = subject
        
        # Plain text part
        msg.attach(MIMEText(body, 'plain'))
        
        # HTML part if provided
        if html_body:
            msg.attach(MIMEText(html_body, 'html'))
        
        # Send via Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()
        
        return {"success": True, "message": f"Email sent to {to}"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def check_email(limit=10):
    """Check inbox via Gmail IMAP"""
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(EMAIL, PASSWORD)
        mail.select('inbox')
        
        # Search for all emails
        _, search_data = mail.search(None, 'ALL')
        email_ids = search_data[0].split()
        
        # Get last N emails
        emails = []
        for eid in reversed(email_ids[-limit:]):
            _, data = mail.fetch(eid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            
            emails.append({
                "id": eid.decode(),
                "from": email_message['From'],
                "subject": email_message['Subject'],
                "date": email_message['Date'],
                "body": get_email_body(email_message)
            })
        
        mail.close()
        mail.logout()
        
        return {"success": True, "emails": emails, "count": len(emails)}
    except Exception as e:
        import traceback
        return {"success": False, "error": str(e), "traceback": traceback.format_exc()}

def get_email_body(email_message):
    """Extract body from email message"""
    body = ""
    if email_message.is_multipart():
        for part in email_message.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                try:
                    body = part.get_payload(decode=True).decode()
                    break
                except:
                    pass
    else:
        try:
            body = email_message.get_payload(decode=True).decode()
        except:
            pass
    return body[:500]  # Limit body length

if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "check"
    
    if command == "send":
        to = sys.argv[2] if len(sys.argv) > 2 else ""
        subject = sys.argv[3] if len(sys.argv) > 3 else "Test Email"
        body = sys.argv[4] if len(sys.argv) > 4 else "Hello from Rocco!"
        result = send_email(to, subject, body)
    elif command == "check":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        result = check_email(limit)
    else:
        result = {"error": "Unknown command. Use 'send' or 'check'"}
    
    print(json.dumps(result, indent=2))
