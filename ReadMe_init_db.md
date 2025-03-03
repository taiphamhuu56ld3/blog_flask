# 📌 `init_db.py` – Khởi tạo Database cho Flask Blog

---

## ✅ Chức năng chính:
File **`init_db.py`** dùng để **tạo database** và các bảng (tables) tương ứng từ các mô hình (`models.py`) đã định nghĩa trong ứng dụng Flask.

---

## 📜 Nội dung code:
```python
from flaskblog import db, app
from flaskblog.models import User

with app.app_context():
    db.create_all()
```

---

## 🔍 Giải thích:

| Thành phần | Công dụng |
|------------|-----------|
| `from flaskblog import db, app` | Import đối tượng database (`SQLAlchemy`) và app Flask đã cấu hình. |
| `from flaskblog.models import User` | Import các model để đảm bảo chúng được đăng ký với SQLAlchemy khi tạo bảng. |
| `with app.app_context():` | Tạo application context để thực thi các thao tác liên quan đến database. |
| `db.create_all()` | Tạo tất cả các bảng trong database dựa trên các model đã định nghĩa. |

---

## ⚠️ Lưu ý:
- Phải chạy file này **một lần duy nhất** để khởi tạo database.
- Nếu bạn đã thay đổi models, hãy cân nhắc xóa database cũ hoặc dùng công cụ migrate (ví dụ: Flask-Migrate).
- Database sẽ được tạo tại vị trí đã cấu hình trong `app.config['SQLALCHEMY_DATABASE_URI']`.

---

## 🚀 Cách sử dụng:
### Bước 1: Đảm bảo đã cấu hình database trong `__init__.py`
Ví dụ:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
```

### Bước 2: Chạy file để tạo database:
```bash
python init_db.py
```

### Kết quả:
- File database (`site.db`) được tạo tại thư mục gốc của project.
- Các bảng như `user`, `post` sẽ được tạo theo các model đã định nghĩa.

---

## 🛠️ Có thể mở rộng:
- Tích hợp **Flask-Migrate** để quản lý migration thay vì xóa database thủ công mỗi lần cập nhật model.
- Thêm dữ liệu mẫu (seed data) sau khi tạo bảng để tiện thử nghiệm.
