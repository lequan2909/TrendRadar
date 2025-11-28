#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test RSS feeds for broken Vietnamese news sources"""

import requests
from xml.etree import ElementTree as ET

# RSS feeds to test
RSS_FEEDS = {
    "zingnews": "https://znews.vn/rss",
    "cafef": "https://cafef.vn/trang-chu.rss",
    "genk": "https://genk.vn/rss/tin-moi-nhat.rss",
    "dantri": "https://dansinh.dantri.com.vn/rss.htm",
    "vietnamfinance": "https://vietnamfinance.vn/rss",
    "vnreview": "https://vnreview.vn/rss"
}

def test_rss_feed(name, url):
    """Test a single RSS feed"""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"URL: {url}")
    print(f"{'='*60}")
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            # Try to parse XML
            try:
                root = ET.fromstring(response.content)
                
                # Find channel and items
                channel = root.find('.//channel')
                if channel is not None:
                    items = channel.findall('item')
                    print(f"✓ XML parsed successfully")
                    print(f"✓ Found {len(items)} items")
                    
                    if items:
                        # Show first item
                        first_item = items[0]
                        title = first_item.find('title')
                        link = first_item.find('link')
                        pubDate = first_item.find('pubDate')
                        
                        print(f"\nFirst item preview:")
                        print(f"  Title: {title.text if title is not None else 'N/A'}")
                        print(f"  Link: {link.text if link is not None else 'N/A'}")
                        print(f"  PubDate: {pubDate.text if pubDate is not None else 'N/A'}")
                        
                        return True, f"OK - {len(items)} items"
                    else:
                        return False, "No items found in RSS"
                else:
                    return False, "No channel element in RSS"
                    
            except ET.ParseError as e:
                print(f"✗ XML Parse Error: {e}")
                print(f"Response preview: {response.text[:200]}")
                return False, f"XML Parse Error: {str(e)}"
        else:
            print(f"✗ HTTP Error: {response.status_code}")
            return False, f"HTTP {response.status_code}"
            
    except requests.exceptions.Timeout:
        print(f"✗ Timeout after 15s")
        return False, "Timeout"
    except requests.exceptions.RequestException as e:
        print(f"✗ Request Error: {e}")
        return False, f"Request Error: {str(e)}"
    except Exception as e:
        print(f"✗ Unexpected Error: {e}")
        return False, f"Error: {str(e)}"

def main():
    print("="*60)
    print("RSS Feed Testing for Vietnamese News Sources")
    print("="*60)
    
    results = {}
    
    for name, url in RSS_FEEDS.items():
        success, message = test_rss_feed(name, url)
        results[name] = (success, message)
    
    # Summary
    print(f"\n\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    
    working = []
    broken = []
    
    for name, (success, message) in results.items():
        status = "✓" if success else "✗"
        print(f"{status} {name:20} - {message}")
        
        if success:
            working.append(name)
        else:
            broken.append(name)
    
    print(f"\n{'='*60}")
    print(f"Working: {len(working)}/{len(RSS_FEEDS)}")
    print(f"Broken: {len(broken)}/{len(RSS_FEEDS)}")
    
    if broken:
        print(f"\nBroken sources need fixing:")
        for name in broken:
            print(f"  - {name}: {results[name][1]}")
    
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
