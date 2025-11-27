# ⚡ Quick Start - Build Nguồn Tin VN

## 📋 Tóm Tắt 3 Bước

### **Bước 1: Setup Newsnow** (~30 phút)
```powershell
# 1. Cài Node.js + pnpm
node --version  # ≥18
pnpm --version  # ≥8

# 2. Fork và clone
cd C:\Users\trung\TrendRadar
git clone https://github.com/YOUR_USERNAME/newsnow.git
cd newsnow

# 3. Cài dependencies
pnpm install

# 4. Test chạy
pnpm dev
# → http://localhost:3000
```

### **Bước 2: Thêm Nguồn VN** (~2 giờ)
```powershell
# 1. Cài parser
pnpm add fast-xml-parser

# 2. Tạo 3 file trong server/sources/
# - vnexpress.ts
# - tuoitre.ts
# - dantri.ts

# 3. Thêm vào shared/sources.json
# - vnexpress
# - tuoitre
# - dantri

# 4. Thêm "vietnam" vào shared/types.ts
```

### **Bước 3: Test Local** (~30 phút)
```powershell
# 1. Tạo .env
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
REPORT_MODE=incremental

# 2. Sửa main.py
# Đổi https://newsnow.busiyi.world
# → http://localhost:3000

# 3. Sửa config.yaml
platforms:
  - id: "vnexpress"
  - id: "tuoitre"
  - id: "dantri"

# 4. Chạy
# Terminal 1:
cd newsnow
pnpm dev

# Terminal 2:
cd TrendRadar
python main.py

# 5. Check Telegram! 📱
```

---

## 📂 File Cần Tạo/Sửa

### **Newsnow**
- ✅ `server/sources/vnexpress.ts` - Parser VnExpress
- ✅ `server/sources/tuoitre.ts` - Parser Tuổi Trẻ
- ✅ `server/sources/dantri.ts` - Parser Dân Trí
- ✅ `shared/sources.json` - Thêm 3 nguồn
- ✅ `shared/types.ts` - Thêm "vietnam"

### **TrendRadar**
- ✅ `.env` - Telegram config
- ✅ `main.py` - Sửa dùng localhost
- ✅ `config/config.yaml` - 3 nguồn VN
- ✅ `config/frequency_words.txt` - Từ khóa VN

---

## 🚨 Các Lỗi Thường Gặp

| Lỗi | Nguyên nhân | Giải pháp |
|-----|-------------|-----------|
| `pnpm: command not found` | Chưa cài pnpm | `npm install -g pnpm` |
| `Port 3000 in use` | Port bị chiếm | Kill process hoặc đổi port |
| `Connection refused localhost:3000` | Newsnow chưa chạy | `cd newsnow && pnpm dev` |
| `.env not loaded` | PowerShell không load | Set từng biến hoặc dùng `python-dotenv` |
| `Invalid RSS format` | RSS thay đổi cấu trúc | Check RSS URL, sửa parser |
| Không nhận Telegram | Token/Chat ID sai | Check lại token, test với curl |

---

## 📖 Tài Liệu Chi Tiết

- 📄 [Kế Hoạch Tổng Quan](plan-build-nguon-tin-vn.md)
- 📄 [Bước 1: Setup Newsnow](buoc-1-setup-newsnow.md)
- 📄 [Bước 2: Thêm Nguồn VN](buoc-2-them-nguon-vn.md)
- 📄 [Bước 3: Test Local](buoc-3-test-local.md)

---

## 💡 Tips

### **Debug nhanh**
```powershell
# Test newsnow API
curl http://localhost:3000/api/s?id=vnexpress

# Test Telegram
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" `
  -d "chat_id=<CHAT_ID>&text=Test"

# Check TrendRadar log
python main.py 2>&1 | Select-String "error|success|失败|成功"
```

### **Code Snippets**

Parser mẫu (copy vào `.ts`):
```typescript
import type { NewsItem, SourceHandler } from "../types"
import { XMLParser } from "fast-xml-parser"

export const handler: SourceHandler = async () => {
  const response = await fetch("RSS_URL_HERE")
  const xmlText = await response.text()
  
  const parser = new XMLParser({
    ignoreAttributes: false,
    attributeNamePrefix: "@_"
  })
  const result = parser.parse(xmlText)
  const rssItems = result.rss?.channel?.item || []
  
  return rssItems.slice(0, 40).map((item: any, index: number) => ({
    id: `SOURCE-${index}-${Date.now()}`,
    title: item.title || "Untitled",
    url: item.link || "",
    pubDate: item.pubDate ? new Date(item.pubDate).toISOString() : undefined
  }))
}
```

---

## 🎯 Kết Quả

Sau 3 giờ, bạn có:
- ✅ Newsnow chạy local với 3 nguồn VN
- ✅ TrendRadar lấy tin từ newsnow
- ✅ Nhận tin VN qua Telegram
- ✅ Có thể thêm nguồn mới dễ dàng

---

**Bắt đầu ngay**: [Bước 1 →](buoc-1-setup-newsnow.md)
