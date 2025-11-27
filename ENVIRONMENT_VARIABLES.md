# 🔐 Biến Môi Trường - TrendRadar

## 📋 Bảng Tóm Tắt Nhanh

### ✅ Biến Bắt Buộc (Chọn ít nhất 1 kênh thông báo)

| Tên Biến | Loại | Mô Tả | Ví Dụ |
|----------|------|-------|-------|
| `FEISHU_WEBHOOK_URL` | **Bắt buộc nếu dùng Feishu** | URL webhook của Feishu/Lark bot | `https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxx` |
| `DINGTALK_WEBHOOK_URL` | **Bắt buộc nếu dùng DingTalk** | URL webhook của DingTalk bot | `https://oapi.dingtalk.com/robot/send?access_token=xxxx` |
| `WEWORK_WEBHOOK_URL` | **Bắt buộc nếu dùng WeChat Work** | URL webhook của WeChat Work bot | `https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx` |
| `TELEGRAM_BOT_TOKEN` | **Bắt buộc nếu dùng Telegram** | Token của Telegram bot | `123456789:ABCdefGHIjklMNOpqrsTUVwxyz` |
| `TELEGRAM_CHAT_ID` | **Bắt buộc nếu dùng Telegram** | Chat ID của nhóm/cá nhân nhận tin | `123456789` hoặc `-987654321` |
| `EMAIL_FROM` | **Bắt buộc nếu dùng Email** | Địa chỉ email gửi | `mybot@gmail.com` |
| `EMAIL_PASSWORD` | **Bắt buộc nếu dùng Email** | Mật khẩu email hoặc App Password | `abcd efgh ijkl mnop` (Gmail App Password) |
| `EMAIL_TO` | **Bắt buộc nếu dùng Email** | Địa chỉ email nhận (nhiều email cách nhau bằng dấu phẩy) | `user1@gmail.com,user2@yahoo.com` |
| `NTFY_TOPIC` | **Bắt buộc nếu dùng ntfy** | Tên topic ntfy | `my-trendradar-alerts` |

---

### ⚙️ Biến Tùy Chọn

| Tên Biến | Loại | Giá Trị Mặc Định | Mô Tả | Giá Trị Hợp Lệ |
|----------|------|------------------|-------|----------------|
| `REPORT_MODE` | Tùy chọn | `daily` | Chế độ báo cáo | `daily`, `current`, `incremental` |
| `ENABLE_CRAWLER` | Tùy chọn | `true` | Bật/tắt thu thập tin tức | `true`, `false` |
| `ENABLE_NOTIFICATION` | Tùy chọn | `true` | Bật/tắt gửi thông báo | `true`, `false` |
| `PUSH_WINDOW_ENABLED` | Tùy chọn | `false` | Bật/tắt giới hạn khung giờ gửi tin | `true`, `false` |
| `PUSH_WINDOW_START` | Tùy chọn | `20:00` | Giờ bắt đầu khung gửi tin (định dạng HH:MM) | `08:00`, `09:30`, v.v. |
| `PUSH_WINDOW_END` | Tùy chọn | `22:00` | Giờ kết thúc khung gửi tin (định dạng HH:MM) | `18:00`, `22:30`, v.v. |
| `PUSH_WINDOW_ONCE_PER_DAY` | Tùy chọn | `true` | Chỉ gửi 1 lần/ngày trong khung giờ | `true`, `false` |
| `PUSH_WINDOW_RETENTION_DAYS` | Tùy chọn | `7` | Số ngày lưu lịch sử gửi tin | Số nguyên dương (ví dụ: `7`, `14`, `30`) |
| `SORT_BY_POSITION_FIRST` | Tùy chọn | `false` | Sắp xếp theo thứ tự cấu hình từ khóa thay vì độ hot | `true`, `false` |
| `MAX_NEWS_PER_KEYWORD` | Tùy chọn | `0` | Giới hạn số tin mỗi từ khóa (0 = không giới hạn) | Số nguyên không âm (ví dụ: `0`, `5`, `10`) |
| `WEWORK_MSG_TYPE` | Tùy chọn | `markdown` | Định dạng tin nhắn WeChat Work | `markdown`, `text` |
| `EMAIL_SMTP_SERVER` | Tùy chọn | Auto-detect | Địa chỉ SMTP server (để trống = tự động nhận diện) | `smtp.gmail.com`, `smtp.qq.com`, v.v. |
| `EMAIL_SMTP_PORT` | Tùy chọn | Auto-detect | Cổng SMTP (để trống = tự động nhận diện) | `587` (TLS), `465` (SSL), `25` |
| `NTFY_SERVER_URL` | Tùy chọn | `https://ntfy.sh` | URL server ntfy (có thể dùng self-hosted) | `https://ntfy.sh`, `https://my-ntfy.com` |
| `NTFY_TOKEN` | Tùy chọn | *(trống)* | Token xác thực ntfy (cho private topic) | `tk_xxxxxxxxxxxxxxxx` |
| `CONFIG_PATH` | Tùy chọn | `config/config.yaml` | Đường dẫn file cấu hình chính | Đường dẫn tương đối hoặc tuyệt đối |
| `FREQUENCY_WORDS_PATH` | Tùy chọn | `config/frequency_words.txt` | Đường dẫn file từ khóa | Đường dẫn tương đối hoặc tuyệt đối |

