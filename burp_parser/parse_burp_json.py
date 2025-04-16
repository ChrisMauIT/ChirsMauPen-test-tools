#!/usr/bin/env python3
"""
Extract high/critical issues from Burp JSON exports.
"""

import json

def extract_issues(file):
    with open(file, 'r') as f:
        data = json.load(f)
        for item in data.get("issues", []):
            if item['severity'] in ['High', 'Critical']:
                print(f"[{item['severity']}] {item['name']} at {item['host']}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python parse_burp_json.py <burp_output.json>")
    else:
        extract_issues(sys.argv[1])
