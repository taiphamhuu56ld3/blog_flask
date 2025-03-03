# 📌 `forms.py` – Xử lý Form trong Flask

File **`forms.py`** quản lý toàn bộ các biểu mẫu (form) được sử dụng trong ứng dụng Flask. Các form này dùng để xử lý việc đăng ký, đăng nhập, cập nhật tài khoản, và đăng bài viết.  
Nhờ sử dụng thư viện **WTForms** và **Flask-WTF**, việc xử lý form trở nên bảo mật, dễ dàng kèm theo các cơ chế xác thực dữ liệu đầu vào.

---

## ✅ Các thư viện chính được sử dụng

| Thư viện | Công dụng |
|----------|-----------|
| `FlaskForm` | Lớp cơ sở cho các form trong Flask. |
| `StringField`, `PasswordField`, `TextAreaField`, `SubmitField`, `FileField`, `BooleanField` | Các loại trường dữ liệu trên form. |
| `validators` | Xác thực dữ liệu nhập vào như kiểm tra độ dài, email hợp lệ, trùng mật khẩu,… |
| `FileAllowed` | Xác thực loại file được phép upload. |
| `current_user` | Lấy thông tin người dùng hiện tại từ phiên đăng nhập để kiểm tra dữ liệu. |

---

## 📝 Chi tiết các form

### 1️⃣ `RegistrationForm`
Form dùng cho việc **đăng ký tài khoản**.

#### Các trường:
| Trường | Loại dữ liệu | Ràng buộc |
|--------|--------------|-----------|
| `user_name` | StringField | Bắt buộc, từ 2-20 ký tự. |
| `email` | StringField | Bắt buộc, định dạng email. |
| `password` | PasswordField | Bắt buộc. |
| `confirm_password` | PasswordField | Bắt buộc, phải trùng với `password`. |
| `submit` | SubmitField | Nút gửi form. |

#### Kiểm tra đặc biệt:
- Kiểm tra **username** đã tồn tại chưa.
- Kiểm tra **email** đã tồn tại chưa.

---

### 2️⃣ `LoginForm`
Form dùng cho việc **đăng nhập**.

#### Các trường:
| Trường | Loại dữ liệu | Ràng buộc |
|--------|--------------|-----------|
| `email` | StringField | Bắt buộc, định dạng email. |
| `password` | PasswordField | Bắt buộc. |
| `remember` | BooleanField | Ghi nhớ đăng nhập. |
| `submit` | SubmitField | Nút gửi form. |

---

### 3️⃣ `UpdateAccountForm`
Form dùng để **cập nhật thông tin tài khoản**.

#### Các trường:
| Trường | Loại dữ liệu | Ràng buộc |
|--------|--------------|-----------|
| `username` | StringField | Bắt buộc, từ 2-20 ký tự. |
| `email` | StringField | Bắt buộc, định dạng email. |
| `picture` | FileField | Chỉ chấp nhận file `.jpg`, `.png`. |
| `submit` | SubmitField | Nút gửi form. |

#### Kiểm tra đặc biệt:
- Nếu đổi username, kiểm tra username mới đã tồn tại chưa.
- Nếu đổi email, kiểm tra email mới đã tồn tại chưa.

---

### 4️⃣ `PostForm`
Form dùng để **tạo bài viết**.

#### Các trường:
| Trường | Loại dữ liệu | Ràng buộc |
|--------|--------------|-----------|
| `title` | StringField | Bắt buộc. |
| `content` | TextAreaField | Bắt buộc. |
| `submit` | SubmitField | Nút gửi form. |

---

## 💡 Lợi ích khi dùng `Flask-WTF`
- Tự động bảo vệ CSRF.
- Tích hợp dễ dàng với Jinja2 để render form.
- Cung cấp các validator tiện dụng.
- Dễ dàng mở rộng và tái sử dụng các form.

---

## ⚠️ Lưu ý bảo mật
- Luôn sử dụng `SECRET_KEY` trong cấu hình Flask để bảo vệ CSRF.
- Các validator giúp tránh lỗi nhập liệu và các tấn công cơ bản như SQL Injection.