# 📰 Bước 2: Thêm Nguồn Tin Việt Nam

## 🎯 Mục Tiêu

Thêm 3 nguồn tin VN vào newsnow:
1. **VnExpress** - vnexpress.net
2. **Tuổi Trẻ** - tuoitre.vn
3. **Dân Trí** - dantri.com.vn

---

## 📚 Chuẩn Bị

### **Nghiên cứu RSS Feed**

| Nguồn | RSS URL | Loại |
|-------|---------|------|
| VnExpress | `https://vnexpress.net/rss/tin-moi-nhat.rss` | Tin mới nhất |
| Tuổi Trẻ | `https://tuoitre.vn/rss/tin-moi-nhat.rss` | Tin mới nhất |
| Dân Trí | `https://dantri.com.vn/rss.htm` | Tin tổng hợp |

---

## 1️⃣ Cài Thư Viện Parse RSS

```powershell
cd C:\Users\trung\TrendRadar\newsnow

# Cài fast-xml-parser
pnpm add fast-xml-parser
```

---

## 2️⃣ Tạo Nguồn VnExpress

### **Tạo file `server/sources/vnexpress.ts`**

```typescript
import type { NewsItem, SourceHandler } from "../types"
import { XMLParser } from "fast-xml-parser"

export const handler: SourceHandler = async () => {
  try {
    // 1. Fetch RSS feed
    const response = await fetch("https://vnexpress.net/rss/tin-moi-nhat.rss")
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const xmlText = await response.text()
    
    // 2. Parse XML
    const parser = new XMLParser({
      ignoreAttributes: false,
      attributeNamePrefix: "@_"
    })
    const result = parser.parse(xmlText)
    
    // 3. Extract items
    const rssItems = result.rss?.channel?.item || []
    if (!Array.isArray(rssItems)) {
      throw new Error("Invalid RSS format")
    }
    
    // 4. Transform thành NewsItem[]
    const items: NewsItem[] = rssItems.slice(0, 40).map((item: any, index: number) => {
      // Lấy description và extract image
      const description = item.description || ""
      const imageMatch = description.match(/src="([^"]+)"/)
      const imageUrl = imageMatch ? imageMatch[1] : undefined
      
      return {
        id: `vnexpress-${index}-${Date.now()}`,
        title: item.title || "Untitled",
        url: item.link || "",
        pubDate: item.pubDate ? new Date(item.pubDate).toISOString() : undefined,
        extra: {
          icon: imageUrl
        }
      }
    })
    
    return items
  } catch (error) {
    console.error("[VnExpress] Error:", error)
    throw error
  }
}
```

---

## 3️⃣ Tạo Nguồn Tuổi Trẻ

### **Tạo file `server/sources/tuoitre.ts`**

```typescript
import type { NewsItem, SourceHandler } from "../types"
import { XMLParser } from "fast-xml-parser"

export const handler: SourceHandler = async () => {
  try {
    const response = await fetch("https://tuoitre.vn/rss/tin-moi-nhat.rss")
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const xmlText = await response.text()
    
    const parser = new XMLParser({
      ignoreAttributes: false,
      attributeNamePrefix: "@_"
    })
    const result = parser.parse(xmlText)
    
    const rssItems = result.rss?.channel?.item || []
    if (!Array.isArray(rssItems)) {
      throw new Error("Invalid RSS format")
    }
    
    const items: NewsItem[] = rssItems.slice(0, 40).map((item: any, index: number) => {
      const description = item.description || ""
      const imageMatch = description.match(/src='([^']+)'/) || description.match(/src="([^"]+)"/)
      const imageUrl = imageMatch ? imageMatch[1] : undefined
      
      return {
        id: `tuoitre-${index}-${Date.now()}`,
        title: item.title || "Untitled",
        url: item.link || "",
        pubDate: item.pubDate ? new Date(item.pubDate).toISOString() : undefined,
        extra: {
          icon: imageUrl
        }
      }
    })
    
    return items
  } catch (error) {
    console.error("[Tuoi Tre] Error:", error)
    throw error
  }
}
```

---

## 4️⃣ Tạo Nguồn Dân Trí

### **Tạo file `server/sources/dantri.ts`**

```typescript
import type { NewsItem, SourceHandler } from "../types"
import { XMLParser } from "fast-xml-parser"

export const handler: SourceHandler = async () => {
  try {
    const response = await fetch("https://dantri.com.vn/rss.htm")
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const xmlText = await response.text()
    
    const parser = new XMLParser({
      ignoreAttributes: false,
      attributeNamePrefix: "@_"
    })
    const result = parser.parse(xmlText)
    
    const rssItems = result.rss?.channel?.item || []
    if (!Array.isArray(rssItems)) {
      throw new Error("Invalid RSS format")
    }
    
    const items: NewsItem[] = rssItems.slice(0, 40).map((item: any, index: number) => {
      const description = item.description || ""
      const imageMatch = description.match(/src="([^"]+)"/)
      const imageUrl = imageMatch ? imageMatch[1] : undefined
      
      return {
        id: `dantri-${index}-${Date.now()}`,
        title: item.title || "Untitled",
        url: item.link || "",
        pubDate: item.pubDate ? new Date(item.pubDate).toISOString() : undefined,
        extra: {
          icon: imageUrl
        }
      }
    })
    
    return items
  } catch (error) {
    console.error("[Dan Tri] Error:", error)
    throw error
  }
}
```

