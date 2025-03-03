# 📌 Flask Blog Project

Đây là project blog được xây dựng bằng **Flask**, áp dụng mô hình **Application Factory Pattern** giúp tổ chức code rõ ràng, dễ mở rộng và bảo trì.

---

## 🏗️ Cấu trúc Project
```
blog_flask/
│
├── app.py                  # Điểm khởi chạy chính của ứng dụng
├── flaskblog/
│   ├── __init__.py         # Khởi tạo Flask app với create_app()
│   ├── routes.py           # Khai báo các route xử lý request
│   ├── models.py           # Định nghĩa database models (User, Post, ...)
│   ├── forms.py            # Khai báo các form xử lý input
│   ├── templates/          # Chứa các file HTML (Jinja2 templates)
│   ├── static/             # Chứa CSS, hình ảnh,...
│   └── ...
├── venv/                   # Virtual environment
└── requirements.txt        # Danh sách thư viện cần cài đặt
```

---

## 🚀 Cách hoạt động của `app.py`

```python
from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

### ✅ Giải thích:
| Thành phần                          | Mô tả                                                         |
|--------------------------------------|---------------------------------------------------------------|
| `from flaskblog import create_app`  | Import hàm factory để tạo Flask app từ package `flaskblog`    |
| `create_app()`                      | Hàm factory khởi tạo và cấu hình toàn bộ app                  |
| `app = create_app()`                | Tạo instance Flask app để sử dụng                             |
| `if __name__ == '__main__'`         | Đảm bảo chạy app khi file được thực thi trực tiếp             |
| `app.run(debug=True)`               | Chạy server Flask với chế độ debug (tự động reload, log lỗi) |

---

## 🧰 Cài đặt môi trường

### 1️⃣ Tạo Python virtual environment:
```bash
sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Cài các thư viện cần thiết:
```bash
pip install Flask
pip install Flask-Bcrypt
pip install Pillow
```
> Hoặc cài nhanh qua `requirements.txt` nếu đã có:
```bash
pip install -r requirements.txt
```

---

## ⚡ Chạy project
Sau khi hoàn tất cài đặt, khởi chạy project bằng lệnh:
```bash
python app.py
```
> Mở trình duyệt và truy cập: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Ghi chú
- ✅ `debug=True`: Giúp tự động reload khi chỉnh sửa code và hiển thị chi tiết lỗi.
- ✅ Sử dụng **Application Factory Pattern** giúp dễ dàng mở rộng, tái sử dụng cấu hình, viết test, và quản lý các phần mở rộng (Flask extensions).
- ✅ Sau khi cài thêm thư viện mới, nhớ lưu lại danh sách bằng:
```bash
pip freeze > requirements.txt
```
- ✅ Nên kích hoạt lại virtual environment mỗi khi làm việc với project:
```bash
source venv/bin/activate
```

----------------------------------------------------------------------------------------------------------------
Các **công nghệ** được sử dụng trong dự án bao gồm:

---

## ✅ Công nghệ chính:
| Công nghệ              | Mô tả                                                             |
|------------------------|-------------------------------------------------------------------|
| **Python**            | Ngôn ngữ lập trình chính để xây dựng backend.                    |
| **Flask**             | Micro web framework để phát triển ứng dụng web.                  |
| **Flask-Bcrypt**      | Thư viện để mã hóa mật khẩu người dùng (bcrypt hashing).         |
| **Flask-WTF**         | Xử lý form HTML và validation qua WTForms.                       |
| **Flask-Login**       | Quản lý đăng nhập, phiên người dùng (session).                   |
| **Flask-SQLAlchemy**  | ORM để thao tác với cơ sở dữ liệu một cách dễ dàng.              |
| **Jinja2**            | Template engine để render HTML với dữ liệu động.                 |
| **Pillow (PIL)**      | Xử lý hình ảnh (resize, lưu avatar cho user).                    |

---

## ✅ Công nghệ giao diện (Frontend):
| Công nghệ              | Mô tả                                                           |
|------------------------|-----------------------------------------------------------------|
| **HTML5**             | Cấu trúc nội dung trang web.                                   |
| **CSS3**              | Tạo kiểu dáng giao diện trang web.                            |
| **Bootstrap 4**       | Framework CSS hỗ trợ responsive design và các thành phần UI. |
| **JavaScript (jQuery)**| Xử lý modal (popup), tương tác frontend nhỏ.                  |

---

## ✅ Khác:
| Công nghệ                | Mô tả                                      |
|--------------------------|--------------------------------------------|
| **SQLite/MySQL/PostgreSQL** (tùy chọn) | Cơ sở dữ liệu để lưu thông tin người dùng, bài viết, ... |
| **Virtualenv (venv)**   | Tạo môi trường ảo để quản lý thư viện Python. |

---

## 📌 Tổng kết lại:
🔹 **Backend:** Python, Flask, Flask-Bcrypt, Flask-WTF, Flask-Login, Flask-SQLAlchemy  
🔹 **Frontend:** HTML5, CSS3, Bootstrap 4, Jinja2, JavaScript (jQuery)  
🔹 **Khác:** Pillow, venv, SQLite (hoặc các DB khác)

---

Mô tả chi tiết **sơ đồ kiến trúc** của project và **luồng xử lý đăng nhập/đăng ký** trong Flask Blog:

---

# 🏗️ Sơ đồ kiến trúc tổng thể của Flask Blog

```
┌──────────────────────┐
│     Người dùng      │
└────────┬────────────┘
         │ Gửi request (HTTP)
         ▼
┌───────────────────────────┐
│        Flask App          │
│  (theo Application Factory│
│           Pattern)        │
└────────┬────────┬─────────┘
         │        │
         │        │
 ┌───────▼──────┐ └─────────────────────────┐
 │  Blueprints │                           │
 │ (routes.py) │                           │
 └──────┬──────┘                           │
        │                                  │
 ┌──────▼────────────┐       ┌─────────────▼──────────┐
 │ Forms (WTForms)  │       │    Models (SQLAlchemy) │
 │ - LoginForm      │       │ - User                │
 │ - RegisterForm   │       │ - Post                │
 └──────────────────┘       └──────────┬─────────────┘
                                       │
                          ┌────────────▼────────────┐
                          │     Database (SQLite)   │
                          └─────────────────────────┘

```

---

# 🔑 Luồng xử lý **Đăng ký (Register)**

### 1️⃣ Người dùng nhập thông tin vào form:
- `username`
- `email`
- `password`
- `confirm_password`

### 2️⃣ Gửi form lên server (`POST /register`)

### 3️⃣ Flask xử lý trong route `@app.route('/register')`
- Validate dữ liệu form.
- Kiểm tra email hoặc username đã tồn tại chưa.
- Băm mật khẩu bằng **Flask-Bcrypt**.
- Tạo user mới và lưu vào database.
  
```python
hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
user = User(username=form.username.data, email=form.email.data, password=hashed_password)
db.session.add(user)
db.session.commit()
```

### 4️⃣ Sau khi đăng ký thành công:
- Flash thông báo “Tạo tài khoản thành công!”
- Redirect về trang đăng nhập (`/login`).

---

# 🔒 Luồng xử lý **Đăng nhập (Login)**

### 1️⃣ Người dùng nhập thông tin vào form:
- `email`
- `password`
- `remember` (tuỳ chọn)

### 2️⃣ Gửi form lên server (`POST /login`)

### 3️⃣ Flask xử lý trong route `@app.route('/login')`
- Validate dữ liệu form.
- Tìm user theo email trong database.
- So sánh password nhập vào với password đã băm trong DB:
  
```python
user = User.query.filter_by(email=form.email.data).first()
if user and bcrypt.check_password_hash(user.password, form.password.data):
    login_user(user, remember=form.remember.data)
```

### 4️⃣ Nếu đúng:
- Login thành công bằng **Flask-Login**.
- Redirect về trang chủ hoặc trang được yêu cầu.

### 5️⃣ Nếu sai:
- Hiện thông báo lỗi: “Đăng nhập thất bại. Vui lòng kiểm tra email và mật khẩu.”

---

## ✅ Lưu ý:
- **Flask-WTF** xử lý việc validate form.
- **Flask-Bcrypt** mã hoá mật khẩu trước khi lưu vào database.
- **Flask-Login** quản lý session đăng nhập và kiểm tra trạng thái người dùng.

---

Sơ đồ **Sequence Diagram** (tuần tự) mô tả luồng xử lý đăng nhập trong project Flask Blog:

---

# 🔄 Sơ đồ Sequence – Đăng nhập (Login)

```
Người dùng         Trình duyệt            Flask App         Database (SQLite)
    │                  │                      │                     │
    │  Nhập email/pass │                      │                     │
    │─────────────────>│                      │                     │
    │                  │  Gửi POST /login     │                     │
    │                  │────────────────────> │                     │
    │                  │                      │  Tìm user theo email│
    │                  │                      │───────────────►     │
    │                  │                      │                     │
    │                  │                      │   Trả về thông tin user
    │                  │                      │◄────────────────────│
    │                  │                      │
    │                  │                      │  Kiểm tra password (bcrypt)
    │                  │                      │
    │                  │                      │  Nếu đúng → login_user()
    │                  │                      │
    │                  │   Trả về response    │
    │                  │<──────────────────── │
    │  Hiển thị thông báo và chuyển hướng     │
    │<─────────────────────────────────────── │
```

---

# 🔄 Sơ đồ Sequence – Đăng ký (Register)

```
Người dùng         Trình duyệt            Flask App         Database (SQLite)
    │                  │                      │                     │
    │ Nhập form đăng ký│                      │                     │
    │─────────────────>│                      │                     │
    │                  │  Gửi POST /register  │                     │
    │                  │────────────────────> │                     │
    │                  │                      │ Kiểm tra email tồn tại?
    │                  │                      │───────────────►     │
    │                  │                      │                     │
    │                  │                      │   Không tồn tại → OK
    │                  │                      │◄────────────────────│
    │                  │                      │ Băm password (bcrypt)
    │                  │                      │ Thêm user vào DB
    │                  │                      │───────────────►     │
    │                  │                      │                     │
    │                  │                      │  Commit dữ liệu     │
    │                  │                      │◄────────────────────│
    │                  │   Trả về response    │
    │                  │<──────────────────── │
    │  Hiển thị thông báo và chuyển hướng     │
    │<─────────────────────────────────────── │
```

---
