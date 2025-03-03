# 📌 `config.py` – Cấu hình Flask Application

File **`config.py`** chịu trách nhiệm quản lý các biến cấu hình quan trọng cho toàn bộ ứng dụng Flask. Việc tập trung cấu hình vào một file giúp dễ bảo trì, dễ mở rộng và thuận tiện thay đổi giữa các môi trường như **development**, **testing**, hoặc **production**.

---

## ✅ Nội dung code

```python
import os

class Config:
    SECRET_KEY = "b2dd17eb994d430edbc07467c6805875"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    
    # Cấu hình gửi email
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
```

---

## 🧩 Giải thích các thành phần chính

| Biến cấu hình | Mô tả |
|---------------|-------|
| **`SECRET_KEY`** | Khóa bí mật để bảo vệ dữ liệu quan trọng như session, cookie và CSRF. ⚠️ Nên bảo mật bằng biến môi trường. |
| **`SQLALCHEMY_DATABASE_URI`** | Đường dẫn kết nối tới database. Ở đây dùng SQLite với file `site.db`. |
| **`MAIL_SERVER`** | Máy chủ SMTP dùng để gửi email (ở đây dùng Google Mail). |
| **`MAIL_PORT`** | Cổng SMTP (587 dành cho TLS). |
| **`MAIL_USE_TLS`** | Bật/Tắt chế độ mã hóa TLS khi gửi email. |
| **`MAIL_USERNAME`** | Tên đăng nhập email để gửi mail, lấy từ biến môi trường `EMAIL_USER`. |
| **`MAIL_PASSWORD`** | Mật khẩu email để gửi mail, lấy từ biến môi trường `EMAIL_PASS`. |

---

## ⚠️ Lưu ý bảo mật

❌ **KHÔNG NÊN** để lộ **`SECRET_KEY`**, tên tài khoản và mật khẩu email trực tiếp trong code.

✅ Cách làm an toàn hơn là sử dụng biến môi trường:

Ví dụ thêm vào file `.env`:
```
SECRET_KEY=your_secret_key_here
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
```

Sau đó sửa lại file `config.py`:
```python
SECRET_KEY = os.environ.get('SECRET_KEY')
```

Và sử dụng thư viện như [`python-dotenv`](https://pypi.org/project/python-dotenv/) để tự động load `.env`.

---

## 💡 Tại sao dùng class `Config`
- Giúp quản lý tập trung các giá trị cấu hình.
- Dễ kế thừa, mở rộng cho các môi trường khác nhau:
  
  ```python
  class DevelopmentConfig(Config):
      DEBUG = True
  ```

- Dễ import vào Flask app bằng:
  
  ```python
  app.config.from_object(Config)
  ```

---

## 🎯 Lợi ích
- Chuẩn hóa cấu hình.
- Dễ dàng bảo trì.
- Linh hoạt mở rộng môi trường làm việc.
- Đảm bảo tính bảo mật cao hơn khi dùng biến môi trường.