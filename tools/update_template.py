#!/usr/bin/env python3
"""
Update ListMonk Template #1 with logo - fixed version
"""
import os
import sys
import json
import urllib.request
import urllib.error

BASE_URL = os.getenv('LISTMONK_URL', 'https://monk.wowsumitra.com')
API_KEY = os.getenv('LISTMONK_API_KEY', '')
USERNAME = os.getenv('LISTMONK_USERNAME', 'clawdbot')
AUTH_HEADER = f"token {USERNAME}:{API_KEY}"

def api_put(endpoint, data=None):
    url = f"{BASE_URL}/api{endpoint}"
    headers = {
        "Authorization": AUTH_HEADER,
        "Content-Type": "application/json"
    }
    try:
        body = json.dumps(data).encode() if data else None
        req = urllib.request.Request(url, data=body, headers=headers, method="PUT")
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        return {"error": f"HTTP {e.code}: {e.reason}", "details": error_body}
    except Exception as e:
        return {"error": str(e)}

TEMPLATE_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ .Campaign.Subject }}</title>
    <style>
        body, table, td, p { margin: 0; padding: 0; }
        body {
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 16px;
            line-height: 1.7;
            color: #333333;
            background-color: #f8f8f8;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }
        .header {
            text-align: center;
            padding: 40px 30px 20px;
            border-bottom: 1px solid #eeeeee;
        }
        .header-logo img {
            display: block;
            margin: 0 auto;
        }
        .header-tagline {
            font-size: 12px;
            color: #888888;
            text-transform: uppercase;
            letter-spacing: 3px;
            margin-top: 8px;
        }
        .content {
            padding: 30px;
        }
        h1 {
            font-size: 24px;
            font-weight: normal;
            color: #2c3e50;
            margin: 30px 0 15px;
            line-height: 1.3;
        }
        h2 {
            font-size: 20px;
            font-weight: normal;
            color: #34495e;
            margin: 25px 0 12px;
            line-height: 1.3;
        }
        h3 {
            font-size: 17px;
            font-weight: bold;
            color: #2c3e50;
            margin: 20px 0 10px;
        }
        p {
            margin-bottom: 15px;
        }
        a {
            color: #2980b9;
            text-decoration: none;
            border-bottom: 1px solid #2980b9;
        }
        a:hover {
            color: #1a5276;
        }
        .trip-card {
            background-color: #fafafa;
            border-left: 3px solid #2980b9;
            padding: 20px;
            margin: 20px 0;
        }
        .trip-card h3 {
            margin-top: 0;
        }
        .urgency {
            background-color: #fff8e1;
            border-left: 3px solid #f39c12;
            padding: 15px 20px;
            margin: 20px 0;
            font-size: 15px;
        }
        .cta {
            text-align: center;
            margin: 25px 0;
        }
        .cta a {
            display: inline-block;
            background-color: #2c3e50;
            color: #ffffff;
            padding: 12px 30px;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
            border: none;
        }
        .cta a:hover {
            background-color: #34495e;
        }
        .footer {
            background-color: #2c3e50;
            color: #ffffff;
            padding: 30px;
            text-align: center;
            font-size: 13px;
        }
        .footer a {
            color: #ffffff;
            border-bottom: 1px solid rgba(255,255,255,0.3);
        }
        @media screen and (max-width: 600px) {
            .content {
                padding: 20px;
            }
            h1 {
                font-size: 22px;
            }
            h2 {
                font-size: 18px;
            }
            .trip-card {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <table class="container" width="100%" cellpadding="0" cellspacing="0">
        <tr>
            <td class="header">
                <div class="header-logo">
                    <img src="https://www.wowclub.com/images/main-logo.svg" alt="WOW Club" width="180">
                </div>
                <div class="header-tagline">Women On Wanderlust</div>
            </td>
        </tr>
        <tr>
            <td class="content">
                {{ template "content" . }}
            </td>
        </tr>
        <tr>
            <td class="footer">
                <p>With wanderlust,<br>Sumitra</p>
                <p style="margin-top: 20px;">
                    📧 me@wowclub.in<br>
                    🌐 www.wowclub.com<br>
                    📱 Join our WhatsApp Community
                </p>
                <p style="margin-top: 20px; font-size: 11px; opacity: 0.7;">
                    You're receiving this because you enquired about WOW Club trips.<br>
                    <a href="{{ UnsubscribeURL }}">Unsubscribe</a> | 
                    <a href="{{ MessageURL }}">View in browser</a>
                </p>
            </td>
        </tr>
    </table>
</body>
</html>'''

if __name__ == "__main__":
    data = {
        "name": "WOW Club Newsletter",
        "body": TEMPLATE_HTML,
        "type": "campaign"
    }
    result = api_put("/templates/1", data)
    
    if "error" in result:
        print(f"❌ Error: {result['error']}")
        if "details" in result:
            print(f"Details: {result['details']}")
        sys.exit(1)
    else:
        print(f"✅ Template #1 updated with complete HTML!")
