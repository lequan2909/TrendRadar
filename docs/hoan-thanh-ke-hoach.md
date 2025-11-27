# 🎯 Hoàn Thành Kế Hoạch - Build Nguồn Tin VN

## ✅ Checklist Tổng Thể

### **Phase 0: Chuẩn Bị** (10 phút)
- [ ] Cài Node.js ≥18.0.0
- [ ] Cài pnpm ≥8.0.0  
- [ ] Cài Python ≥3.10
- [ ] Cài Git
- [ ] Tạo Telegram Bot (lưu token & chat ID)

### **Phase 1: Setup TrendRadar** (15 phút)
- [ ] Tạo Python virtual environment
- [ ] Cài dependencies Python
- [ ] Test chạy TrendRadar với nguồn cũ
- [ ] Cấu hình Telegram

### **Phase 2: Setup Newsnow** (30 phút)
- [ ] Fork newsnow trên GitHub
- [ ] Clone về thư mục `TrendRadar/newsnow/`
- [ ] Cài dependencies: `pnpm install`
- [ ] Test chạy: `pnpm dev`
- [ ] Test API: `curl localhost:3000/api/s?id=zhihu`

### **Phase 3: Thêm Nguồn VN** (2 giờ)
- [ ] Cài `fast-xml-parser`
- [ ] Tạo `server/sources/vnexpress.ts`
- [ ] Tạo `server/sources/tuoitre.ts`
- [ ] Tạo `server/sources/dantri.ts`
- [ ] Sửa `shared/sources.json` (thêm 3 nguồn)
- [ ] Sửa `shared/types.ts` (thêm "vietnam")
- [ ] Test 3 API nguồn VN

### **Phase 4: Kết Nối & Test** (30 phút)
- [ ] Sửa `main.py` (dùng localhost:3000)
- [ ] Sửa `config/config.yaml` (3 nguồn VN)
- [ ] Tạo `config/frequency_words.txt`
- [ ] Tạo file `.env` từ `.env.example`
- [ ] Chạy cả 2: newsnow + TrendRadar
- [ ] Nhận tin VN qua Telegram ✅

---

## 📋 Hướng Dẫn Chi Tiết

### **🐍 Phase 1: Setup Python Virtual Environment**

#### **Bước 1.1: Tạo venv tự động**

```powershell
# Chạy script setup (đã tạo sẵn)
.\setup-venv.bat
```

Script này sẽ:
1. ✅ Kiểm tra Python
2. ✅ Tạo virtual environment (`venv/`)
3. ✅ Kích hoạt venv
4. ✅ Nâng cấp pip
5. ✅ Cài đặt dependencies từ `requirements.txt`

#### **Bước 1.2: Kích hoạt venv thủ công (nếu cần)**

```powershell
# Kích hoạt
venv\Scripts\activate

# Kiểm tra
python --version
pip list

# Thoát
deactivate
```

#### **Bước 1.3: Cài thêm package (nếu cần)**

```powershell
# Kích hoạt venv
venv\Scripts\activate

# Cài package
pip install <package_name>

# Cập nhật requirements.txt
pip freeze > requirements.txt
```

#### **Bước 1.4: Test TrendRadar**

```powershell
# Cách 1: Dùng script (khuyến nghị)
.\run.bat

# Cách 2: Thủ công
venv\Scripts\activate
python main.py
```

---

### **⚙️ Phase 2-4: Làm theo tài liệu**

Sau khi setup venv xong, làm theo các bước trong docs:

1. **Setup Newsnow**: [`docs/buoc-1-setup-newsnow.md`](docs/buoc-1-setup-newsnow.md)
2. **Thêm Nguồn VN**: [`docs/buoc-2-them-nguon-vn.md`](docs/buoc-2-them-nguon-vn.md)
3. **Test Local**: [`docs/buoc-3-test-local.md`](docs/buoc-3-test-local.md)

---

## 🎬 Workflow Hàng Ngày

### **Lần đầu chạy trong ngày**

```powershell
# Terminal 1: Chạy Newsnow
cd C:\Users\trung\TrendRadar\newsnow
pnpm dev

# Terminal 2: Chạy TrendRadar (với venv)
cd C:\Users\trung\TrendRadar
.\run.bat
```

### **Đã chạy, muốn chạy lại**

```powershell
# TrendRadar
.\run.bat

# Hoặc thủ công
venv\Scripts\activate
python main.py
```

---

## 📂 Cấu Trúc Thư Mục Cuối Cùng

