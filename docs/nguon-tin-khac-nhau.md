# 🌍 Hướng Dẫn Thay Đổi Nguồn Tin - TrendRadar

## 📊 Tình Hình Hiện Tại

### ✅ Nguồn Tin Hiện Hỗ Trợ

Dự án TrendRadar hiện sử dụng API từ **newsnow.busiyi.world**, hỗ trợ **50+ nguồn tin** bao gồm:

#### 🇨🇳 **Trung Quốc** (China)
- 知乎 (Zhihu)
- 微博 (Weibo) 
- 抖音 (Douyin)
- 百度热搜 (Baidu)
- 今日头条 (Toutiao)
- 哔哩哔哩 (Bilibili)
- 贴吧 (Tieba)
- 澎湃新闻 (ThePaper)
- 凤凰网 (Ifeng)
- 腾讯新闻 (Tencent News)
- 虎扑 (Hupu)
- 快手 (Kuaishou)
- 豆瓣 (Douban)
- 牛客 (Nowcoder)
- 虫部落 (Chongbuluo)

#### 💰 **Tài Chính** (Finance)
- 华尔街见闻 (WallStreetCN) - **Tin quốc tế**
- 财联社 (CLS)
- 雪球 (Xueqiu)
- 格隆汇 (Gelonghui)
- 法布财经 (Fastbull)
- 金十数据 (Jin10)
- MKTNews

#### 🌐 **Quốc Tế** (World)
- **Hacker News** - Tin công nghệ Mỹ
- **Product Hunt** - Sản phẩm công nghệ mới
- **Github Trending** - Dự án GitHub hot
- **Steam** - Thống kê game
- **联合早报 (Zaobao)** - Singapore
- 卫星通讯社 (Sputnik News CN) - Nga
- 参考消息 (Cankaoxiaoxi) - Tin quốc tế
- 靠谱新闻 (Kaopu News)

#### 💻 **Công Nghệ** (Tech)
- V2EX
- 酷安 (Coolapk)
- IT之家 (ITHome)
- 36氪 (36Kr)
- 少数派 (SSPAI)
- 稀土掘金 (Juejin)
- Solidot
- 远景论坛 (PCBeta)

---

## ❌ Nguồn Tin KHÔNG Hỗ Trợ

### **Việt Nam** 🇻🇳
Hiện tại **KHÔNG** có nguồn tin Việt Nam:
- ❌ VnExpress
- ❌ Tuổi Trẻ
- ❌ Thanh Niên
- ❌ Zing News
- ❌ Dân Trí
- ❌ VOV
- ❌ VTV

### **Tin Tức Quốc Tế Chính**
- ❌ BBC
- ❌ CNN
- ❌ Reuters
- ❌ Bloomberg
- ❌ Financial Times
- ❌ The Guardian
- ❌ New York Times

---

## 🔧 Cách Thay Đổi Nguồn Tin

### **Phương Án 1: Sử Dụng Nguồn Tin Có Sẵn** ⭐ (Khuyến nghị)

Bạn có thể thay đổi trong `config/config.yaml`:

```yaml
platforms:
  # === TÀI CHÍNH QUỐC TẾ ===
  - id: "wallstreetcn-hot"
    name: "华尔街见闻 (Hot)"
  
  - id: "wallstreetcn-quick"
    name: "华尔街见闻 (Tin nhanh)"
  
  - id: "wallstreetcn-news"
    name: "华尔街见闻 (Mới nhất)"
  
  - id: "jin10"
    name: "金十数据 (Tài chính)"
  
  - id: "xueqiu-hotstock"
    name: "雪球 (Chứng khoán hot)"
  
  # === CÔNG NGHỆ QUỐC TẾ ===
  - id: "hackernews"
    name: "Hacker News"
  
  - id: "producthunt"
    name: "Product Hunt"
  
  - id: "github-trending-today"
    name: "Github Trending"
  
  - id: "solidot"
    name: "Solidot (Tech News)"
  
  # === TIN TỨC THẾ GIỚI ===
  - id: "zaobao"
    name: "联合早报 (Singapore)"
  
  - id: "sputniknewscn"
    name: "卫星通讯社 (Sputnik)"
  
  - id: "cankaoxiaoxi"
    name: "参考消息 (Tin quốc tế)"
  
  - id: "kaopu"
    name: "靠谱新闻"
  
  # === GIẢI TRÍ & KHÁC ===
  - id: "steam"
    name: "Steam (Games)"
  
  - id: "douban"
    name: "豆瓣 (Movies)"
```

