#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""Quick test RSS URLs directly"""
import requests

urls = {
    "zingnews": "https://zingnews.vn/rss",
    "cafef": "https://m.cafef.vn/sitemaps/category.rss",
    "genk": "https://genk.vn/rss/home.rss",
    "dantri": "https://dantri.com.vn/thoi-su.rss",
    "vietnamfinance": "https://vietnamfinance.vn/rss",
    "vnreview": "http://vnreview.vn/feed/-/rss/home"
}

for name, url in urls.items():
    try:
        r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        print(f"{name:20} {r.status_code:3} - {url}")
        if r.status_code != 200:
            print(f"  └─ Error: {r.text[:100]}")
    except Exception as e:
        print(f"{name:20} ERR - {str(e)[:60]}")