```
TrendRadar/
├── venv/                          ✅ Virtual environment
│   ├── Scripts/
│   │   ├── activate.bat          ✅ Kích hoạt venv
│   │   ├── deactivate.bat        ✅ Thoát venv
│   │   ├── python.exe            ✅ Python trong venv
│   │   └── pip.exe               ✅ pip trong venv
│   └── Lib/                      ✅ Packages
│
├── newsnow/                      ✅ Dự án newsnow
│   ├── server/sources/
│   │   ├── vnexpress.ts         ✅ 
│   │   ├── tuoitre.ts           ✅
│   │   └── dantri.ts            ✅
│   └── shared/
│       ├── sources.json         ✅
│       └── types.ts             ✅
│
├── config/
│   ├── config.yaml              ✅
│   └── frequency_words.txt      ✅
│
├── docs/                        ✅ Tài liệu
│   ├── README.md
│   ├── QUICKSTART.md
│   ├── plan-build-nguon-tin-vn.md
│   ├── buoc-1-setup-newsnow.md
│   ├── buoc-2-them-nguon-vn.md
│   ├── buoc-3-test-local.md
│   └── hoan-thanh-ke-hoach.md  ← File này
│
├── setup-venv.bat               ✅ Script setup venv
├── run.bat                      ✅ Script chạy nhanh
├── .env                         ✅ Biến môi trường
├── .env.example                 ✅ Mẫu .env
├── requirements.txt             ✅ Dependencies
├── main.py                      ✅ (đã sửa)
└── README-VI.md                 ✅
```

---

## 🔧 Scripts Tiện Ích

### **setup-venv.bat** 
Tạo virtual environment và cài dependencies một lần.

```powershell
.\setup-venv.bat
```

### **run.bat**
Chạy TrendRadar với venv đã kích hoạt.

```powershell
.\run.bat
```

---

## 🐛 Troubleshooting

### **Lỗi: `venv\Scripts\activate.bat` không hoạt động**

```powershell
# Chạy PowerShell as Administrator
Set-ExecutionPolicy RemoteSigned

# Hoặc dùng cmd thay vì PowerShell
cmd
venv\Scripts\activate.bat
```

### **Lỗi: Package không tìm thấy sau khi cài**

```powershell
# Kiểm tra đang dùng Python nào
where python

# Phải thấy path venv:
# C:\Users\trung\TrendRadar\venv\Scripts\python.exe

# Nếu không, chưa activate venv
venv\Scripts\activate
```

### **Lỗi: `python-dotenv` không load .env**

Thêm vào đầu `main.py`:

```python
# Thêm import ở đầu file
from dotenv import load_dotenv

# Thêm sau import, trước CONFIG = load_config()
load_dotenv()  # Load biến từ .env file
```

### **Muốn xóa venv và tạo lại**

```powershell
# Xóa thư mục venv
rmdir /s /q venv

# Chạy lại setup
.\setup-venv.bat
```

---

## ✅ Kiểm Tra Hoàn Thành

### **Checklist Cuối Cùng**

#### **Python & venv**
- [ ] `venv/` được tạo
- [ ] `venv\Scripts\activate.bat` chạy OK
- [ ] `pip list` hiển thị: requests, pytz, PyYAML, python-dotenv
- [ ] `.\run.bat` chạy TrendRadar thành công

#### **Newsnow**
- [ ] `newsnow/` được clone
- [ ] `pnpm dev` chạy OK
- [ ] `curl localhost:3000/api/s?id=vnexpress` trả về JSON
- [ ] `curl localhost:3000/api/s?id=tuoitre` trả về JSON
- [ ] `curl localhost:3000/api/s?id=dantri` trả về JSON

#### **TrendRadar**
- [ ] File `.env` có Telegram token
- [ ] `main.py` dùng `localhost:3000`
- [ ] `config.yaml` có 3 nguồn VN
- [ ] `frequency_words.txt` có từ khóa VN
- [ ] Chạy `.\run.bat` không lỗi

#### **Kết Quả**
- [ ] Telegram nhận tin từ VnExpress ✅
- [ ] Telegram nhận tin từ Tuổi Trẻ ✅
- [ ] Telegram nhận tin từ Dân Trí ✅

---

## 🎉 Hoàn Thành!

Chúc mừng! Bạn đã:
- ✅ Setup Python virtual environment
- ✅ Fork và mở rộng newsnow
- ✅ Thêm 3 nguồn tin Việt Nam
- ✅ Kết nối TrendRadar với newsnow
- ✅ Nhận tin VN qua Telegram tự động

---

## 🚀 Bước Tiếp Theo

### **1. Tối Ưu Từ Khóa**
Chỉnh sửa `config/frequency_words.txt` để lọc tin chính xác hơn.

### **2. Thêm Nguồn Mới**
- Thanh Niên: https://thanhnien.vn/rss/home.rss
- Zing News: https://zingnews.vn/rss
- VOV: https://vov.vn/rss/...

### **3. Deploy Production**
- Deploy newsnow lên Cloudflare Pages
- Sửa TrendRadar dùng URL production
- Setup GitHub Actions

### **4. Monitoring**
- Theo dõi log
- Kiểm tra tin nhận được
- Tinh chỉnh interval, từ khóa

---

## 📚 Tài Liệu Tham Khảo

- [README Chính](docs/README.md)
- [Quick Start](docs/QUICKSTART.md)
- [Kế Hoạch Tổng Quan](docs/plan-build-nguon-tin-vn.md)
- [Bước 1: Setup Newsnow](docs/buoc-1-setup-newsnow.md)
- [Bước 2: Thêm Nguồn VN](docs/buoc-2-them-nguon-vn.md)
- [Bước 3: Test Local](docs/buoc-3-test-local.md)

---

**Cập nhật**: 2025-11-27  
**Thời gian hoàn thành**: ~3.5 giờ  
**Độ khó**: ⭐⭐⭐☆☆

**Chúc bạn thành công! 🎉**