### **Danh Sách Đầy Đủ ID Có Sẵn**

Bạn có thể dùng bất kỳ ID nào sau:

<details>
<summary>📋 Click để xem 50+ nguồn tin (ID → Tên)</summary>

```
v2ex-share → V2EX 最新分享
zhihu → 知乎
weibo → 微博 实时热搜
zaobao → 联合早报 (Singapore)
coolapk → 酷安 今日最热
mktnews-flash → MKTNews 快讯
wallstreetcn-quick → 华尔街见闻 快讯
wallstreetcn-news → 华尔街见闻 最新
wallstreetcn-hot → 华尔街见闻 最热
36kr-quick → 36氪 快讯
douyin → 抖音
hupu → 虎扑 主干道热帖
tieba → 百度贴吧 热议
toutiao → 今日头条
ithome → IT之家
thepaper → 澎湃新闻 热榜
sputniknewscn → 卫星通讯社
cankaoxiaoxi → 参考消息
pcbeta-windows11 → 远景论坛 Win11
cls-telegraph → 财联社 电报
cls-depth → 财联社 深度
cls-hot → 财联社 热门
xueqiu-hotstock → 雪球 热门股票
gelonghui → 格隆汇 事件
fastbull-express → 法布财经 快讯
fastbull-news → 法布财经 头条
solidot → Solidot
hackernews → Hacker News
producthunt → Product Hunt
github-trending-today → Github Trending Today
bilibili-hot-search → 哔哩哔哩 热搜
bilibili-hot-video → 哔哩哔哩 热门视频
bilibili-ranking → 哔哩哔哩 排行榜
kuaishou → 快手
kaopu → 靠谱新闻
jin10 → 金十数据
baidu → 百度热搜
nowcoder → 牛客
sspai → 少数派
juejin → 稀土掘金
ifeng → 凤凰网 热点资讯
chongbuluo-latest → 虫部落 最新
chongbuluo-hot → 虫部落 最热
douban → 豆瓣 热门电影
steam → Steam 在线人数
tencent-hot → 腾讯新闻 综合早报
```

</details>

---

### **Phương Án 2: Tự Build Nguồn Tin Mới** 🔨 (Nâng cao)

Nếu muốn thêm nguồn tin Việt Nam (VnExpress, Tuổi Trẻ, v.v.), bạn cần:

#### **Bước 1: Fork dự án newsnow**
```bash
git clone https://github.com/ourongxing/newsnow.git
cd newsnow
```

#### **Bước 2: Tạo nguồn mới**

Tạo file `server/sources/vnexpress.ts`:

```typescript
import type { NewsItem, SourceHandler } from "../types"

export const handler: SourceHandler = async () => {
  const response = await fetch("https://vnexpress.net/rss/tin-moi-nhat.rss")
  const xml = await response.text()
  
  // Parse RSS feed
  const items: NewsItem[] = parseRSS(xml)
  
  return items
}
```

Thêm vào `shared/sources.json`:

```json
{
  "vnexpress": {
    "name": "VnExpress",
    "column": "vietnam",
    "home": "https://vnexpress.net",
    "color": "red",
    "interval": 300000,
    "title": "Tin mới nhất"
  }
}
```

#### **Bước 3: Deploy lên server riêng**

```bash
# Build
pnpm build

# Deploy lên Cloudflare Pages hoặc server riêng
```

#### **Bước 4: Sử dụng API riêng**

Sửa file `main.py` của TrendRadar:

```python
# Thay đổi từ
url = f"https://newsnow.busiyi.world/api/s?id={id_value}&latest"

# Thành
url = f"https://your-domain.com/api/s?id={id_value}&latest"
```

---

## 🎯 Giải Pháp Khuyến Nghị

### **Cho Tin Việt Nam + Đầu Tư**

Vì hiện không có nguồn tin Việt Nam trực tiếp, tôi khuyến nghị:

#### **Cấu hình 1: Tập trung Tài chính Quốc tế**

