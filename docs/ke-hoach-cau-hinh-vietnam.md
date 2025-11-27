# 📋 Kế Hoạch Cấu Hình TrendRadar cho Tin Tức Việt Nam & Đầu Tư

## 🎯 Mục Tiêu

Giám sát tin tức từ các nền tảng Trung Quốc (do giới hạn nguồn dữ liệu) nhưng **chỉ lọc tin liên quan đến**:
1. **Việt Nam** - Chính trị, kinh tế, xã hội
2. **Đầu tư quốc tế** - Chứng khoán, tiền tệ, hàng hóa, bất động sản
3. **Sự kiện thế giới** có tác động đến thị trường Việt Nam

---

## 📱 Bước 1: Cấu Hình Telegram

### 1.1. Tạo Telegram Bot

1. **Mở Telegram** → Tìm kiếm `@BotFather`
2. **Gửi lệnh**: `/newbot`
3. **Đặt tên bot**: `TrendRadar Vietnam News Bot` (hoặc tên bạn thích)
4. **Đặt username**: `trendradar_vietnam_bot` (phải kết thúc bằng `_bot`)
5. **Lưu Bot Token**: BotFather sẽ trả về token dạng:
   ```
   123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567
   ```

### 1.2. Lấy Chat ID

**Cách 1: Nhận tin vào cá nhân**
1. Tìm bot vừa tạo trong Telegram
2. Click **Start** hoặc gửi tin nhắn `/start`
3. Mở trình duyệt, truy cập:
   ```
   https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
   ```
   Thay `<BOT_TOKEN>` bằng token ở bước 1.1
4. Tìm `"chat":{"id":123456789}` trong JSON response
5. Lưu số `123456789` đó (Chat ID của bạn)

**Cách 2: Nhận tin vào nhóm**
1. Tạo nhóm Telegram mới
2. Thêm bot vào nhóm
3. Gửi tin nhắn bất kỳ trong nhóm
4. Truy cập URL getUpdates như trên
5. Chat ID của nhóm thường là số âm: `-987654321`

### 1.3. Thêm Biến Môi Trường

#### **Cho GitHub Actions**:
1. Vào repository → **Settings**
2. **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Thêm 2 secrets:

| Name | Secret (Giá trị) |
|------|------------------|
| `TELEGRAM_BOT_TOKEN` | `123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567` |
| `TELEGRAM_CHAT_ID` | `123456789` (hoặc `-987654321` nếu là nhóm) |

#### **Cho Docker**:
```bash
docker run -d \
  --name trendradar-vietnam \
  -e TELEGRAM_BOT_TOKEN="123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567" \
  -e TELEGRAM_CHAT_ID="123456789" \
  -e REPORT_MODE="incremental" \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/output:/app/output \
  wantcat/trendradar:latest
```

#### **Cho Local (Windows PowerShell)**:
```powershell
$env:TELEGRAM_BOT_TOKEN="123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567"
$env:TELEGRAM_CHAT_ID="123456789"
python main.py
```

---

## 🔑 Bước 2: Cấu Hình Từ Khóa (frequency_words.txt)

### 2.1. Chiến Lược Từ Khóa

Vì nguồn tin là Trung Quốc, ta sẽ dùng **từ khóa tiếng Trung** để lọc tin liên quan Việt Nam và đầu tư:

#### **Nhóm 1: Việt Nam** 🇻🇳
```
越南
Vietnam
河内
胡志明
阮富仲
范明政
武文赏
@10
```
**Giải thích**:
- `越南` = Việt Nam (tiếng Trung)
- `Vietnam` = Việt Nam (tiếng Anh, đôi khi xuất hiện)
- `河内` = Hà Nội
- `胡志明` = Hồ Chí Minh (thành phố)
- `阮富仲`, `范明政`, `武文赏` = Lãnh đạo Việt Nam
- `@10` = Giới hạn tối đa 10 tin/nhóm

#### **Nhóm 2: Chứng Khoán & Thị Trường** 📈
```
股市
股票
A股
美股
港股
道琼斯
纳斯达克
标普500
恒生指数
!股东
@15
```
**Giải thích**:
- `股市` = Thị trường chứng khoán
- `股票` = Cổ phiếu
- `A股` = Thị trường A-Share (Trung Quốc)
- `美股` = Chứng khoán Mỹ
- `港股` = Chứng khoán Hong Kong
- `道琼斯`, `纳斯达克`, `标普500` = Dow Jones, Nasdaq, S&P500
- `恒生指数` = Hang Seng Index
- `!股东` = Loại bỏ tin về "cổ đông" (nhiễu)
- `@15` = Tối đa 15 tin

#### **Nhóm 3: Tiền Tệ & Ngoại Hối** 💱
```
美元
人民币
汇率
外汇
美联储
加息
降息
通胀
@10
```
**Giải thích**:
- `美元` = USD
- `人民币` = CNY (Nhân dân tệ)
- `汇率` = Tỷ giá
- `外汇` = Ngoại hối
- `美联储` = Fed (Cục Dự trữ Liên bang Mỹ)
- `加息`, `降息` = Tăng/giảm lãi suất
- `通胀` = Lạm phát

