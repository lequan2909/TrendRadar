#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test fixed NewsNow sources on local dev server"""

import requests
import json
import time

# Local NewsNow API
BASE_URL = "http://localhost:5173/api"

# Sources to test
SOURCES = [
    ("zingnews", "Zing News"),
    ("cafef", "CafeF Tài chính"),
    ("genk", "Genk Tech"),
    ("dantri", "Dân Trí"),
    ("vietnamfinance", "Vietnam Finance"),
    ("vnreview", "VNReview Tech")
]

def test_source(source_id, source_name):
    """Test a single source"""
    url = f"{BASE_URL}/s?id={source_id}&latest"
    
    print(f"\n{'='*60}")
    print(f"Testing: {source_name} ({source_id})")
    print(f"URL: {url}")
    print(f"{'='*60}")
    
    try:
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            
            status = data.get('status', 'unknown')
            items = data.get('items', [])
            updated_time = data.get('updatedTime', 0)
            
            print(f"✓ Status: {status}")
            print(f"✓ Items count: {len(items)}")
            
            if items:
                # Show first item
                first = items[0]
                print(f"\nFirst item:")
                print(f"  Title: {first.get('title', 'N/A')[:80]}...")
                print(f"  URL: {first.get('url', 'N/A')[:80]}...")
                print(f"  PubDate: {first.get('pubDate', 'N/A')}")
                
                return True, len(items)
            else:
                print(f"✗ No items returned")
                return False, 0
        else:
            print(f"✗ HTTP Error: {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return False, 0
            
    except requests.exceptions.ConnectionError:
        print(f"✗ Connection Error: Server not running?")
        return False, 0
    except requests.exceptions.Timeout:
        print(f"✗ Timeout after 30s")
        return False, 0
    except Exception as e:
        print(f"✗ Error: {e}")
        return False, 0

def main():
    print("="*60)
    print("NewsNow Local Test - Fixed Sources")
    print("="*60)
    print(f"Base URL: {BASE_URL}")
    print(f"Sources to test: {len(SOURCES)}")
    
    # Wait for server to start
    print("\nWaiting 8 seconds for dev server to start...")
    time.sleep(8)
    
    results = {}
    
    for source_id, source_name in SOURCES:
        success, count = test_source(source_id, source_name)
        results[source_id] = (success, count)
        time.sleep(2)  # Wait between requests
    
    # Summary
    print(f"\n\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    
    working = []
    broken = []
    
    for source_id, source_name in SOURCES:
        success, count = results[source_id]
        status = "✓" if success else "✗"
        
        print(f"{status} {source_name:20} - {count} items")
        
        if success:
            working.append(source_id)
        else:
            broken.append(source_id)
    
    print(f"\n{'='*60}")
    print(f"Working: {len(working)}/{len(SOURCES)}")
    print(f"Broken: {len(broken)}/{len(SOURCES)}")
    
    if broken:
        print(f"\nBroken sources:")
        for sid in broken:
            print(f"  - {sid}")
    
    print(f"{'='*60}")
    
    return len(working) == len(SOURCES)

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
