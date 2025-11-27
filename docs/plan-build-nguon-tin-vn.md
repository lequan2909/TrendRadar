# 📋 Kế Hoạch Build Nguồn Tin Việt Nam

## 🎯 Mục Tiêu

Xây dựng hệ thống giám sát tin tức Việt Nam bằng cách:
1. Fork và mở rộng dự án **newsnow** 
2. Thêm 3 nguồn tin VN để test: **VnExpress**, **Tuổi Trẻ**, **Dân Trí**
3. Deploy local để test
4. Kết nối với **TrendRadar** để nhận tin qua Telegram

---

## 📁 Cấu Trúc Dự Án

```
TrendRadar/
├── newsnow/              # Dự án newsnow (fork)
│   ├── server/
│   │   └── sources/
│   │       ├── vnexpress.ts    # Nguồn VnExpress
│   │       ├── tuoitre.ts      # Nguồn Tuổi Trẻ
│   │       └── dantri.ts       # Nguồn Dân Trí
│   └── shared/
│       └── sources.json        # Cấu hình nguồn
│
├── config/
│   ├── config.yaml            # Cấu hình TrendRadar
│   └── frequency_words.txt    # Từ khóa
│
├── .env                       # Biến môi trường local
└── docs/
    ├── plan-build-nguon-tin-vn.md  # File này
    ├── buoc-1-setup-newsnow.md      # Hướng dẫn setup
    ├── buoc-2-them-nguon-vn.md      # Thêm nguồn VN
    └── buoc-3-test-local.md         # Test local
```

---

## 🗓️ Timeline & Checklist

### **Giai đoạn 1: Setup môi trường** ⏱️ ~30 phút
- [ ] Cài đặt Node.js, pnpm
- [ ] Fork newsnow về thư mục `newsnow/`
- [ ] Cài đặt dependencies
- [ ] Chạy test để đảm bảo hoạt động

### **Giai đoạn 2: Thêm nguồn tin VN** ⏱️ ~2 giờ
- [ ] Nghiên cứu RSS/API của VnExpress
- [ ] Tạo parser cho VnExpress
- [ ] Nghiên cứu RSS/API của Tuổi Trẻ
- [ ] Tạo parser cho Tuổi Trẻ
- [ ] Nghiên cứu RSS/API của Dân Trí
- [ ] Tạo parser cho Dân Trí
- [ ] Thêm cấu hình vào `sources.json`

### **Giai đoạn 3: Deploy local** ⏱️ ~30 phút
- [ ] Build newsnow
- [ ] Chạy server local
- [ ] Test API endpoints

### **Giai đoạn 4: Kết nối TrendRadar** ⏱️ ~30 phút
- [ ] Cấu hình TrendRadar dùng API local
- [ ] Tạo file `.env` với Telegram
- [ ] Chạy test local
- [ ] Kiểm tra nhận tin qua Telegram

### **Giai đoạn 5: Tối ưu** ⏱️ ~1 giờ
- [ ] Tinh chỉnh từ khóa
- [ ] Điều chỉnh interval
- [ ] Xử lý lỗi
- [ ] Tài liệu hóa

**Tổng thời gian dự kiến: ~5 giờ**

---

## 🛠️ Công Nghệ Sử Dụng

| Công nghệ | Phiên bản | Mục đích |
|-----------|-----------|----------|
| **Node.js** | ≥18.0.0 | Runtime cho newsnow |
| **pnpm** | ≥8.0.0 | Package manager |
| **TypeScript** | ≥5.0.0 | Ngôn ngữ lập trình |
| **Python** | ≥3.10 | Chạy TrendRadar |
| **Telegram Bot** | - | Nhận thông báo |

---

## 📚 Tài Liệu Hướng Dẫn

### **Bước 1: Setup Newsnow**
👉 Xem chi tiết: [`buoc-1-setup-newsnow.md`](buoc-1-setup-newsnow.md)
- Cài đặt môi trường
- Fork và clone dự án
- Cài dependencies
- Chạy test

### **Bước 2: Thêm Nguồn Tin VN**
👉 Xem chi tiết: [`buoc-2-them-nguon-vn.md`](buoc-2-them-nguon-vn.md)
- Cấu trúc parser
- Thêm VnExpress
- Thêm Tuổi Trẻ
- Thêm Dân Trí

### **Bước 3: Test Local**
👉 Xem chi tiết: [`buoc-3-test-local.md`](buoc-3-test-local.md)
- Build và chạy newsnow
- Cấu hình TrendRadar
- Test nhận tin Telegram

---

## 🎯 Kết Quả Mong Đợi

Sau khi hoàn thành, bạn sẽ có:

### **1. API Local Newsnow**
```bash
# Chạy trên http://localhost:3000
curl http://localhost:3000/api/s?id=vnexpress
```

Response:
```json
{
  "status": "success",
  "items": [
    {
      "title": "Giá vàng hôm nay tăng vọt",
      "url": "https://vnexpress.net/...",
      "pubDate": "2025-11-27T16:00:00Z"
    }
  ]
}
```

### **2. TrendRadar Nhận Tin VN**

Telegram sẽ hiển thị:
```
📰 TrendRadar - Tin Việt Nam
⏰ 27/11/2025 16:20

🇻🇳 Kinh tế (5 tin)
1. Giá vàng hôm nay tăng vọt ⭐NEW
   VnExpress #1
2. VN-Index vượt 1200 điểm
   Tuổi Trẻ #3
...
```

---

## ⚠️ Lưu Ý Quan Trọng

### **1. Về RSS Feed**
- VnExpress: Có RSS công khai
- Tuổi Trẻ: Có RSS công khai
- Dân Trí: Có RSS công khai
- **Lưu ý**: Không scrape trực tiếp HTML để tránh bị block

### **2. Về Tần Suất Cập Nhật**
- RSS thường cache 5-10 phút
- Không request quá nhanh (khuyến nghị: ≥5 phút/lần)

### **3. Về Deploy**
- **Giai đoạn test**: Chạy local
- **Giai đoạn production**: Deploy lên VPS hoặc Cloudflare Pages

---

## 🚀 Bắt Đầu

Sẵn sàng? Hãy bắt đầu từ:

👉 **[Bước 1: Setup Newsnow](buoc-1-setup-newsnow.md)**

---

**Thời gian cập nhật**: 2025-11-27  
**Tác giả**: TrendRadar Vietnam Team