#### **Nhóm 4: Hàng Hóa & Năng Lượng** ⚡
```
石油
黄金
原油
大宗商品
铜价
天然气
布伦特
WTI
@10
```
**Giải thích**:
- `石油` = Dầu
- `黄金` = Vàng
- `原油` = Dầu thô
- `大宗商品` = Hàng hóa đại trà
- `铜价` = Giá đồng
- `天然气` = Khí tự nhiên
- `布伦特`, `WTI` = Brent, WTI (loại dầu)

#### **Nhóm 5: Bất Động Sản** 🏢
```
房地产
楼市
房价
恒大
碧桂园
万科
@8
```
**Giải thích**:
- `房地产` = Bất động sản
- `楼市` = Thị trường nhà
- `房价` = Giá nhà
- `恒大`, `碧桂园`, `万科` = Các tập đoàn BĐS lớn TQ (có ảnh hưởng toàn cầu)

#### **Nhóm 6: Công Nghệ & AI** 🤖
```
人工智能
AI
芯片
半导体
英伟达
台积电
三星
ChatGPT
DeepSeek
!gai
@12
```
**Giải thích**:
- `人工智能` = AI
- `芯片` = Chip
- `半导体` = Bán dẫn
- `英伟达` = NVIDIA
- `台积电` = TSMC
- `三星` = Samsung
- `!gai` = Loại tin nhiễu

#### **Nhóm 7: Quan Hệ Quốc Tế & Địa Chính Trị** 🌍
```
+东盟
ASEAN
中美
中越
俄乌
以色列
巴勒斯坦
制裁
关税
@10
```
**Giải thích**:
- `+东盟` = ASEAN (từ bắt buộc)
- `中美`, `中越` = Trung-Mỹ, Trung-Việt
- `俄乌` = Nga-Ukraine
- `以色列`, `巴勒斯坦` = Israel, Palestine
- `制裁` = Trừng phạt
- `关税` = Thuế quan

#### **Nhóm 8: Kinh Tế Vĩ Mô** 📊
```
GDP
经济增长
失业率
PMI
CPI
央行
@8
```

#### **Nhóm 9: Doanh Nghiệp Lớn** 🏭
```
苹果
特斯拉
比亚迪
阿里巴巴
腾讯
字节跳动
小米
华为
@10
```

---

### 2.2. File Cấu Hình Hoàn Chỉnh

Tạo file `config/frequency_words.txt`:

```text
# === VIỆT NAM ===
越南
Vietnam
河内
胡志明
阮富仲
范明政
武文赏
@10

# === CHỨNG KHOÁN ===
股市
股票
A股
美股
港股
道琼斯
纳斯达克
标普500
恒生指数
!股东
@15

# === NGOẠI HỐI & LÃI SUẤT ===
美元
人民币
汇率
外汇
美联储
加息
降息
通胀
@10

# === HÀNG HÓA & NĂNG LƯỢNG ===
石油
黄金
原油
大宗商品
铜价
天然气
布伦特
WTI
@10

# === BẤT ĐỘNG SẢN ===
房地产
楼市
房价
恒大
碧桂园
万科
@8

# === CÔNG NGHỆ & AI ===
人工智能
AI
芯片
半导体
英伟达
台积电
三星
ChatGPT
DeepSeek
!gai
@12

# === QUAN HỆ QUỐC TẾ ===
+东盟
ASEAN
中美
中越
俄乌
以色列
巴勒斯坦
制裁
关税
@10

# === KINH TẾ VĨ MÔ ===
GDP
经济增长
失业率
PMI
CPI
央行
@8

# === DOANH NGHIỆP LỚN ===
苹果
特斯拉
比亚迪
阿里巴巴
腾讯
字节跳动
小米
华为
@10
```

---

## ⚙️ Bước 3: Tối Ưu Cấu Hình config.yaml

### 3.1. Chế Độ Báo Cáo

**Khuyến nghị**: Dùng `incremental` để tránh spam

```yaml
report:
  mode: "incremental"  # Chỉ nhận tin MỚI
  rank_threshold: 5
  sort_by_position_first: false  # Sắp xếp theo độ hot
  max_news_per_keyword: 0  # Đã giới hạn bằng @số trong từ khóa
```

### 3.2. Cửa Sổ Thời Gian (Tùy Chọn)

Nếu chỉ muốn nhận tin trong giờ làm việc:

```yaml
notification:
  push_window:
    enabled: true
    time_range:
      start: "08:00"  # 8 giờ sáng
      end: "22:00"    # 10 giờ tối
    once_per_day: false  # Nhận nhiều lần trong ngày khi có tin mới
```

### 3.3. Webhook (Chỉ Telegram)

