# 📝 `register.html` – Trang Đăng Ký Người Dùng  

---

## ✅ Chức năng:
- Cung cấp **form đăng ký** để người dùng tạo tài khoản.
- Bao gồm các trường: **username, email, password, confirm password**.
- Sau khi đăng ký thành công, người dùng có thể đăng nhập ngay.

---

## 🏗️ Cấu trúc chính:
| Thành phần | Chức năng |
|------------|-----------|
| `{% extends "layout.html" %}` | Kế thừa giao diện tổng thể của trang web. |
| **Form đăng ký** | Gồm 4 input: `username`, `email`, `password`, `confirm password`. |
| **Nút đăng ký** | Gửi form qua phương thức `POST` để xử lý đăng ký. |
| **Link đăng nhập** | Nếu đã có tài khoản, người dùng có thể chuyển đến trang login. |

---

## 🔍 Chi tiết nổi bật:
- **Dùng Flask-WTF để tạo form**:  
  ```jinja
  {{ form.hidden_tag() }}
  ```
  Giúp bảo vệ form khỏi các cuộc tấn công CSRF.

- **Các input có class Bootstrap** để giao diện đẹp hơn:  
  ```jinja
  {{ form.email(class = "form-control form-control-lg") }}
  ```

- **Tạo đường dẫn đến trang đăng nhập cho người dùng đã có tài khoản**:  
  ```jinja
  <a class="ml-2" href="{{ url_for('login') }}">Sign In</a>
  ```

- **Thiếu xử lý lỗi form**:  
  Không có kiểm tra lỗi khi nhập dữ liệu không hợp lệ, có thể thêm vào như sau:
  ```jinja
  {% if form.email.errors %}
      {{ form.email(class="form-control form-control-lg is-invalid") }}
      <div class="invalid-feedback">
          {% for error in form.email.errors %}
              <span>{{ error }}</span>
          {% endfor %}
      </div>
  {% else %}
      {{ form.email(class="form-control form-control-lg") }}
  {% endif %}
  ```

---

## 🚀 Cần cải thiện:
- [ ] **Thêm kiểm tra lỗi input** để hiển thị cảnh báo khi nhập sai.
- [ ] **Cải thiện UI/UX**: Dùng placeholder hoặc tooltip hướng dẫn người dùng.
- [ ] **Thêm reCAPTCHA** để tránh spam đăng ký.
- [ ] **Hỗ trợ đăng ký qua OAuth** (Google, GitHub).

---

## 💡 Gợi ý mở rộng:
- Gửi email xác nhận sau khi đăng ký.
- Thêm Avatar mặc định cho tài khoản mới.
- Hiển thị điều khoản sử dụng trước khi đăng ký.