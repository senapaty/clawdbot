#!/usr/bin/env python3
"""
Rocco's ListMonk Client - Newsletter management for WOW Club
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

def api_get(endpoint, params=None):
    """Make GET request to ListMonk API"""
    url = f"{BASE_URL}/api{endpoint}"
    if params:
        query = "&".join([f"{k}={v}" for k, v in params.items()])
        url = f"{url}?{query}"
    req = urllib.request.Request(url, headers={"Authorization": AUTH_HEADER})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

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
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

def list_campaigns(limit=5):
    """List recent campaigns"""
    return api_get("/campaigns", {"per_page": limit})

def get_campaign(campaign_id):
    """Get single campaign details"""
    return api_get(f"/campaigns/{campaign_id}")

def create_campaign(name, subject, body, list_ids, from_email="Sumitra Senapaty <me@wowclub.in>"):
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
        "tags": ["newsletter"],
        "template_id": 1
    }
    return api_post("/campaigns", data)

def list_lists():
    """List all subscriber lists"""
    return api_get("/lists", {"per_page": 20})

if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "campaigns"
    
    if command == "campaigns":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        result = list_campaigns(limit)
        # Pretty print just the essentials
        if "data" in result and "results" in result["data"]:
            for c in result["data"]["results"]:
                print(f"ID: {c['id']} | {c['subject']} | Status: {c['status']} | Sent: {c.get('sent', 0)}")
        else:
            print(json.dumps(result, indent=2))
    
    elif command == "lists":
        result = list_lists()
        if "data" in result and "results" in result["data"]:
            for l in result["data"]["results"]:
                print(f"ID: {l['id']} | {l['name']} | Subscribers: {l.get('subscriber_count', 0)}")
        else:
            print(json.dumps(result, indent=2))
    
    elif command == "get":
        cid = sys.argv[2] if len(sys.argv) > 2 else "11"
        result = get_campaign(cid)
        print(json.dumps(result, indent=2))
    
    else:
        print("Usage: listmonk.py [campaigns|lists|get <id>]")
