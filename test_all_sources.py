#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive test for ALL NewsNow sources"""

import requests
import json
import time
from collections import defaultdict

# Local NewsNow API
BASE_URL = "http://localhost:5173/api"

# ALL 90 SOURCES (extracted from sources directory)
ALL_SOURCES = [
    "24h", "_36kr", "aljazeera", "anonyviet", "apnews", "arstechnica",
    "baidu", "bangkokpost", "baomoi", "bbcnews", "bbcvietnamese", "bilibili",
    "bloomberg", "cafef", "cankaoxiaoxi", "chongbuluo", "cna", "cnet",
    "cnn", "coolapk", "dantri", "douyin", "engadget", "fastbull",
    "gelonghui", "genk", "ghxi", "github", "hackernews", "hupu",
    "ictnews", "ifeng", "ithome", "jin10", "juejin", "kaopu",
    "kenh14", "kuaishou", "laodong", "lemmy", "linuxdo", "lobsters",
    "luatkhoa", "mktnews", "nld", "nowcoder", "pcbeta", "plo",
    "producthunt", "reddit-geopolitics", "reddit-programming", "reddit-science",
    "reddit-technology", "reddit-worldnews", "redditvietnam", "reuters", "rfa",
    "rfi", "smzdm", "soha", "solidot", "sputniknewscn", "sspai",
    "stackoverflow", "techcrunch", "thanhnien", "theguardian", "thepaper",
    "thestar", "thevietnamese", "theverge", "tieba", "tinhte",
    "toutiao", "tuoitre", "v2ex", "vietnamfinance", "vietnamnet",
    "vietnamnews", "vietstock", "vna", "vnexpress", "vnreview",
    "voa", "wallstreetcn", "weibo", "wired", "xueqiu",
    "zaobao", "zhihu", "zingnews"
]

def test_source(source_id):
    """Test a single source - quick version"""
    url = f"{BASE_URL}/s?id={source_id}&latest"
    
    try:
        response = requests.get(url, timeout=15)
        
        if response.status_code == 200:
            try:
                data = response.json()
                status = data.get('status', 'unknown')
                items = data.get('items', [])
                
                if 'error' in data:
                    return 'ERROR', 0, str(data.get('error', ''))[:50]
                
                return status, len(items), None
            except json.JSONDecodeError:
                return 'JSON_ERROR', 0, 'Invalid JSON'
        else:
            return f'HTTP_{response.status_code}', 0, None
            
    except requests.exceptions.Timeout:
        return 'TIMEOUT', 0, None
    except requests.exceptions.ConnectionError:
        return 'CONNECTION', 0, None
    except Exception as e:
        return 'EXCEPTION', 0, str(e)[:50]

def main():
    print("="*80)
    print("COMPREHENSIVE NewsNow Source Test")
    print("="*80)
    print(f"Base URL: {BASE_URL}")
    print(f"Total sources: {len(ALL_SOURCES)}")
    print("="*80)
    
    print("\nTesting all sources (this will take a while)...\n")
    
    results = {}
    stats = defaultdict(int)
    
    for i, source_id in enumerate(ALL_SOURCES, 1):
        status, count, error = test_source(source_id)
        results[source_id] = (status, count, error)
        
        # Progress indicator
        if i % 10 == 0:
            print(f"Progress: {i}/{len(ALL_SOURCES)} tested...")
        
        # Small delay to not overwhelm server
        time.sleep(0.5)
    
    # Print results
    print(f"\n{'='*80}")
    print("RESULTS")
    print(f"{'='*80}\n")
    
    # Group by status
    working = []
    broken = []
    zero_items = []
    errors = []
    
    for source_id in ALL_SOURCES:
        status, count, error = results[source_id]
        
        if status in ['success', 'cache']:
            if count > 0:
                working.append((source_id, count))
            else:
                zero_items.append(source_id)
        else:
            broken.append((source_id, status, error))
    
    # Print working sources
    print(f"✅ WORKING ({len(working)}):")
    for source_id, count in sorted(working, key=lambda x: -x[1]):
        print(f"   {source_id:25} - {count:3} items")
    
    # Print zero items
    if zero_items:
        print(f"\n⚠️  ZERO ITEMS ({len(zero_items)}):")
        for source_id in zero_items:
            print(f"   {source_id}")
    
    # Print broken sources
    if broken:
        print(f"\n❌ BROKEN ({len(broken)}):")
        for source_id, status, error in broken:
            error_msg = f" - {error}" if error else ""
            print(f"   {source_id:25} - {status}{error_msg}")
    
    # Summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"Working (with items):  {len(working):3} / {len(ALL_SOURCES)}")
    print(f"Zero items:            {len(zero_items):3} / {len(ALL_SOURCES)}")
    print(f"Broken/Error:          {len(broken):3} / {len(ALL_SOURCES)}")
    print(f"Success rate:          {len(working)/len(ALL_SOURCES)*100:.1f}%")
    print(f"{'='*80}\n")
    
    # Vietnamese sources specific
    vietnamese_sources = [s for s in ALL_SOURCES if any(vn in s for vn in ['vn', 'vietnam', 'viet', 'vietnam'])]
    vietnamese_working = [s for s, c in working if any(vn in s for vn in ['vn', 'vietnam', 'viet'])]
    
    print(f"Vietnamese sources: {len(vietnamese_sources)}")
    print(f"Vietnamese working: {len(vietnamese_working)}")
    print(f"Vietnamese sources: {', '.join(vietnamese_sources)}")
    
    return len(working) > 50  # Success if > 50 sources work

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
