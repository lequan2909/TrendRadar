#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simple test to see which sources are working (have items) vs broken"""

import requests
import time

BASE_URL = "http://localhost:5173/api"

# All 91 sources
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

def test_source_quick(source_id):
    """Quick test - just check if has items"""
    try:
        response = requests.get(
            f"{BASE_URL}/s?id={source_id}&latest",
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            status = data.get('status', 'unknown')
            
            if 'error' in data:
                return 'ERROR', 0
            
            return 'OK' if len(items) > 0 else 'EMPTY', len(items)
        else:
            return f'HTTP_{response.status_code}', 0
    except:
        return 'FAIL', 0

print("="*70)
print("TEST NGUỒN TIN NEWSNOW - Kiểm tra nhanh")
print("="*70)
print(f"Đang test {len(ALL_SOURCES)} nguồn...\n")

working = []
empty = []
broken = []

for i, source_id in enumerate(ALL_SOURCES, 1):
    status, count = test_source_quick(source_id)
    
    if status == 'OK':
        working.append((source_id, count))
        print(f"✅ {i:2}. {source_id:25} - {count:3} tin")
    elif status == 'EMPTY':
        empty.append(source_id)
        print(f"⚠️  {i:2}. {source_id:25} - 0 tin")
    else:
        broken.append((source_id, status))
        print(f"❌ {i:2}. {source_id:25} - LỖI ({status})")
    
    time.sleep(0.3)  # Delay nhỏ giữa các request

print("\n" + "="*70)
print("KẾT QUẢ TỔNG HỢP")
print("="*70)

print(f"\n✅ CÓ TIN ({len(working)} nguồn):")
for source, count in sorted(working, key=lambda x: -x[1])[:20]:
    print(f"   {source:25} - {count:3} tin")
if len(working) > 20:
    print(f"   ... và {len(working)-20} nguồn khác")

if empty:
    print(f"\n⚠️  KHÔNG CÓ TIN ({len(empty)} nguồn):")
    for source in empty[:15]:
        print(f"   {source}")
    if len(empty) > 15:
        print(f"   ... và {len(empty)-15} nguồn khác")

if broken:
    print(f"\n❌ LỖI/KHÔNG KẾT NỐI ({len(broken)} nguồn):")
    for source, status in broken[:15]:
        print(f"   {source:25} - {status}")
    if len(broken) > 15:
        print(f"   ... và {len(broken)-15} nguồn khác")

print("\n" + "="*70)
print(f"Tổng cộng:        {len(ALL_SOURCES)} nguồn")
print(f"✅ Có tin:        {len(working)} ({len(working)/len(ALL_SOURCES)*100:.1f}%)")
print(f"⚠️  Không có tin:  {len(empty)} ({len(empty)/len(ALL_SOURCES)*100:.1f}%)")
print(f"❌ Lỗi:           {len(broken)} ({len(broken)/len(ALL_SOURCES)*100:.1f}%)")
print("="*70)

# Vietnamese sources summary
vn_sources = [s for s in ALL_SOURCES if 'vn' in s.lower() or 'viet' in s.lower()]
vn_working = [s for s, c in working if 'vn' in s.lower() or 'viet' in s.lower()]
vn_empty = [s for s in empty if 'vn' in s.lower() or 'viet' in s.lower()]
vn_broken = [(s, st) for s, st in broken if 'vn' in s.lower() or 'viet' in s.lower()]

print(f"\n📍 NGUỒN TIN VIỆT NAM:")
print(f"   Tổng:          {len(vn_sources)} nguồn")
print(f"   ✅ Có tin:      {len(vn_working)} nguồn")
print(f"   ⚠️  Không tin:   {len(vn_empty)} nguồn")
print(f"   ❌ Lỗi:         {len(vn_broken)} nguồn")

if vn_working:
    print(f"\n   Nguồn VN hoạt động: {', '.join(vn_working)}")
if vn_empty:
    print(f"   Nguồn VN không tin: {', '.join(vn_empty)}")
if vn_broken:
    print(f"   Nguồn VN lỗi: {', '.join([s for s, st in vn_broken])}")

print("="*70)
