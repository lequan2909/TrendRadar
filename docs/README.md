# 📚 Tài Liệu Hướng Dẫn TrendRadar

## 🌟 Bắt Đầu Nhanh

### **🐍 Setup Python Virtual Environment (BẮT BUỘC)**
👉 **[Hoàn Thành Kế Hoạch](hoan-thanh-ke-hoach.md)** - Setup venv, checklist đầy đủ

```powershell
# Chạy script tự động
.\setup-venv.bat

# Sau đó chạy TrendRadar
.\run.bat
```

### **Mới bắt đầu?**
👉 [README Tiếng Việt](../README-VI.md) - Hướng dẫn cơ bản, cài đặt, cấu hình

### **Muốn test nhanh?**
👉 [Quick Start](QUICKSTART.md) - Tóm tắt 3 bước build nguồn tin VN

---

## 🇻🇳 Build Nguồn Tin Việt Nam

### **Kế Hoạch Hoàn Chỉnh**
- 📋 [Kế Hoạch Tổng Quan](plan-build-nguon-tin-vn.md) - Timeline, checklist, công nghệ
- ⚡ [Quick Start](QUICKSTART.md) - Tóm tắt 3 bước, lỗi thường gặp

### **Hướng Dẫn Từng Bước**
- 🔧 [Bước 1: Setup Newsnow](buoc-1-setup-newsnow.md) - Fork, clone, cài đặt (~30 phút)
- 📰 [Bước 2: Thêm Nguồn VN](buoc-2-them-nguon-vn.md) - VnExpress, Tuổi Trẻ, Dân Trí (~2 giờ)
- 🧪 [Bước 3: Test Local](buoc-3-test-local.md) - Kết nối TrendRadar, nhận tin Telegram (~30 phút)

---

## 📱 Cấu Hình Telegram

- 📱 [Hướng Dẫn Telegram](huong-dan-telegram.md) - Setup bot trong 5 phút

---

## 🌍 Nguồn Tin Hiện Có

- 🔍 [Danh Sách Nguồn Tin](nguon-tin-khac-nhau.md) - 50+ nguồn có sẵn, cách thay đổi

---

## 🗂️ Cấu Hình

- ⚙️ [Biến Môi Trường](../ENVIRONMENT_VARIABLES.md) - Chi tiết tất cả biến env
- 📝 [Kế Hoạch Cấu Hình Vietnam](ke-hoach-cau-hinh-vietnam.md) - Chiến lược từ khóa cho tin VN

---

## 📁 File Mẫu

### **Cấu hình**
- ✅ `config/config.yaml` - Cấu hình chính (đã dịch tiếng Việt)
- ✅ `config/config_international.yaml` - Cấu hình nguồn quốc tế
- ✅ `config/frequency_words_vietnam_investment.txt` - Từ khóa VN & đầu tư

### **Môi trường**
- ✅ `.env.example` - File .env mẫu với Telegram

---

## 🗺️ Roadmap

### **Giai đoạn 1: Setup cơ bản** ✅
- [x] Fork TrendRadar
- [x] Cấu hình Telegram
- [x] Chạy với nguồn tin Trung Quốc

### **Giai đoạn 2: Build nguồn VN** 🔄 (Bạn đang ở đây)
- [ ] Fork newsnow
- [ ] Thêm VnExpress
- [ ] Thêm Tuổi Trẻ
- [ ] Thêm Dân Trí
- [ ] Test local thành công

### **Giai đoạn 3: Production** 🎯
- [ ] Deploy newsnow lên Cloudflare Pages
- [ ] Cấu hình TrendRadar dùng API production
- [ ] Setup GitHub Actions
- [ ] Monitor và maintain

### **Giai đoạn 4: Mở rộng** 🚀
- [ ] Thêm nguồn: Thanh Niên, Zing News
- [ ] Thêm chuyên mục: Kinh tế, Công nghệ, Thể thao
- [ ] Tối ưu từ khóa
- [ ] Tạo dashboard riêng

---

## 🛠️ Công Cụ Hỗ Trợ

### **Debug**
```powershell
# Test newsnow API
curl http://localhost:3000/api/s?id=vnexpress

# Test Telegram
curl "https://api.telegram.org/bot<TOKEN>/getMe"

# Check TrendRadar
python main.py
```

### **Code Snippets**

**Parser RSS mẫu:**
```typescript
import type { NewsItem, SourceHandler } from "../types"
import { XMLParser } from "fast-xml-parser"

export const handler: SourceHandler = async () => {
  const response = await fetch("RSS_URL")
  const xmlText = await response.text()
  const parser = new XMLParser({ ignoreAttributes: false })
  const result = parser.parse(xmlText)
  const items = result.rss?.channel?.item || []
  
  return items.slice(0, 40).map((item: any, i: number) => ({
    id: `id-${i}-${Date.now()}`,
    title: item.title,
    url: item.link,
    pubDate: new Date(item.pubDate).toISOString()
  }))
}
```

---

## ❓ Câu Hỏi Thường Gặp

### **1. Tôi cần cài gì để bắt đầu?**
- Node.js ≥18
- pnpm ≥8
- Python ≥3.10
- Git

### **2. Mất bao lâu để build nguồn tin VN?**
- Setup: 30 phút
- Code: 2 giờ
- Test: 30 phút
- **Tổng: ~3 giờ**

### **3. Có thể dùng nguồn tin sẵn không?**
Có! Xem [nguon-tin-khac-nhau.md](nguon-tin-khac-nhau.md) - có 50+ nguồn (TQ + quốc tế)

### **4. Tôi không biết TypeScript?**
Không sao! Copy code mẫu trong tài liệu, chỉ cần sửa RSS URL.

### **5. Deploy như thế nào?**
3 cách:
- **Cloudflare Pages** (miễn phí, khuyến nghị)
- **VPS** (Ubuntu/Debian)
- **Docker**

---

## 📞 Hỗ Trợ

### **Gặp lỗi?**
1. Check [QUICKSTART.md](QUICKSTART.md) - phần lỗi thường gặp
2. Check từng bước trong docs
3. Test từng component riêng

### **Cần giúp đỡ?**
- GitHub Issues: https://github.com/sansan0/TrendRadar/issues
- Đọc lại tài liệu kỹ
- Debug với curl, console.log

---

## 🎯 Mục Tiêu

Sau khi hoàn thành tài liệu này, bạn sẽ:
- ✅ Hiểu cách TrendRadar hoạt động
- ✅ Biết cách thêm nguồn tin mới
- ✅ Có hệ thống giám sát tin Việt Nam
- ✅ Nhận tin qua Telegram tự động
- ✅ Có thể mở rộng và tùy chỉnh

---

**Bắt đầu ngay**: [Quick Start →](QUICKSTART.md)

**Cập nhật lần cuối**: 2025-11-27
