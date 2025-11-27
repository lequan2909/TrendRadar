# 📱 Hướng Dẫn Setup Telegram cho TrendRadar

## Bước 1: Tạo Telegram Bot (2 phút)

1. Mở Telegram → Tìm **@BotFather**
2. Gửi lệnh: `/newbot`
3. Đặt tên bot: `TrendRadar Vietnam Bot`
4. Đặt username: `trendradar_vietnam_bot` (phải có `_bot` ở cuối)
5. **Lưu lại Bot Token**:
   ```
   123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567
   ```

## Bước 2: Lấy Chat ID (1 phút)

### Cách A: Nhận tin vào cá nhân

1. Tìm bot vừa tạo trong Telegram
2. Click **Start** (hoặc gửi `/start`)
3. Mở trình duyệt, vào:
   ```
   https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
   ```
   Thay `<BOT_TOKEN>` bằng token ở Bước 1
   
4. Tìm dòng:
   ```json
   "chat":{"id":123456789,"first_name":"..."}
   ```
   
5. **Lưu lại Chat ID**: `123456789`

### Cách B: Nhận tin vào nhóm

1. Tạo nhóm mới trong Telegram
2. Thêm bot vào nhóm
3. **Cấp quyền Admin** cho bot (quan trọng!)
4. Gửi tin nhắn bất kỳ trong nhóm
5. Truy cập URL getUpdates như Cách A
6. **Lưu lại Chat ID** (số âm): `-987654321`

---

## Bước 3: Cấu Hình Biến Môi Trường

### ✅ GitHub Actions (Khuyến nghị)

1. Vào repository → **Settings**
2. **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Thêm **2 secrets**:

#### Secret 1:
- **Name**: `TELEGRAM_BOT_TOKEN`
- **Secret**: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567`

#### Secret 2:
- **Name**: `TELEGRAM_CHAT_ID`
- **Secret**: `123456789` (hoặc `-987654321` nếu nhóm)

5. Click **Add secret**

### ✅ Docker

```bash
docker run -d \
  --name trendradar \
  -e TELEGRAM_BOT_TOKEN="123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567" \
  -e TELEGRAM_CHAT_ID="123456789" \
  -e REPORT_MODE="incremental" \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/output:/app/output \
  wantcat/trendradar:latest
```

### ✅ Local (Windows PowerShell)

```powershell
$env:TELEGRAM_BOT_TOKEN="123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567"
$env:TELEGRAM_CHAT_ID="123456789"
$env:REPORT_MODE="incremental"
python main.py
```

---

## Bước 4: Kiểm Tra

### Test ngay lập tức (không cần đợi workflow)

```bash
# Chạy thử local
python main.py
```

Hoặc trigger GitHub Actions:
1. Vào tab **Actions**
2. Chọn **Hot News Crawler**
3. Click **Run workflow**

### Xem kết quả

Mở Telegram → Tìm bot/nhóm → Đợi vài phút → Nhận tin!

---

## 🔧 Troubleshooting

### ❌ Lỗi: "Chat not found"
**Giải pháp**: Gửi tin nhắn `/start` cho bot (nếu chat cá nhân)

### ❌ Lỗi: "Forbidden: bot was blocked by the user"
**Giải pháp**: Vào chat với bot → Click **Restart** hoặc **Unblock**

### ❌ Lỗi: "Bad Request: chat not found"
**Giải pháp**: 
- Kiểm tra lại Chat ID
- Nếu nhóm: Đảm bảo bot vẫn còn trong nhóm

### ❌ Không nhận được tin
**Kiểm tra**:
1. Bot Token đúng chưa?
2. Chat ID đúng chưa?
3. Nếu nhóm: Bot có quyền gửi tin không?
4. File `config/frequency_words.txt` có từ khóa chưa?

---

## ⚡ Quick Start (3 dòng lệnh)

Sau khi đã có Bot Token và Chat ID:

```bash
# 1. Thay thế file từ khóa
cp config/frequency_words_vietnam_investment.txt config/frequency_words.txt

# 2. Set biến môi trường (Windows PowerShell)
$env:TELEGRAM_BOT_TOKEN="YOUR_TOKEN_HERE"
$env:TELEGRAM_CHAT_ID="YOUR_CHAT_ID_HERE"

# 3. Chạy
python main.py
```

---

## 📚 Tài Liệu Chi Tiết

- [Kế Hoạch Cấu Hình Vietnam](ke-hoach-cau-hinh-vietnam.md)
- [README Tiếng Việt](../README-VI.md)
- [Hướng Dẫn Biến Môi Trường](../ENVIRONMENT_VARIABLES.md)

---

**Thời gian setup: ~5 phút**

*Cập nhật: 2025-11-27*