---

## 📖 Chi Tiết Từng Biến

### 🔔 Kênh Thông Báo

#### 1. Feishu/Lark
```bash
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxx
```
- **Cách lấy**: Tạo bot trong Feishu → Lấy webhook URL
- **Lưu ý**: Feishu có giới hạn độ dài tin nhắn, dự án tự động chia batch

#### 2. DingTalk
```bash
DINGTALK_WEBHOOK_URL=https://oapi.dingtalk.com/robot/send?access_token=xxxx
```
- **Cách lấy**: Tạo custom bot trong DingTalk group
- **Lưu ý**: Có thể cần cấu hình keyword hoặc IP whitelist

#### 3. WeChat Work (企业微信)
```bash
WEWORK_WEBHOOK_URL=https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx
WEWORK_MSG_TYPE=markdown  # hoặc text
```
- **markdown**: Hỗ trợ định dạng rich text (cho bot trong group)
- **text**: Tin nhắn văn bản thuần túy (cho ứng dụng cá nhân)

#### 4. Telegram
```bash
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
```
- **Cách lấy Bot Token**: Chat với @BotFather → `/newbot`
- **Cách lấy Chat ID**:
  - Cho nhóm: Thêm @userinfobot vào group → lấy ID
  - Cho cá nhân: Chat với @userinfobot → lấy ID

#### 5. Email
```bash
EMAIL_FROM=mybot@gmail.com
EMAIL_PASSWORD=abcd efgh ijkl mnop
EMAIL_TO=user1@gmail.com,user2@outlook.com
EMAIL_SMTP_SERVER=smtp.gmail.com    # Tùy chọn
EMAIL_SMTP_PORT=587                 # Tùy chọn
```

**SMTP Auto-detect** (để trống `EMAIL_SMTP_SERVER` và `EMAIL_SMTP_PORT`):
- Gmail: `smtp.gmail.com:587` (TLS)
- QQ Mail: `smtp.qq.com:465` (SSL)
- Outlook: `smtp-mail.outlook.com:587` (TLS)
- 163 Mail: `smtp.163.com:465` (SSL)
- 126 Mail: `smtp.126.com:465` (SSL)

**Lưu ý Gmail**: Phải dùng **App Password**, không dùng mật khẩu thường
- Vào https://myaccount.google.com/security
- Bật 2-Step Verification
- Tạo App Password → Dùng password đó

#### 6. ntfy
```bash
NTFY_TOPIC=my-trendradar-alerts
NTFY_SERVER_URL=https://ntfy.sh            # Hoặc self-hosted URL
NTFY_TOKEN=tk_xxxxxxxxxxxxxxxx             # Tùy chọn cho private topic
```
- **Public topic**: Chỉ cần `NTFY_TOPIC`
- **Private topic**: Cần thêm `NTFY_TOKEN`
- **Self-hosted**: Thay đổi `NTFY_SERVER_URL`

---

### 🎯 Chế Độ Báo Cáo

#### `REPORT_MODE`

| Giá trị | Mô tả | Khi nào dùng |
|---------|-------|--------------|
| `daily` | Tổng hợp toàn bộ tin trong ngày | Muốn xem overview ngày, không quan tâm lặp lại |
| `current` | Chỉ tin đang hot trên bảng xếp hạng hiện tại | Theo dõi real-time, chấp nhận lặp lại |
| `incremental` | Chỉ tin MỚI, không lặp lại | Muốn tránh spam, chỉ quan tâm tin mới |

**Ví dụ**:
```bash
REPORT_MODE=incremental  # Chỉ nhận tin mới, không lặp
```

---

### ⏰ Cửa Sổ Thời Gian

Giới hạn khung giờ gửi tin để tránh làm phiền ngoài giờ:

```bash
PUSH_WINDOW_ENABLED=true
PUSH_WINDOW_START=09:00       # Bắt đầu lúc 9 giờ sáng
PUSH_WINDOW_END=18:00         # Kết thúc lúc 6 giờ chiều
PUSH_WINDOW_ONCE_PER_DAY=true # Chỉ gửi 1 lần/ngày
```

**Kịch bản ứng dụng**:
- **Giờ làm việc**: `09:00` - `18:00`
- **Buổi tối**: `20:00` - `22:00`
- **Cả ngày**: Tắt `PUSH_WINDOW_ENABLED=false`

---

### 🔢 Kiểm Soát Số Lượng Tin

#### `MAX_NEWS_PER_KEYWORD`
Giới hạn toàn cục số tin mỗi từ khóa:

```bash
MAX_NEWS_PER_KEYWORD=10  # Tối đa 10 tin cho mỗi từ khóa
MAX_NEWS_PER_KEYWORD=0   # Không giới hạn (mặc định)
```

