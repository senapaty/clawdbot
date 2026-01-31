#!/usr/bin/env python3
"""
Update ListMonk Campaign #12 with new HTML content
"""
import os
import sys
import json
import urllib.request
import urllib.error

# Config
BASE_URL = os.getenv('LISTMONK_URL', 'https://monk.wowsumitra.com')
API_KEY = os.getenv('LISTMONK_API_KEY', '')
USERNAME = os.getenv('LISTMONK_USERNAME', 'clawdbot')
AUTH_HEADER = f"token {USERNAME}:{API_KEY}"

def api_put(endpoint, data=None):
    """Make PUT request to ListMonk API"""
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

def update_campaign(campaign_id, body_content):
    """Update campaign body"""
    data = {
        "body": body_content,
        "content_type": "richtext"
    }
    return api_put(f"/campaigns/{campaign_id}", data)

if __name__ == "__main__":
    # Read the HTML content from file
    content_file = sys.argv[1] if len(sys.argv) > 1 else "/home/pi/.openclaw/workspace/drafts/newsletter_2026_02_turkey.html"
    
    with open(content_file, 'r') as f:
        body_content = f.read()
    
    # Update campaign 12
    result = update_campaign(12, body_content)
    
    if "error" in result:
        print(f"❌ Error: {result['error']}")
        if "details" in result:
            print(f"Details: {result['details']}")
        sys.exit(1)
    else:
        print(f"✅ Campaign #12 updated successfully!")
        print(json.dumps(result, indent=2))
