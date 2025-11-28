#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick test for specific RSS feeds"""

import requests

urls = [
    ("zingnews", "https://znews.vn/rss"),
    ("cafef", "https://cafef.vn/trang-chu.rss"),
    ("genk", "https://genk.vn/rss/tin-moi-nhat.rss"),
    ("dantri", "https://dansinh.dantri.com.vn/rss.htm"),
    ("vietnamfinance", "https://vietnamfinance.vn/rss/tai-chinh.rss"),
]

for name, url in urls:
    try:
        r = requests.head(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        print(f"{name:20} - Status: {r.status_code} - {url}")
    except Exception as e:
        print(f"{name:20} - Error: {str(e)[:50]}")
