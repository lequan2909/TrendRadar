# TrendRadar - Hướng Dẫn Sử Dụng (Tiếng Việt)

## 📌 Giới Thiệu Dự Án

**TrendRadar** là một công cụ giám sát và tổng hợp tin tức nóng hổi từ nhiều nền tảng mạng xã hội và tin tức lớn. Dự án giúp bạn:

- **Theo dõi xu hướng**: Giám sát 11 nền tảng lớn (Zhihu, Douyin, Bilibili, Weibo, Baidu, v.v.)
- **Lọc thông tin**: Chỉ nhận tin tức phù hợp với từ khóa quan tâm
- **Nhận thông báo**: Đẩy tin qua nhiều kênh (WeChat, Telegram, Email, Feishu, DingTalk, ntfy)
- **Phân tích AI**: Tích hợp MCP (Model Context Protocol) để phân tích xu hướng tin tức
- **Triển khai dễ dàng**: Hỗ trợ GitHub Actions, Docker, và deployment thủ công

---

## 🚀 Triển Khai Nhanh

### Phương Án 1: GitHub Actions (Khuyến nghị cho người mới)

1. **Fork dự án** về tài khoản GitHub của bạn
2. **Cấu hình GitHub Secrets** (xem mục [Biến Môi Trường](#-biến-môi-trường))
3. **Kích hoạt GitHub Actions**: Vào tab "Actions" → Enable workflows
4. **Kích hoạt GitHub Pages** (tùy chọn): Settings → Pages → Source: `gh-pages`

### Phương Án 2: Docker

```bash
# Pull image chính thức
docker pull wantcat/trendradar:latest

# Chạy container
docker run -d \
  --name trendradar \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/output:/app/output \
  -e FEISHU_WEBHOOK_URL="your_webhook_url" \
  -e REPORT_MODE="daily" \
  wantcat/trendradar:latest
```

### Phương Án 3: Chạy Thủ Công (Local)

```bash
# Clone dự án
git clone https://github.com/sansan0/TrendRadar.git
cd TrendRadar

# Cài đặt dependencies
pip install -r requirements.txt

# Cấu hình file config/config.yaml và config/frequency_words.txt
# (Xem hướng dẫn chi tiết bên dưới)

# Chạy
python main.py
```

---

## ⚙️ Cấu Hình Chi Tiết

### 1. File `config/config.yaml`

File này chứa tất cả cấu hình chính của dự án:

#### **a) Cấu hình ứng dụng (`app`)**
```yaml
app:
  version_check_url: "https://raw.githubusercontent.com/sansan0/TrendRadar/refs/heads/master/version"
  show_version_update: true  # Hiển thị thông báo phiên bản mới
```

#### **b) Cấu hình crawler (`crawler`)**
```yaml
crawler:
  request_interval: 1000     # Khoảng cách giữa các request (ms)
  enable_crawler: true       # Bật/tắt chức năng thu thập tin
  use_proxy: false           # Sử dụng proxy (true/false)
  default_proxy: "http://127.0.0.1:10086"
```

#### **c) Chế độ báo cáo (`report`)**
```yaml
report:
  mode: "daily"                    # Chế độ: daily/current/incremental
  rank_threshold: 5                # Ngưỡng highlight tin quan trọng
  sort_by_position_first: false    # Sắp xếp theo vị trí cấu hình hay theo độ hot
  max_news_per_keyword: 0          # Giới hạn số tin mỗi từ khóa (0 = không giới hạn)
```

**Ba Chế độ Báo Cáo:**

| Chế độ | Mô tả | Phù hợp với |
|--------|-------|-------------|
| `daily` | Tổng hợp tất cả tin trong ngày | Muốn xem toàn bộ xu hướng ngày |
| `current` | Chỉ tin đang hot trên bảng xếp hạng hiện tại | Theo dõi real-time |
| `incremental` | Chỉ tin MỚI xuất hiện, không lặp lại | Tránh spam, chỉ quan tâm tin mới |

#### **d) Cấu hình thông báo (`notification`)**
```yaml
notification:
  enable_notification: true        # Bật/tắt thông báo
  message_batch_size: 4000         # Kích thước batch gửi tin (bytes)
  dingtalk_batch_size: 20000       # Batch riêng cho DingTalk
  feishu_batch_size: 29000         # Batch riêng cho Feishu
  batch_send_interval: 3           # Khoảng cách giữa các batch (giây)
```

#### **e) Cửa sổ thời gian đẩy tin (`push_window`)**
```yaml
  push_window:
    enabled: false                 # Bật/tắt giới hạn khung giờ
    time_range:
      start: "20:00"               # Giờ bắt đầu (múi giờ Bắc Kinh)
      end: "22:00"                 # Giờ kết thúc
    once_per_day: true             # Chỉ gửi 1 lần/ngày trong khung giờ
    push_record_retention_days: 7  # Lưu lịch sử gửi tin bao nhiêu ngày
```

#### **f) Webhooks (QUAN TRỌNG)**

> ⚠️ **CẢNH BÁO BẢO MẬT**: Không bao giờ để lộ webhook URL ra công khai! Nếu deploy qua GitHub, hãy dùng GitHub Secrets thay vì ghi trực tiếp vào file này.

```yaml
  webhooks:
    feishu_url: ""                 # Webhook Feishu/Lark
    dingtalk_url: ""               # Webhook DingTalk
    wework_url: ""                 # Webhook WeChat Work
    wework_msg_type: "markdown"    # markdown hoặc text
    telegram_bot_token: ""         # Telegram Bot Token
    telegram_chat_id: ""           # Telegram Chat ID
    email_from: ""                 # Email gửi
    email_password: ""             # Mật khẩu email/App password
    email_to: ""                   # Email nhận (phân cách bằng dấu phẩy)
    email_smtp_server: ""          # SMTP server (để trống = tự động)
    email_smtp_port: ""            # SMTP port (để trống = tự động)
    ntfy_server_url: "https://ntfy.sh"
    ntfy_topic: ""                 # ntfy topic
    ntfy_token: ""                 # ntfy token (tùy chọn)
```

#### **g) Trọng số tính điểm tin (`weight`)**
```yaml
weight:
  rank_weight: 0.6        # Điểm từ thứ hạng (60%)
  frequency_weight: 0.3   # Điểm từ số lần xuất hiện (30%)
  hotness_weight: 0.1     # Điểm từ độ hot tổng thể (10%)
```

#### **h) Danh sách nền tảng (`platforms`)**
```yaml
platforms:
  - id: "toutiao"
    name: "今日头条"
  - id: "baidu"
    name: "百度热搜"
  - id: "zhihu"
    name: "知乎"
  # ... và 8 nền tảng khác
```

### 2. File `config/frequency_words.txt`

File này định nghĩa **từ khóa** bạn muốn theo dõi. Cú pháp:

#### **Cú pháp cơ bản:**
- **Từ khóa thông thường**: Viết bình thường, mỗi dòng 1 từ
- **Từ bắt buộc**: Thêm `+` phía trước (ví dụ: `+AI`)
- **Từ loại trừ**: Thêm `!` phía trước (ví dụ: `!gai` để loại "gái" khi tìm "ai")
- **Giới hạn số lượng**: Thêm `@số` (ví dụ: `@5` để chỉ lấy 5 tin)
- **Nhóm từ khóa**: Cách nhau bằng dòng trống

**Ví dụ:**
```
AI
!gai
@10

+华为
+鸿蒙
@5

比亚迪
王传福
```

Giải thích:
- Nhóm 1: Tìm "AI", loại bỏ "gai", tối đa 10 tin
- Nhóm 2: Tìm tin CÓ CẢ "华为" VÀ "鸿蒙", tối đa 5 tin
- Nhóm 3: Tìm "比亚迪" HOẶC "王传福", không giới hạn số lượng

---

## 🔐 Biến Môi Trường

### **Biến Bắt Buộc**

Để dự án chạy, bạn phải cấu hình **ít nhất 1 kênh thông báo** trong số các kênh sau:

| Biến | Mô tả | Ví dụ |
|------|-------|-------|
| `FEISHU_WEBHOOK_URL` | Webhook Feishu/Lark | `https://open.feishu.cn/open-apis/bot/v2/hook/xxx` |
| `DINGTALK_WEBHOOK_URL` | Webhook DingTalk | `https://oapi.dingtalk.com/robot/send?access_token=xxx` |
| `WEWORK_WEBHOOK_URL` | Webhook WeChat Work | `https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx` |
| `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` | Telegram Bot | Token: `123456:ABC-DEF...`, Chat ID: `123456789` |
| `EMAIL_FROM` + `EMAIL_PASSWORD` + `EMAIL_TO` | Email | From: `user@gmail.com`, Password: App Password, To: `receiver@gmail.com` |
| `NTFY_TOPIC` | ntfy Topic | `my-trendradar-alerts` |

> **Lưu ý**: Nếu deploy qua GitHub Actions, hãy thêm các biến này vào **GitHub Secrets** (Settings → Secrets and variables → Actions → New repository secret)

---

### **Biến Tùy Chọn**

| Biến | Mô tả | Giá trị mặc định | Ghi chú |
|------|-------|------------------|---------|
| `REPORT_MODE` | Chế độ báo cáo | `daily` | `daily`/`current`/`incremental` |
| `ENABLE_CRAWLER` | Bật/tắt thu thập tin | `true` | `true`/`false` |
| `ENABLE_NOTIFICATION` | Bật/tắt thông báo | `true` | `true`/`false` |
| `PUSH_WINDOW_ENABLED` | Bật/tắt cửa sổ thời gian | `false` | `true`/`false` |
| `PUSH_WINDOW_START` | Giờ bắt đầu khung gửi | `20:00` | Định dạng `HH:MM` |
| `PUSH_WINDOW_END` | Giờ kết thúc khung gửi | `22:00` | Định dạng `HH:MM` |
| `PUSH_WINDOW_ONCE_PER_DAY` | Chỉ gửi 1 lần/ngày | `true` | `true`/`false` |
| `PUSH_WINDOW_RETENTION_DAYS` | Lưu lịch sử bao lâu | `7` | Số ngày |
| `SORT_BY_POSITION_FIRST` | Sắp xếp theo vị trí cấu hình | `false` | `true`/`false` |
| `MAX_NEWS_PER_KEYWORD` | Giới hạn tin/từ khóa | `0` | `0` = không giới hạn |
| `WEWORK_MSG_TYPE` | Loại tin WeChat Work | `markdown` | `markdown`/`text` |
| `EMAIL_SMTP_SERVER` | SMTP server | Auto-detect | Ví dụ: `smtp.gmail.com` |
| `EMAIL_SMTP_PORT` | SMTP port | Auto-detect | Ví dụ: `587` (TLS) hoặc `465` (SSL) |
| `NTFY_SERVER_URL` | ntfy server URL | `https://ntfy.sh` | Có thể dùng self-hosted |
| `NTFY_TOKEN` | ntfy access token | (trống) | Cho private topic |
| `CONFIG_PATH` | Đường dẫn file cấu hình | `config/config.yaml` | - |
| `FREQUENCY_WORDS_PATH` | Đường dẫn file từ khóa | `config/frequency_words.txt` | - |

---

### **Sử dụng với GitHub Actions**

Thêm biến vào **GitHub Secrets**:

1. Vào repository → **Settings**
2. Chọn **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Nhập **Name** (ví dụ: `FEISHU_WEBHOOK_URL`)
5. Nhập **Secret** (giá trị webhook)
6. Click **Add secret**

---

### **Sử dụng với Docker**

Truyền biến môi trường qua tham số `-e`:

```bash
docker run -d \
  --name trendradar \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/output:/app/output \
  -e FEISHU_WEBHOOK_URL="https://open.feishu.cn/..." \
  -e REPORT_MODE="incremental" \
  -e PUSH_WINDOW_ENABLED="true" \
  -e PUSH_WINDOW_START="08:00" \
  -e PUSH_WINDOW_END="20:00" \
  wantcat/trendradar:latest
```

Hoặc dùng file `.env`:

```bash
# Tạo file .env
cat > .env << EOF
FEISHU_WEBHOOK_URL=https://open.feishu.cn/...
REPORT_MODE=daily
ENABLE_NOTIFICATION=true
EOF

# Chạy với --env-file
docker run -d \
  --name trendradar \
  --env-file .env \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/output:/app/output \
  wantcat/trendradar:latest
```

---

### **Sử dụng với Docker Compose**

Tạo file `docker-compose.yml`:

```yaml
version: '3.8'

services:
  trendradar:
    image: wantcat/trendradar:latest
    container_name: trendradar
    restart: unless-stopped
    volumes:
      - ./config:/app/config
      - ./output:/app/output
    environment:
      # Biến bắt buộc (chọn ít nhất 1 kênh)
      FEISHU_WEBHOOK_URL: "${FEISHU_WEBHOOK_URL}"
      # TELEGRAM_BOT_TOKEN: "${TELEGRAM_BOT_TOKEN}"
      # TELEGRAM_CHAT_ID: "${TELEGRAM_CHAT_ID}"
      
      # Biến tùy chọn
      REPORT_MODE: "daily"
      ENABLE_CRAWLER: "true"
      ENABLE_NOTIFICATION: "true"
      PUSH_WINDOW_ENABLED: "false"
      # PUSH_WINDOW_START: "08:00"
      # PUSH_WINDOW_END: "20:00"
```

Chạy:
```bash
docker-compose up -d
```

---

## 📊 Tính Năng AI (MCP)

Dự án hỗ trợ **Model Context Protocol** để phân tích tin tức bằng AI:

- Phân tích xu hướng
- Tìm kiếm tin liên quan
- Thống kê nền tảng
- Tóm tắt thông minh

Chi tiết xem file `README-MCP-FAQ.md` và thư mục `mcp_server/`.

---

## 📝 Câu Hỏi Thường Gặp

### 1. Làm sao để chỉ nhận tin mới, không nhận lại tin đã thấy?
→ Đặt `REPORT_MODE=incremental` hoặc sửa `mode: "incremental"` trong `config/config.yaml`

### 2. Làm sao để chỉ nhận tin trong giờ làm việc?
→ Bật `push_window` trong `config/config.yaml`:
```yaml
push_window:
  enabled: true
  time_range:
    start: "09:00"
    end: "18:00"
  once_per_day: false
```

### 3. Tôi muốn theo dõi tin về AI nhưng không muốn nhận tin về "gái"?
→ Dùng từ loại trừ trong `frequency_words.txt`:
```
AI
!gái
!gai
```

### 4. Làm sao để nhận nhiều email cùng lúc?
→ Trong `EMAIL_TO`, phân cách bằng dấu phẩy:
```
EMAIL_TO=user1@gmail.com,user2@yahoo.com,user3@outlook.com
```

### 5. GitHub Actions không gửi thông báo?
→ Kiểm tra:
- Đã thêm webhook vào GitHub Secrets chưa?
- Workflow đã được Enable chưa? (Tab Actions)
- Xem log của workflow để biết lỗi

### 6. Docker container không chạy?
→ Kiểm tra log:
```bash
docker logs trendradar
```

---

## 📂 Cấu Trúc Thư Mục

```
TrendRadar/
├── config/
│   ├── config.yaml              # Cấu hình chính
│   └── frequency_words.txt      # Từ khóa theo dõi
├── output/                      # Dữ liệu đầu ra
│   └── 2025年11月27日/
│       ├── html/               # File HTML
│       └── txt/                # File TXT
├── mcp_server/                  # MCP AI server
├── .github/workflows/
│   └── crawler.yml             # GitHub Actions workflow
├── main.py                     # File chính
├── requirements.txt            # Dependencies Python
├── README.md                   # Hướng dẫn tiếng Trung
├── README-EN.md                # Hướng dẫn tiếng Anh
└── README-VI.md                # Hướng dẫn tiếng Việt (file này)
```

---

## 📜 Giấy Phép

Dự án này sử dụng giấy phép **GPL-3.0**. Xem file `LICENSE` để biết thêm chi tiết.

---

## 🙏 Cảm Ơn

- Dự án sử dụng API từ [newsnow](https://github.com/ourongxing/newsnow)
- Tác giả gốc: [sansan0](https://github.com/sansan0/TrendRadar)
- Đóng góp từ cộng đồng GitHub

---

## 🔗 Liên Kết Hữu Ích

- **Repository chính thức**: https://github.com/sansan0/TrendRadar
- **Docker Hub**: https://hub.docker.com/r/wantcat/trendradar
- **Issues/Bug Reports**: https://github.com/sansan0/TrendRadar/issues

---

**Chúc bạn sử dụng TrendRadar hiệu quả! 🎉**
