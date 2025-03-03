# 📌 `routes.py` – Định nghĩa các tuyến đường (Routes) của ứng dụng

File **`routes.py`** chứa các route xử lý logic chính của ứng dụng Flask blog, bao gồm: hiển thị bài viết, xử lý đăng ký, đăng nhập, cập nhật tài khoản, CRUD bài viết và đăng nhập bằng GitHub OAuth.

---

## ✅ Các thư viện chính được sử dụng

| Thư viện | Công dụng |
|----------|-----------|
| `flask` | Render template, xử lý request, flash message, abort, redirect. |
| `flask_login` | Quản lý đăng nhập, đăng xuất, xác thực người dùng. |
| `flask_dance.contrib.github` | OAuth đăng nhập bằng GitHub. |
| `werkzeug.utils` | Redirect URL. |
| `PIL.Image` | Xử lý ảnh đại diện người dùng. |
| `secrets` | Sinh chuỗi ngẫu nhiên bảo mật cho tên file ảnh. |
| `os` | Thao tác với hệ thống tệp tin (lưu ảnh). |

---

## 📌 Các route chính

### 🔹 Trang chính
```python
@app.route("/")
@app.route("/home")
```
- Hiển thị tất cả các bài viết từ database.

---

### 🔹 Trang About
```python
@app.route("/about")
```
- Hiển thị trang giới thiệu đơn giản.

---

### 🔹 Đăng ký tài khoản
```python
@app.route("/register", methods=["POST", "GET"])
```
- Xử lý form đăng ký tài khoản mới.
- Mật khẩu được hash bằng `bcrypt`.
- Nếu thành công, chuyển hướng sang trang đăng nhập.

---

### 🔹 Đăng nhập
```python
@app.route("/login", methods=["POST", "GET"])
```
- Kiểm tra email và mật khẩu.
- Nếu đúng, đăng nhập người dùng và điều hướng đến trang trước đó (nếu có) hoặc trang chủ.

---

### 🔹 Đăng xuất
```python
@app.route("/logout")
```
- Đăng xuất người dùng hiện tại và quay về trang chủ.

---

### 🔹 Thông tin tài khoản
```python
@app.route("/account", methods=["GET", "POST"])
@login_required
```
- Cập nhật thông tin tài khoản (username, email, ảnh đại diện).
- Ảnh đại diện sẽ được xử lý và lưu vào thư mục `static/profile_pics/`.

#### 💡 Hàm hỗ trợ:
```python
def save_picture(form_picture)
```
- Sinh tên file ngẫu nhiên cho ảnh.
- Resize ảnh về kích thước nhỏ (125x125) để tối ưu dung lượng.

---

### 🔹 Tạo bài viết mới
```python
@app.route("/post/new", methods=['GET', 'POST'])
@login_required
```
- Cho phép người dùng tạo bài viết mới sau khi đăng nhập.
- Lưu bài viết vào database với thông tin người viết là `current_user`.

---

### 🔹 Xem chi tiết bài viết
```python
@app.route("/post/<int:post_id>")
```
- Lấy thông tin bài viết từ `post_id` và hiển thị.

---

### 🔹 Cập nhật bài viết
```python
@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
```
- Kiểm tra quyền sở hữu bài viết.
- Nếu hợp lệ, cập nhật tiêu đề và nội dung bài viết.

---

### 🔹 Xóa bài viết
```python
@app.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
@login_required
```
- Kiểm tra quyền sở hữu bài viết.
- Nếu hợp lệ, xóa bài viết khỏi database.

---

### 🔹 Đăng nhập bằng GitHub
```python
@app.route("/gitlogin")
```
- Sử dụng OAuth qua `flask_dance` để đăng nhập bằng tài khoản GitHub.
- Nếu chưa cấp quyền, điều hướng đến trang đăng nhập GitHub.
- Sau khi đăng nhập thành công, lấy thông tin user từ GitHub API.

---

## 📝 Lưu ý đặc biệt
- Các route như `/account`, `/post/new`, `/post/<id>/update`, `/post/<id>/delete` đều yêu cầu người dùng phải đăng nhập (`@login_required`).
- Hàm `abort(403)` được sử dụng để từ chối truy cập khi user không có quyền thao tác.
- `flash()` được dùng để hiển thị thông báo (success, danger) sau các hành động như đăng nhập, đăng ký, cập nhật, xóa, v.v.
- Ảnh đại diện người dùng được xử lý cẩn thận để tránh trùng tên và đảm bảo ảnh có kích thước nhỏ gọn.

---

## 🛠️ Có thể mở rộng thêm:
- Pagination (phân trang) cho danh sách bài viết.
- Chức năng bình luận cho bài viết.
- Tính năng tìm kiếm bài viết.
- Phân quyền nâng cao (Admin, Editor...).
- Thông báo real-time qua WebSocket.