---

## 5️⃣ Đăng Ký Nguồn Tin

### **Sửa file `shared/sources.json`**

Thêm vào cuối file (trước dấu `}`):

```json
{
  "existing sources...": "...",

  "vnexpress": {
    "name": "VnExpress",
    "type": "realtime",
    "column": "vietnam",
    "home": "https://vnexpress.net",
    "color": "red",
    "interval": 300000,
    "title": "Tin mới nhất"
  },
  
  "tuoitre": {
    "name": "Tuổi Trẻ",
    "type": "realtime",
    "column": "vietnam",
    "home": "https://tuoitre.vn",
    "color": "blue",
    "interval": 300000,
    "title": "Tin mới nhất"
  },
  
  "dantri": {
    "name": "Dân Trí",
    "type": "realtime",
    "column": "vietnam",
    "home": "https://dantri.com.vn",
    "color": "orange",
    "interval": 300000,
    "title": "Tin tổng hợp"
  }
}
```

**Giải thích:**
- `column: "vietnam"` - Tạo cột mới "Vietnam" trong UI
- `interval: 300000` - Cache 5 phút (300,000ms)
- `type: "realtime"` - Tin real-time

---

## 6️⃣ Thêm Column "Vietnam"

### **Sửa file `shared/types.ts`**

Tìm `export type SourceColumn` và thêm `"vietnam"`:

```typescript
export type SourceColumn = "china" | "tech" | "finance" | "world" | "vietnam"
//                                                                   ^^^^^^^^
//                                                                   Thêm vào
```

---

## 7️⃣ Test Nguồn Mới

### **Restart server**

```powershell
# Dừng server (Ctrl+C)
# Chạy lại
pnpm dev
```

### **Test API**

```powershell
# Test VnExpress
curl http://localhost:3000/api/s?id=vnexpress

# Test Tuoi Tre
curl http://localhost:3000/api/s?id=tuoitre

# Test Dan Tri
curl http://localhost:3000/api/s?id=dantri
```

**Response mẫu:**
```json
{
  "status": "success",
  "items": [
    {
      "id": "vnexpress-0-1732699800000",
      "title": "Giá vàng hôm nay 27/11: Tăng mạnh sau khi Fed...",
      "url": "https://vnexpress.net/gia-vang-hom-nay-27-11...",
      "pubDate": "2025-11-27T09:30:00.000Z",
      "extra": {
        "icon": "https://i1-kinhdoanh.vnecdn.net/..."
      }
    }
  ],
  "updatedTime": 1732699800000
}
```

✅ **Thành công nếu thấy tin tức Việt Nam!**

---

## 8️⃣ Kiểm Tra Trên Web UI

1. Mở http://localhost:5173
2. Tìm column **Vietnam** (hoặc cuộn xuống)
3. Xem 3 nguồn: VnExpress, Tuổi Trẻ, Dân Trí

![Ảnh demo](https://example.com/demo.png)

---

## ✅ Checklist Hoàn Thành

- [ ] Cài `fast-xml-parser`
- [ ] Tạo `server/sources/vnexpress.ts`
- [ ] Tạo `server/sources/tuoitre.ts`
- [ ] Tạo `server/sources/dantri.ts`
- [ ] Thêm 3 nguồn vào `shared/sources.json`
- [ ] Thêm `"vietnam"` vào `shared/types.ts`
- [ ] Test API 3 nguồn OK
- [ ] Thấy nguồn VN trên Web UI

---

## 🐛 Troubleshooting

### **Lỗi: `Cannot find module 'fast-xml-parser'`**
```powershell
# Cài lại
pnpm add fast-xml-parser

# Restart server
pnpm dev
```

### **Lỗi: `RSS fetch failed`**
- Kiểm tra internet
- Kiểm tra RSS URL còn hoạt động không
- Thử truy cập trực tiếp RSS trong browser

### **Lỗi: `Column 'vietnam' not found`**
- Kiểm tra đã thêm vào `shared/types.ts` chưa
- Restart server

### **Không thấy tin trên Web UI**
- Check console log: `F12` → Console
- Kiểm tra API trả về data chưa: `curl localhost:3000/api/s?id=vnexpress`

---

## 🎨 Tùy Chỉnh (Optional)

### **Thay đổi màu sắc**

Trong `sources.json`:
```json
"vnexpress": {
  "color": "green"  // red, blue, green, orange, purple, v.v.
}
```

### **Thay đổi số lượng tin**

Trong file `.ts`:
```typescript
.slice(0, 40)  // Lấy 40 tin
// Thay thành .slice(0, 20) để lấy 20 tin
```

### **Thêm chuyên mục**

VnExpress có nhiều RSS:
```
Kinh doanh: https://vnexpress.net/rss/kinh-doanh.rss
Thể thao: https://vnexpress.net/rss/the-thao.rss
Công nghệ: https://vnexpress.net/rss/so-hoa.rss
```

Tạo nhiều file, ví dụ:
- `vnexpress-business.ts`
- `vnexpress-tech.ts`

---

## 🎯 Bước Tiếp Theo

Nguồn tin đã hoạt động! Giờ kết nối với TrendRadar:

👉 **[Bước 3: Test Local với TrendRadar](buoc-3-test-local.md)**

---

**Thời gian hoàn thành**: ~2 giờ  
**Độ khó**: ⭐⭐⭐☆☆
