Dưới đây là nội dung `README.md` dành riêng cho file **`blog_flask/flaskblog/__init__.py`**, trình bày rõ chức năng và các thành phần chính của file:

---

# 📌 `__init__.py` – Khởi tạo Flask Application

File **`__init__.py`** trong thư mục `flaskblog` chịu trách nhiệm khởi tạo và cấu hình toàn bộ Flask app theo mô hình **Application Factory Pattern**.

---

## 🏗️ Chức năng chính

- Khởi tạo app Flask.
- Cấu hình app từ class `Config`.
- Khởi tạo các extension:
  - **SQLAlchemy** – quản lý database.
  - **Bcrypt** – mã hóa mật khẩu.
  - **LoginManager** – quản lý đăng nhập.
  - **Mail** – gửi email.
- Tích hợp OAuth qua GitHub với **Flask-Dance**.
- Import các route từ file `routes.py`.

---

## ✅ Nội dung code

```python
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_dance.contrib.github import make_github_blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from flaskblog.config import Config

# Khởi tạo các extension (chưa gắn vào app)
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    
    # Load cấu hình từ class Config
    app.config.from_object(config_class)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Khởi động các extension với app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    # Import routes
    from flaskblog import routes
    
    # OAuth - Đăng nhập GitHub
    blueprint = make_github_blueprint(
        client_id="Ov23liCBryBDxvtnwTqH",
        client_secret="0f23236da39e20bd27b6669d12c4808d75b44c7f",
    )
    app.register_blueprint(blueprint, url_prefix="/login")
    
    return app
```

---

## 🧩 Các thành phần quan trọng

| Thành phần | Chức năng |
|------------|-----------|
| **`SQLAlchemy()`** | ORM để quản lý database |
| **`Bcrypt()`** | Mã hóa password |
| **`LoginManager()`** | Quản lý phiên đăng nhập |
| **`Mail()`** | Gửi email (ví dụ quên mật khẩu) |
| **`make_github_blueprint()`** | Tích hợp OAuth để đăng nhập qua GitHub |
| **`Config`** | Chứa các thiết lập cấu hình cho app |

---

## 🔐 Lưu ý bảo mật
⚠️ **CẢNH BÁO:** Không nên để lộ **`client_id`** và **`client_secret`** như trên. Hãy dùng biến môi trường để bảo vệ thông tin này:

```python
import os
client_id = os.environ.get('GITHUB_CLIENT_ID')
client_secret = os.environ.get('GITHUB_CLIENT_SECRET')
```

Và set biến môi trường trong hệ thống hoặc `.env` file.

---

## 🎯 Lợi ích khi dùng Application Factory
- Dễ dàng mở rộng app.
- Tách biệt cấu hình, extension, route.
- Dễ dàng viết test.
- Phù hợp với app lớn và nhiều môi trường (development, production).

---

## 💡 Tham khảo thêm
- [Flask Application Factories](https://flask.palletsprojects.com/en/latest/patterns/appfactories/)
- [Flask-Dance OAuth with GitHub](https://flask-dance.readthedocs.io/en/latest/)

---

Nếu muốn mình viết thêm ví dụ `.env` mẫu hoặc file `config.py`, cứ nhắn mình nha 😄