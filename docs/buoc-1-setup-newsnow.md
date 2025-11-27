# 🔧 Bước 1: Setup Newsnow

## 📋 Chuẩn Bị

### **Yêu cầu hệ thống**
- Windows 10/11
- Node.js ≥18.0.0
- pnpm ≥8.0.0
- Git

---

## 1️⃣ Cài Đặt Node.js và pnpm

### **Cài Node.js**

```powershell
# Kiểm tra đã cài chưa
node --version

# Nếu chưa có, download tại:
# https://nodejs.org/en/download/ (chọn LTS)
```

### **Cài pnpm**

```powershell
# Cài qua npm
npm install -g pnpm

# Kiểm tra
pnpm --version
# Output: 8.x.x
```

---

## 2️⃣ Fork và Clone Newsnow

### **Fork trên GitHub**

1. Mở https://github.com/ourongxing/newsnow
2. Click nút **Fork** ở góc phải trên
3. Chọn tài khoản của bạn
4. Đợi fork hoàn tất

### **Clone về máy**

```powershell
# Di chuyển vào thư mục TrendRadar
cd C:\Users\trung\TrendRadar

# Clone dự án newsnow (thay YOUR_USERNAME)
git clone https://github.com/YOUR_USERNAME/newsnow.git

# Di chuyển vào thư mục
cd newsnow
```

---

## 3️⃣ Cài Đặt Dependencies

```powershell
# Cài tất cả packages
pnpm install

# Đợi vài phút...
# Output: "Dependencies installed successfully"
```

---

## 4️⃣ Cấu Trúc Dự Án

Sau khi clone, bạn sẽ có:

```
newsnow/
├── server/              # Backend (API)
│   ├── sources/        # ⭐ Nơi thêm nguồn tin VN
│   │   ├── zhihu.ts
│   │   ├── weibo.ts
│   │   └── ...
│   └── index.ts
│
├── shared/            # Shared code
│   ├── sources.json   # ⭐ Cấu hình nguồn tin
│   └── types.ts       # Type definitions
│
├── src/              # Frontend (Web UI)
├── package.json
└── pnpm-lock.yaml
```

**Chú ý 2 thư mục quan trọng:**
- 📁 `server/sources/` - Viết code lấy tin
- 📄 `shared/sources.json` - Đăng ký nguồn tin

---

## 5️⃣ Kiểm Tra Hoạt Động

### **Chạy development server**

```powershell
# Build và chạy
pnpm dev
```

**Output mong đợi:**
```
> newsnow@1.0.0 dev
> turbo dev

• Running dev...
• server:dev: cache miss, executing...
• web:dev: cache miss, executing...

  VITE v5.0.0  ready in 1234 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: http://192.168.1.100:5173/
  
  Server running on http://localhost:3000
```

### **Test API**

Mở trình duyệt hoặc dùng `curl`:

```powershell
# Test API zhihu (nguồn có sẵn)
curl http://localhost:3000/api/s?id=zhihu
```

**Response mẫu:**
```json
{
  "status": "success",
  "items": [
    {
      "id": "12345",
      "title": "知乎热榜第一",
      "url": "https://www.zhihu.com/question/12345",
      "extra": {
        "icon": "..."
      }
    }
  ],
  "updatedTime": 1732699800000
}
```

✅ **Nếu thấy JSON response → Setup thành công!**

---

## 6️⃣ Hiểu Cách Hoạt Động

### **Flow lấy tin:**

```
Browser/TrendRadar
    ↓
GET /api/s?id=zhihu
    ↓
server/index.ts (Router)
    ↓
server/sources/zhihu.ts (Handler)
    ↓
Fetch data từ zhihu.com
    ↓
Parse & return JSON
    ↓
Browser/TrendRadar nhận data
```

### **Các file quan trọng:**

#### **1. `server/sources/zhihu.ts`** (Ví dụ)
```typescript
import type { NewsItem, SourceHandler } from "../types"

export const handler: SourceHandler = async () => {
  // 1. Fetch dữ liệu
  const response = await fetch("https://www.zhihu.com/api/...")
  const data = await response.json()
  
  // 2. Parse thành NewsItem[]
  const items: NewsItem[] = data.data.map(item => ({
    id: item.target.id.toString(),
    title: item.target.title,
    url: `https://www.zhihu.com/question/${item.target.id}`,
    extra: {
      icon: item.target.image_url
    }
  }))
  
  // 3. Return
  return items
}
```

#### **2. `shared/sources.json`**
```json
{
  "zhihu": {
    "name": "知乎",
    "type": "hottest",
    "column": "china",
    "home": "https://www.zhihu.com",
    "color": "blue",
    "interval": 600000
  }
}
```

**Giải thích:**
- `id`: zhihu (dùng trong API: `/api/s?id=zhihu`)
- `name`: Tên hiển thị
- `type`: `hottest` | `realtime`
- `column`: `china` | `tech` | `finance` | `world`
- `interval`: Thời gian cache (ms)

---

## 7️⃣ Test Thêm Nguồn Khác

```powershell
# Test weibo
curl http://localhost:3000/api/s?id=weibo

# Test hackernews
curl http://localhost:3000/api/s?id=hackernews

# Test github
curl http://localhost:3000/api/s?id=github
```

Tất cả đều phải trả về JSON với `status: "success"`.

---

## 8️⃣ Dừng Server

```powershell
# Nhấn Ctrl+C trong terminal
Ctrl+C
```

---

## ✅ Checklist Hoàn Thành

Đánh dấu khi hoàn thành:

- [ ] Cài Node.js ≥18.0.0
- [ ] Cài pnpm ≥8.0.0
- [ ] Fork newsnow trên GitHub
- [ ] Clone về `TrendRadar/newsnow/`
- [ ] Chạy `pnpm install` thành công
- [ ] Chạy `pnpm dev` không lỗi
- [ ] Test API `curl localhost:3000/api/s?id=zhihu` OK
- [ ] Hiểu flow lấy tin
- [ ] Hiểu cấu trúc `sources/` và `sources.json`

---

## 🐛 Troubleshooting

### **Lỗi: `pnpm: command not found`**
```powershell
# Cài lại pnpm
npm install -g pnpm

# Hoặc dùng corepack (Node.js ≥16.13)
corepack enable
corepack prepare pnpm@latest --activate
```

### **Lỗi: `Port 3000 already in use`**
```powershell
# Tìm process đang dùng port 3000
netstat -ano | findstr :3000

# Kill process (thay PID)
taskkill /PID <PID> /F
```

### **Lỗi: `pnpm install` failed**
```powershell
# Xóa node_modules và pnpm-lock.yaml
Remove-Item -Recurse -Force node_modules
Remove-Item pnpm-lock.yaml

# Cài lại
pnpm install
```

---

## 🎯 Bước Tiếp Theo

Sau khi setup xong, tiếp tục:

👉 **[Bước 2: Thêm Nguồn Tin VN](buoc-2-them-nguon-vn.md)**

---

**Thời gian hoàn thành**: ~30 phút  
**Độ khó**: ⭐⭐☆☆☆
