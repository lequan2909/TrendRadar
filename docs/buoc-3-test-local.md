# 🧪 Bước 3: Test Local với TrendRadar

## 🎯 Mục Tiêu

Kết nối TrendRadar với newsnow local để nhận tin Việt Nam qua Telegram.

---

## 1️⃣ Chuẩn Bị Telegram Bot

### **Tạo Bot (nếu chưa có)**

```
1. Mở Telegram → Tìm @BotFather
2. Gửi: /newbot
3. Đặt tên: TrendRadar Vietnam Bot
4. Username: trendradar_vn_bot
5. Lưu Bot Token: 123456789:ABCdef...
```

### **Lấy Chat ID**

```
1. Gửi tin nhắn cho bot: /start
2. Truy cập:
   https://api.telegram.org/bot<TOKEN>/getUpdates
3. Lưu Chat ID: 123456789
```

---

## 2️⃣ Tạo File .env Cho TrendRadar

### **Tạo file `C:\Users\trung\TrendRadar\.env`**

```bash
# === CẤU HÌNH TELEGRAM ===
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567
TELEGRAM_CHAT_ID=123456789

# === CẤU HÌNH CHẾ ĐỘ ===
REPORT_MODE=incremental
ENABLE_CRAWLER=true
ENABLE_NOTIFICATION=true

# === CẤU HÌNH CỬA SỔ THỜI GIAN (tùy chọn) ===
PUSH_WINDOW_ENABLED=false
# PUSH_WINDOW_START=08:00
# PUSH_WINDOW_END=22:00
```

**Lưu ý:** Thay `123456789:ABC...` bằng token thật của bạn!

---

## 3️⃣ Sửa TrendRadar Dùng API Local

### **Tạo file backup**

```powershell
cd C:\Users\trung\TrendRadar
cp main.py main.py.backup
```

### **Sửa file `main.py`**

Tìm dòng:
```python
url = f"https://newsnow.busiyi.world/api/s?id={id_value}&latest"
```

Thay thành:
```python
# Dùng API local
url = f"http://localhost:3000/api/s?id={id_value}&latest"
```

Tìm ở khoảng **dòng 467** trong hàm `fetch_data()`.

---

## 4️⃣ Cấu Hình Nguồn Tin VN

### **Sửa file `config/config.yaml`**

Thay phần `platforms:`:

```yaml
platforms:
  # === NGUỒN TIN VIỆT NAM ===
  - id: "vnexpress"
    name: "VnExpress"
  
  - id: "tuoitre"
    name: "Tuổi Trẻ"
  
  - id: "dantri"
    name: "Dân Trí"
```

### **Cấu hình từ khóa (tùy chọn)**

Tạo `config/frequency_words.txt`:

```text
# === KINH TẾ ===
vàng
USD
VN-Index
chứng khoán
lãi suất
@10

# === CHÍNH TRỊ ===
Quốc hội
Chính phủ
Thủ tướng
@8

# === XÃ HỘI ===
giáo dục
y tế
giao thông
@8

# === CÔNG NGHỆ ===
FPT
Viettel
VinSmart
AI
@5
```

Hoặc **để trống** để nhận TẤT CẢ tin.

---

## 5️⃣ Chạy Test

### **Terminal 1: Chạy Newsnow**

```powershell
# Di chuyển vào newsnow
cd C:\Users\trung\TrendRadar\newsnow

# Chạy server
pnpm dev

# Đợi output:
# Server running on http://localhost:3000
```

### **Terminal 2: Chạy TrendRadar**

Mở PowerShell mới:

```powershell
# Di chuyển vào TrendRadar
cd C:\Users\trung\TrendRadar

# Load .env và chạy
python main.py
```

---

## 6️⃣ Kiểm Tra Kết Quả

### **Output Terminal 2 (TrendRadar)**

```
正在加载配置...
配置文件加载成功: config/config.yaml
TrendRadar v3.2.0 配置加载完成
监控平台数量: 3
通知渠道配置来源: Telegram(环境变量)

获取 vnexpress 成功（最新数据）
获取 tuoitre 成功（最新数据）
获取 dantri 成功（最新数据）

成功: ['vnexpress', 'tuoitre', 'dantri'], 失败: []

...推送到 Telegram 成功...
```

### **Telegram**

Mở Telegram → Tìm bot → Sẽ thấy tin:

```
📰 TrendRadar 热点监控
⏰ 2025-11-27 16:45

🇻🇳 vàng (3条)
1. Giá vàng hôm nay 27/11: Tăng mạnh lên 89 triệu ⭐NEW
   VnExpress #1
2. Vàng SJC tăng 500.000 đồng/lượng
   Tuổi Trẻ #2

💹 chứng khoán (2条)
1. VN-Index vượt mốc 1.200 điểm ⭐NEW
   Dân Trí #3
...
```

✅ **Thành công nếu nhận được tin VN qua Telegram!**

---

## 7️⃣ Tùy Chỉnh

### **Thay đổi tần suất**

Sửa `.github/workflows/crawler.yml`:

```yaml
schedule:
  - cron: "*/5 * * * *"  # Mỗi 5 phút (cho test)
  # - cron: "0 * * * *"  # Mỗi giờ (production)
```

### **Chỉ nhận tin Việt Nam**

Sửa `config/frequency_words.txt`, xóa hết, để trống = nhận tất cả.

Hoặc thêm từ khóa phủ định để loại tin Trung Quốc:

```text
!中国
!北京
!上海

# Chỉ giữ từ khóa VN
Việt Nam
Hà Nội
TP.HCM
```

---

## 8️⃣ Cấu Trúc File Sau Khi Hoàn Thành

```
TrendRadar/
├── newsnow/                     # Dự án newsnow
│   ├── server/
│   │   └── sources/
│   │       ├── vnexpress.ts    ✅
│   │       ├── tuoitre.ts      ✅
│   │       └── dantri.ts       ✅
│   └── shared/
│       └── sources.json        ✅ (đã thêm 3 nguồn VN)
│
├── config/
│   ├── config.yaml             ✅ (3 nguồn VN)
│   └── frequency_words.txt     ✅ (từ khóa VN)
│
├── .env                        ✅ (Telegram config)
├── main.py                     ✅ (đã sửa dùng localhost)
│
└── docs/
    ├── plan-build-nguon-tin-vn.md
    ├── buoc-1-setup-newsnow.md
    ├── buoc-2-them-nguon-vn.md
    └── buoc-3-test-local.md    ← Bạn đang ở đây
```

---

## ✅ Checklist Hoàn Thành

- [ ] Tạo Telegram Bot và lấy token
- [ ] Lấy Chat ID
- [ ] Tạo file `.env` với Telegram config
- [ ] Sửa `main.py` dùng `http://localhost:3000`
- [ ] Cấu hình `config.yaml` với 3 nguồn VN
- [ ] Tạo/sửa `frequency_words.txt`
- [ ] Chạy newsnow: `pnpm dev`
- [ ] Chạy TrendRadar: `python main.py`
- [ ] Nhận tin VN qua Telegram ✅

---

## 🐛 Troubleshooting

### **Lỗi: `Connection refused localhost:3000`**
```powershell
# Kiểm tra newsnow có chạy không
curl http://localhost:3000/api/s?id=vnexpress

# Nếu không chạy, vào thư mục newsnow:
cd C:\Users\trung\TrendRadar\newsnow
pnpm dev
```

### **Lỗi: TrendRadar không load .env**

Windows PowerShell không tự động load `.env`. Dùng cách này:

```powershell
# Option 1: Set từng biến
$env:TELEGRAM_BOT_TOKEN="123456789:ABC..."
$env:TELEGRAM_CHAT_ID="123456789"
$env:REPORT_MODE="incremental"
python main.py

# Option 2: Dùng python-dotenv (khuyến nghị)
pip install python-dotenv
```

Thêm vào đầu `main.py`:
```python
from dotenv import load_dotenv
load_dotenv()  # Load .env
```

### **Không nhận tin Telegram**

```powershell
# Kiểm tra token và chat ID
curl https://api.telegram.org/bot<TOKEN>/getMe
curl https://api.telegram.org/bot<TOKEN>/getUpdates

# Gửi tin test
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" `
  -d "chat_id=<CHAT_ID>&text=Test"
```

### **Nhận tin nhưng toàn tiếng Trung**

- Kiểm tra `config.yaml` có 3 nguồn VN chưa
- Kiểm tra newsnow có chạy và trả về tin VN không:
  ```powershell
  curl http://localhost:3000/api/s?id=vnexpress
  ```

---

## 🎉 Hoàn Thành!

Chúc mừng! Bạn đã:
- ✅ Fork và mở rộng newsnow
- ✅ Thêm 3 nguồn tin Việt Nam
- ✅ Kết nối TrendRadar với newsnow local
- ✅ Nhận tin VN qua Telegram

---

## 🚀 Bước Tiếp Theo

### **Deploy lên Production**

Có 3 lựa chọn:

#### **1. Cloudflare Pages** (Miễn phí, khuyến nghị)
- Fork newsnow đã sửa lên GitHub
- Kết nối với Cloudflare Pages
- Auto deploy
- Lấy URL: `https://your-newsnow.pages.dev`
- Sửa TrendRadar dùng URL này

#### **2. VPS (Ubuntu/Debian)**
```bash
# Cài Node.js, pnpm
# Clone newsnow
# pnpm build
# pm2 start
```

#### **3. Docker**
```dockerfile
FROM node:18
WORKDIR /app
COPY . .
RUN pnpm install
RUN pnpm build
CMD ["pnpm", "start"]
```

### **Tài liệu thêm**

- 📖 [Deploy Cloudflare Pages](buoc-4-deploy-production.md) (TODO)
- 📖 [Thêm nguồn tin khác](buoc-5-them-nguon-khac.md) (TODO)

---

**Thời gian hoàn thành**: ~30 phút  
**Độ khó**: ⭐⭐⭐☆☆  
**Kết quả**: 🎉 Nhận tin Việt Nam qua Telegram!
