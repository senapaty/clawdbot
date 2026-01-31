#!/usr/bin/env python3
"""
Create WOW Club newsletter draft in ListMonk
"""
import os
import sys
import json
import urllib.request
import urllib.error

BASE_URL = os.getenv('LISTMONK_URL', 'https://monk.wowsumitra.com')
API_KEY = os.getenv('LISTMONK_API_KEY', '')
AUTH_HEADER = f"token clawdbot:{API_KEY}"

def api_post(endpoint, data=None):
    """Make POST request to ListMonk API"""
    url = f"{BASE_URL}/api{endpoint}"
    headers = {
        "Authorization": AUTH_HEADER,
        "Content-Type": "application/json"
    }
    try:
        body = json.dumps(data).encode() if data else None
        req = urllib.request.Request(url, data=body, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}", "details": e.read().decode()}
    except Exception as e:
        return {"error": str(e)}

def create_campaign(name, subject, body, list_ids=[5], from_email="Sumitra Senapaty <me@wowclub.in>"):
    """Create a new campaign draft"""
    data = {
        "name": name,
        "subject": subject,
        "body": body,
        "content_type": "richtext",
        "messenger": "email",
        "type": "regular",
        "from_email": from_email,
        "lists": list_ids,
        "tags": ["newsletter", "featured-trip"],
        "template_id": 1
    }
    return api_post("/campaigns", data)

if __name__ == "__main__":
    # Read the HTML content
    html_file = "/home/pi/.openclaw/workspace/drafts/newsletter_2026_02_turkey.html"
    with open(html_file, 'r') as f:
        body = f.read()
    
    # Create campaign
    result = create_campaign(
        name="February 2026 - Turkey Calling",
        subject="That one trip that changes everything 🎈",
        body=body,
        list_ids=[5]  # Oct - last 6 months enquired
    )
    
    if "data" in result:
        print(f"✅ Campaign created!")
        print(f"   ID: {result['data'].get('id')}")
        print(f"   Name: {result['data'].get('name')}")
        print(f"   Subject: {result['data'].get('subject')}")
        print(f"   Status: {result['data'].get('status')}")
        print(f"\nView in ListMonk: https://monk.wowsumitra.com/admin/campaigns/{result['data'].get('id')}")
    else:
        print(f"❌ Error: {result.get('error', 'Unknown error')}")
        if 'details' in result:
            print(f"Details: {result['details']}")
