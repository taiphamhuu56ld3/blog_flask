# 📌 `site.db` – Database của Flask Blog

---

## ✅ Chức năng:
**`site.db`** là file **SQLite database** chính của ứng dụng Flask Blog. Nó lưu trữ tất cả dữ liệu liên quan đến hệ thống, bao gồm:
- Thông tin người dùng (Users).
- Các bài viết (Posts).
- Những mối quan hệ giữa người dùng và bài viết.

---

## 📂 Vị trí:
```
blog_flask/
├── instance/
│   └── site.db
```
> Thư mục `instance/` được Flask sử dụng để lưu trữ các dữ liệu riêng biệt và nhạy cảm (như database, file cấu hình riêng tư...), nhằm tách biệt khỏi mã nguồn chính.

---

## 🏗️ Cách tạo file `site.db`:
File `site.db` được tạo ra bằng cách chạy lệnh khởi tạo database từ file **`init_db.py`**:

```bash
python init_db.py
```
Lúc này, dựa trên cấu hình:
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
```
Flask-SQLAlchemy sẽ tạo database SQLite với tên **`site.db`** trong thư mục **`instance/`**.

---

## 🔍 Các bảng dữ liệu chính:
Dựa trên các model đã định nghĩa trong `models.py`, `site.db` sẽ có các bảng như:
| Bảng | Chức năng |
|------|-----------|
| `user` | Lưu thông tin tài khoản người dùng: username, email, password... |
| `post` | Lưu các bài viết (posts) của người dùng, liên kết với `user`. |

---

## 🔐 Lưu ý bảo mật:
- Không nên commit file `site.db` lên Git khi làm việc thực tế (sử dụng `.gitignore`).
- Nếu chứa dữ liệu thật (user, mật khẩu), hãy bảo vệ kỹ file này và cân nhắc sử dụng database bảo mật hơn như PostgreSQL hoặc MySQL.
- Với môi trường production, hãy đặt database ngoài thư mục project hoặc trên server riêng biệt.

---

## ♻️ Khi nào cần xóa `site.db`?
- Khi bạn thay đổi cấu trúc model (thêm/sửa/xóa field) và không dùng migration.
- Khi muốn làm mới dữ liệu hoàn toàn.

> ⚠️ **Cẩn thận:** Xóa `site.db` đồng nghĩa với việc mất hết dữ liệu hiện tại!

---

## 💡 Mở rộng:
- Dùng **Flask-Migrate** để quản lý thay đổi schema mà không phải xóa database.
- Thêm các seed script để tự động tạo dữ liệu mẫu sau khi khởi tạo.


-----------------------------------------------------------------------------------------------------------------------------------------------
---

# 🗂️ Database trong dự án Flask Blog

Dự án sử dụng **ORM SQLAlchemy** để quản lý cơ sở dữ liệu.  
Cơ sở dữ liệu có thể là **SQLite** (mặc định khi phát triển local), hoặc nâng cấp lên **MySQL/PostgreSQL** khi triển khai thực tế.

---

## ✅ Các bảng chính trong Database

Thông thường trong một Blog cơ bản như trên sẽ có ít nhất **2 bảng chính**:

---

### 1️⃣ `User` – Lưu thông tin người dùng
```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
```

#### Các cột:
| Tên cột    | Kiểu dữ liệu    | Ý nghĩa                        |
|------------|-----------------|--------------------------------|
| id        | Integer (PK)    | Khóa chính                    |
| username  | String (20)     | Tên đăng nhập, duy nhất        |
| email     | String (120)    | Email người dùng, duy nhất     |
| image_file| String (20)     | Ảnh đại diện của user         |
| password  | String (60)     | Mật khẩu đã được mã hóa       |
| posts     | Relationship    | Quan hệ 1-nhiều với bảng Post |

---

### 2️⃣ `Post` – Lưu thông tin các bài viết
```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

#### Các cột:
| Tên cột     | Kiểu dữ liệu   | Ý nghĩa                       |
|-------------|----------------|-------------------------------|
| id         | Integer (PK)   | Khóa chính                    |
| title      | String (100)   | Tiêu đề bài viết              |
| date_posted| DateTime       | Ngày đăng bài (mặc định thời gian hiện tại) |
| content    | Text           | Nội dung bài viết             |
| user_id    | Integer (FK)   | Khóa ngoại, liên kết với User |

---

## ✅ Mối quan hệ giữa các bảng

- **User (1) ⇄ (N) Post**  
  ➤ Một user có thể viết nhiều post.  
  ➤ Mỗi post chỉ thuộc về một user.

Sơ đồ đơn giản như sau:
```
User
 ├── id
 ├── username
 └── ...

Post
 ├── id
 ├── title
 ├── content
 ├── user_id (FK -> User.id)
 └── ...
```

---

## ✅ Cơ sở dữ liệu sử dụng

| Môi trường     | Database sử dụng         |
|----------------|--------------------------|
| Phát triển    | SQLite (`sqlite:///site.db`) |
| Triển khai    | MySQL, PostgreSQL (tuỳ chọn) |

---

## ✅ Các thao tác liên quan DB trong project:
- Tạo database từ ORM:
  ```bash
  from flaskblog import db
  db.create_all()
  ```
- Thêm user/post mới.
- Cập nhật, xóa dữ liệu.
- Query dữ liệu để hiển thị ra trang web (VD: bài viết, thông tin người dùng).

---

## ✅ Lưu ý:
- ORM SQLAlchemy giúp bạn làm việc với DB thông qua class Python thay vì SQL thuần.
- Dùng `Flask-Migrate` để dễ quản lý **migration** khi thay đổi DB (nếu muốn nâng cấp).

---