```yaml
webhooks:
  feishu_url: ""
  dingtalk_url: ""
  wework_url: ""
  telegram_bot_token: ""  # ĐỂ TRỐNG - dùng GitHub Secrets
  telegram_chat_id: ""    # ĐỂ TRỐNG - dùng GitHub Secrets
  # ... các kênh khác để trống
```

> ⚠️ **Lưu ý**: Không điền token trực tiếp vào file này nếu dùng GitHub Actions!

---

## 🚀 Bước 4: Triển Khai

### 4.1. GitHub Actions

1. **Commit file cấu hình**:
   ```bash
   git add config/frequency_words.txt
   git commit -m "Cập nhật từ khóa cho tin Việt Nam và đầu tư"
   git push
   ```

2. **Thêm secrets** (xem Bước 1.3)

3. **Kích hoạt workflow**:
   - Vào tab **Actions**
   - Chọn workflow **Hot News Crawler**
   - Click **Run workflow**

### 4.2. Docker

```bash
# Tạo file .env
cat > .env << 'EOF'
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567
TELEGRAM_CHAT_ID=123456789
REPORT_MODE=incremental
PUSH_WINDOW_ENABLED=true
PUSH_WINDOW_START=08:00
PUSH_WINDOW_END=22:00
PUSH_WINDOW_ONCE_PER_DAY=false
EOF

# Chạy container
docker run -d \
  --name trendradar-vietnam \
  --env-file .env \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/output:/app/output \
  --restart unless-stopped \
  wantcat/trendradar:latest
```

---

## 📊 Bước 5: Kiểm Tra Kết Quả

### 5.1. Telegram

- Mở Telegram → Tìm bot của bạn
- Đợi vài phút (GitHub Actions chạy mỗi giờ, Docker tùy cấu hình)
- Bạn sẽ nhận tin dạng:

```
📰 TrendRadar 热点监控
⏰ 2025-11-27 15:45

🔥 越南 (10条)
1. 越南经济增长超预期 GDP达7.2% ⭐NEW
   百度热搜 #3
2. 河内房价上涨20% 创历史新高
   今日头条 #5
...

💹 股市 (15条)
1. 美股三大指数集体收涨 道指创新高 ⭐NEW
   华尔街见闻 #1
...
```

### 5.2. Kiểm Tra Log

**GitHub Actions**:
- Vào tab Actions → Chọn workflow run → Xem log

**Docker**:
```bash
docker logs trendradar-vietnam
```

---

## 🎯 Mẹo Tối Ưu

### 1. Điều Chỉnh Số Lượng Tin
Nếu nhận quá nhiều tin:
- Giảm `@số` trong `frequency_words.txt`
- Ví dụ: `@15` → `@5`

### 2. Thêm Từ Loại Trừ
Nếu có tin nhiễu:
```
股市
!股东
!股民
!股神
```

### 3. Tăng Độ Chính Xác
Dùng từ bắt buộc `+`:
```
+越南
+投资
@5
```
→ Chỉ lấy tin CÓ CẢ "越南" VÀ "投资"

### 4. Theo Dõi Công Ty Việt Nam
Thêm tên tiếng Trung của công ty VN:
```
# Vingroup
文集团

# Viettel
越南军队电信

# Vietnam Airlines
越南航空
```

---

## 🔄 Bảo Trì Định Kỳ

### Hàng tuần:
- [ ] Xem lại từ khóa, loại bỏ từ không hiệu quả
- [ ] Thêm từ khóa mới theo xu hướng

### Hàng tháng:
- [ ] Kiểm tra log, tối ưu cấu hình
- [ ] Cập nhật phiên bản TrendRadar (nếu có)

---

## ❓ FAQ

### Q1: Tại sao không có nguồn tin Việt Nam trực tiếp?
**A**: Dự án hiện chỉ hỗ trợ 11 nền tảng Trung Quốc. Tuy nhiên, tin về Việt Nam và thị trường quốc tế vẫn xuất hiện trên các nền tảng này (Weibo, Toutiao, Baidu, v.v.)

### Q2: Làm sao biết từ khóa tiếng Trung cho các công ty/sự kiện VN?
**A**: Dùng Google Translate hoặc tra Wikipedia tiếng Trung. Ví dụ:
- Hồ Chí Minh → 胡志明
- Hà Nội → 河内
- FPT → 富达 (FPT Corporation)

### Q3: Tin nhắn Telegram quá dài?
**A**: Giảm tổng số `@số` trong tất cả các nhóm. Ví dụ: tổng 100 → 50 tin

### Q4: Không nhận được tin nào?
**A**: Kiểm tra:
- Bot Token và Chat ID đúng chưa?
- Đã gửi `/start` cho bot chưa (nếu chat cá nhân)?
- Xem log có lỗi không?

---

## 📚 Tài Liệu Tham Khảo

- [README Tiếng Việt](../README-VI.md)
- [Hướng Dẫn Biến Môi Trường](../ENVIRONMENT_VARIABLES.md)
- [Telegram Bot API](https://core.telegram.org/bots/api)

---

**Chúc bạn triển khai thành công! 🎉**

*Cập nhật lần cuối: 2025-11-27*