**Lưu ý**: Có thể override cho từng từ khóa riêng trong `frequency_words.txt` bằng cú pháp `@số`:
```
AI
@5    # Chỉ lấy 5 tin dù MAX_NEWS_PER_KEYWORD là bao nhiêu
```

---

### 📊 Sắp Xếp Tin

#### `SORT_BY_POSITION_FIRST`

```bash
SORT_BY_POSITION_FIRST=true   # Sắp xếp theo thứ tự từ khóa trong file
SORT_BY_POSITION_FIRST=false  # Sắp xếp theo độ hot (mặc định)
```

**Ví dụ**: `frequency_words.txt`
```
比亚迪
特斯拉
AI
```

- `false`: Tin về AI (nhiều nhất) → Tin về 比亚迪 → Tin về 特斯拉
- `true`: Tin về 比亚迪 → Tin về 特斯拉 → Tin về AI (theo thứ tự file)

---

## 🛠️ Cách Sử Dụng Biến Môi Trường

### 1️⃣ GitHub Actions

Thêm vào **GitHub Secrets**:
1. Vào repository → Settings
2. Secrets and variables → Actions
3. New repository secret
4. Nhập Name (ví dụ: `FEISHU_WEBHOOK_URL`) và Secret (giá trị)

**File `.github/workflows/crawler.yml` đã cấu hình sẵn**:
```yaml
env:
  FEISHU_WEBHOOK_URL: ${{ secrets.FEISHU_WEBHOOK_URL }}
  TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
  # ... các biến khác
```

### 2️⃣ Docker Run

```bash
docker run -d \
  --name trendradar \
  -e FEISHU_WEBHOOK_URL="https://open.feishu.cn/..." \
  -e REPORT_MODE="incremental" \
  -e PUSH_WINDOW_ENABLED="true" \
  -e PUSH_WINDOW_START="09:00" \
  -e PUSH_WINDOW_END="18:00" \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/output:/app/output \
  wantcat/trendradar:latest
```

### 3️⃣ Docker Compose

Tạo file `.env`:
```bash
FEISHU_WEBHOOK_URL=https://open.feishu.cn/...
TELEGRAM_BOT_TOKEN=123456:ABC-DEF
TELEGRAM_CHAT_ID=123456789
REPORT_MODE=daily
ENABLE_CRAWLER=true
ENABLE_NOTIFICATION=true
```

Tạo `docker-compose.yml`:
```yaml
version: '3.8'
services:
  trendradar:
    image: wantcat/trendradar:latest
    env_file: .env
    environment:
      PUSH_WINDOW_ENABLED: "false"
    volumes:
      - ./config:/app/config
      - ./output:/app/output
```

### 4️⃣ Local Python

**Linux/Mac**:
```bash
export FEISHU_WEBHOOK_URL="https://open.feishu.cn/..."
export REPORT_MODE="incremental"
python main.py
```

**Windows (PowerShell)**:
```powershell
$env:FEISHU_WEBHOOK_URL="https://open.feishu.cn/..."
$env:REPORT_MODE="incremental"
python main.py
```

**Windows (CMD)**:
```cmd
set FEISHU_WEBHOOK_URL=https://open.feishu.cn/...
set REPORT_MODE=incremental
python main.py
```

---

## ⚠️ Lưu Ý Bảo Mật

### ❌ KHÔNG BAO GIỜ
- Commit webhook URL vào Git
- Public webhook URL
- Share webhook URL qua chat không mã hóa

### ✅ NÊN
- Dùng GitHub Secrets cho GitHub Actions
- Dùng `.env` file và thêm vào `.gitignore`
- Rotate (đổi) webhook định kỳ
- Dùng private repository nếu fork

---

## 🆘 Troubleshooting

### Lỗi: "未配置任何webhook" (Chưa cấu hình webhook)
**Nguyên nhân**: Không có biến môi trường nào được cấu hình
**Giải pháp**: Thêm ít nhất 1 webhook (ví dụ: `FEISHU_WEBHOOK_URL`)

### Lỗi: GitHub Actions không gửi thông báo
**Kiểm tra**:
1. Đã thêm webhook vào Secrets chưa?
2. Tên biến có đúng không? (phân biệt hoa thường)
3. Xem log: Actions tab → chọn workflow run → xem log

### Lỗi: Email không gửi được
**Kiểm tra**:
1. Gmail: Đang dùng App Password chưa?
2. SMTP port: `587` (TLS) hoặc `465` (SSL)?
3. Allow less secure apps: Tắt đi, dùng App Password

### Lỗi: Telegram không nhận tin
**Kiểm tra**:
1. Bot đã được thêm vào nhóm chưa?
2. Chat ID đúng chưa? (ID nhóm thường bắt đầu bằng `-`)
3. Bot có quyền gửi tin không?

---

## 📚 Tài Liệu Liên Quan

- **README Tiếng Việt**: [README-VI.md](README-VI.md)
- **README Chính Thức**: [README.md](README.md)
- **README Tiếng Anh**: [README-EN.md](README-EN.md)
- **MCP FAQ**: [README-MCP-FAQ.md](README-MCP-FAQ.md)

---

**Cập nhật lần cuối**: 2025-11-27