```yaml
platforms:
  # Tin tài chính - ảnh hưởng đến VN
  - id: "wallstreetcn-hot"
    name: "华尔街见闻"
  - id: "jin10"
    name: "金十数据"
  - id: "xueqiu-hotstock"
    name: "雪球"
  - id: "cls-hot"
    name: "财联社"
  
  # Tin quốc tế
  - id: "zaobao"
    name: "联合早报"
  - id: "cankaoxiaoxi"
    name: "参考消息"
  
  # Tin công nghệ quốc tế
  - id: "hackernews"
    name: "Hacker News"
  - id: "github-trending-today"
    name: "Github"
```

Kết hợp với từ khóa:

```
# Từ khóa về ASEAN/Việt Nam
越南
东盟
ASEAN
中越

# Từ khóa tài chính
美股
美元
加息
降息
通胀

# Công nghệ
AI
芯片
半导体
```

#### **Cấu hình 2: Cân bằng Trung Quốc + Quốc tế**

```yaml
platforms:
  # Top 5 Trung Quốc (cho tin về VN)
  - id: "toutiao"
    name: "今日头条"
  - id: "baidu"
    name: "百度热搜"
  - id: "weibo"
    name: "微博"
  - id: "zhihu"
    name: "知乎"
  - id: "thepaper"
    name: "澎湃新闻"
  
  # Tài chính quốc tế
  - id: "wallstreetcn-hot"
    name: "华尔街见闻"
  - id: "jin10"
    name: "金十数据"
  
  # Tech quốc tế
  - id: "hackernews"
    name: "Hacker News"
```

---

## 🔄 Cách Áp Dụng Thay Đổi

### **1. Backup cấu hình cũ**

```bash
cp config/config.yaml config/config.yaml.backup
```

### **2. Sửa file config/config.yaml**

Thay thế phần `platforms:` bằng cấu hình mới.

### **3. Commit thay đổi**

```bash
git add config/config.yaml
git commit -m "Cập nhật nguồn tin quốc tế"
git push
```

### **4. Kiểm tra**

Chạy thử:
```bash
python main.py
```

Hoặc trigger GitHub Actions.

---

## 📈 So Sánh Nguồn Tin

| Nguồn | Loại | Tần suất cập nhật | Phù hợp với |
|-------|------|-------------------|-------------|
| 华尔街见闻 | Tài chính | 5 phút | Đầu tư, chứng khoán |
| 金十数据 | Tài chính | 10 phút | Tin nhanh tài chính |
| Hacker News | Tech | 10 phút | Công nghệ, startup |
| 联合早报 | Tin tức | 30 phút | Tin Đông Nam Á |
| Github Trending | Tech | 10 phút | Dự án mã nguồn mở |

---

## ⚠️ Lưu Ý

### **1. Không có nguồn tin Việt Nam chính thống**
- Tin về Việt Nam chỉ xuất hiện **khi nổi bật** trên nền tảng Trung Quốc/quốc tế
- Dùng từ khóa "越南", "Vietnam" để lọc

### **2. API giới hạn**
- Mỗi nguồn có `interval` riêng (thời gian cache)
- Không nên thêm quá nhiều nguồn (>15) để tránh quá tải

### **3. Ngôn ngữ**
- Hầu hết nguồn là **tiếng Trung**
- Một số nguồn quốc tế: Hacker News, Github, Product Hunt (**tiếng Anh**)

---

## 🚀 Kế Hoạch Tương Lai

### **Nếu bạn muốn nguồn tin Việt Nam**

Có 2 lựa chọn:

#### **Option A: Đóng góp vào dự án newsnow**
1. Fork https://github.com/ourongxing/newsnow
2. Thêm nguồn VnExpress, Tuổi Trẻ, v.v.
3. Tạo Pull Request
4. Đợi tác giả merge

#### **Option B: Tự host newsnow riêng**
1. Clone newsnow + thêm nguồn VN
2. Deploy lên server riêng (VPS, Cloudflare Pages)
3. Sửa TrendRadar để dùng API của bạn

#### **Option C: Sử dụng dự án khác**
- Tìm dự án tương tự hỗ trợ RSS feed Việt Nam
- Hoặc tự build scraper riêng cho VnExpress, Tuổi Trẻ

---

## 📚 Tài Liệu Tham Khảo

- [Newsnow GitHub](https://github.com/ourongxing/newsnow)
- [Newsnow Contributing Guide](https://github.com/ourongxing/newsnow/blob/main/CONTRIBUTING.md)
- [TrendRadar README-VI](../README-VI.md)

---

**Cập nhật: 2025-11-27**
