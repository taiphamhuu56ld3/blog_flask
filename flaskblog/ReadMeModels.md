# 📌 `models.py` – Định nghĩa Database Models

File **`models.py`** chứa các **ORM models** (các bảng trong database) được sử dụng trong ứng dụng Flask. Các model này được tạo bằng SQLAlchemy và giúp tương tác với cơ sở dữ liệu dễ dàng hơn.

---

## ✅ Các thư viện chính được sử dụng

| Thư viện | Công dụng |
|----------|-----------|
| `datetime` | Xử lý ngày giờ. |
| `flask_login.UserMixin` | Hỗ trợ xác thực người dùng. |
| `flaskblog.db` | Thao tác với database bằng SQLAlchemy. |
| `flaskblog.login_manager` | Quản lý đăng nhập người dùng. |

---

## 📌 Chi tiết các model

### 1️⃣ `User`
Lớp đại diện cho **bảng người dùng** trong database.

#### 🔹 Các cột trong bảng:
| Cột | Loại dữ liệu | Ý nghĩa |
|-----|--------------|---------|
| `id` | `Integer (primary key)` | ID duy nhất của mỗi user. |
| `user_name` | `String (20)` | Tên đăng nhập (duy nhất, bắt buộc). |
| `email` | `String (120)` | Địa chỉ email (duy nhất, bắt buộc). |
| `image_file` | `String (20)` | Ảnh đại diện của user (mặc định: `default.jpg`). |
| `password` | `String (60)` | Mật khẩu đã được hash. |
| `posts` | `Relationship` | Liên kết với các bài viết của user. |

#### 🔹 Liên kết (Relationships):
- **Một User có thể có nhiều bài viết (`Post`)** nhờ vào thuộc tính:
  ```python
  posts = db.relationship('Post', backref='author', lazy=True)
  ```
  - `backref='author'`: Cho phép truy cập `user` từ `Post` (`post.author`).
  - `lazy=True`: Tải dữ liệu một cách tối ưu.

#### 🔹 Hàm đặc biệt:
```python
def __repr__(self):
    return f"User('{self.user_name}', '{self.email}', '{self.image_file}')"
```
- Trả về chuỗi đại diện cho object `User`.

---

### 2️⃣ `Post`
Lớp đại diện cho **bảng bài viết** trong database.

#### 🔹 Các cột trong bảng:
| Cột | Loại dữ liệu | Ý nghĩa |
|-----|--------------|---------|
| `id` | `Integer (primary key)` | ID duy nhất của mỗi bài viết. |
| `title` | `String (100)` | Tiêu đề bài viết. |
| `date_posted` | `DateTime` | Ngày đăng bài (mặc định là thời điểm hiện tại). |
| `content` | `Text` | Nội dung bài viết. |
| `user_id` | `Integer (Foreign Key)` | ID của user đã đăng bài. |

#### 🔹 Liên kết (Relationships):
- **Mỗi bài viết thuộc về một user** nhờ vào `user_id`:
  ```python
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  ```
  - `db.ForeignKey('user.id')`: Liên kết `Post` với `User`.

#### 🔹 Hàm đặc biệt:
```python
def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}')"
```
- Trả về chuỗi đại diện cho object `Post`.

---

## 🔑 Quản lý đăng nhập (`load_user` function)

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```
- Hàm này giúp Flask-Login **tải user từ database** dựa trên `user_id`.
- Flask-Login sử dụng hàm này để quản lý phiên đăng nhập.

---

## 🛠️ Cách sử dụng models
1. **Tạo database từ models** (chạy trong terminal Python):
   ```python
   from flaskblog import db, create_app
   app = create_app()
   with app.app_context():
       db.create_all()
   ```
2. **Thêm User mới vào database**:
   ```python
   user = User(user_name="tai", email="tai@example.com", password="hashed_password")
   db.session.add(user)
   db.session.commit()
   ```
3. **Thêm Post mới**:
   ```python
   post = Post(title="Hello World", content="Bài viết đầu tiên!", user_id=user.id)
   db.session.add(post)
   db.session.commit()
   ```

---

## 🔥 Kết luận
- `models.py` giúp định nghĩa cấu trúc database.
- Sử dụng SQLAlchemy để dễ dàng thao tác với database.
- Hỗ trợ đăng nhập bằng Flask-Login.

Bạn có thể mở rộng file này để thêm tính năng như:
- Mô hình **bình luận** (`Comment`).
- **Phân quyền người dùng** (`Admin`, `Editor`, `User`).
- **Lịch sử chỉnh sửa bài viết** (`PostHistory`).
