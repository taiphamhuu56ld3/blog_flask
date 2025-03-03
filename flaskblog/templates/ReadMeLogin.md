# 🔐 `login.html` – Trang đăng nhập người dùng

---

## ✅ Chức năng:
`login.html` là template phục vụ cho việc **đăng nhập người dùng** vào hệ thống blog.  
Trang này bao gồm form để:
- Nhập email.
- Nhập mật khẩu.
- Ghi nhớ đăng nhập (Remember me).
- Gửi form để xác thực tài khoản.

---

## 🏗️ Cấu trúc chính:
| Thành phần | Chức năng |
|------------|-----------|
| `{% extends "layout.html" %}` | Kế thừa giao diện tổng thể của website. |
| Form `POST` | Gửi dữ liệu xác thực (email, password) lên server. |
| `form.hidden_tag()` | Chèn CSRF token tự động. |
| Các input | Render bởi Flask-WTF cho `email`, `password`, `remember`. |
| Hiển thị lỗi | Nếu form có lỗi validate, thông báo sẽ hiển thị cạnh trường lỗi. |
| Submit button | Nút gửi form đăng nhập. |

---

## 🔍 Chi tiết nổi bật:
- **Hiển thị lỗi validate**:
  Nếu có lỗi ở các trường email hoặc password, trang sẽ hiện lỗi cụ thể ngay dưới input tương ứng với class `is-invalid`.
  
  ```html
  {% if form.email.errors %}
      {{ form.email(class="form-control form-control-lg is-invalid") }}
      <div class="invalid-feedback">
          {% for error in form.email.errors %}
              <span>{{ error }}</span>
          {% endfor %}
      </div>
  {% endif %}
  ```

- **Remember Me**:
  Cho phép người dùng chọn duy trì trạng thái đăng nhập.
  
  ```html
  <div class="form-check">
      {{ form.remember(class="form-check-input") }}
      {{ form.remember.label(class="form-check-label") }}
  </div>
  ```

- **Tùy chọn khác**:
  - Quên mật khẩu (`Forgot Password?`) – placeholder chưa xử lý.
  - Link đăng ký tài khoản nếu chưa có.
  - Đăng nhập thông qua GitHub (OAuth):
    ```html
    Log in with github <a class="ml-2" href="{{ url_for('gitlogin') }}">Log In Now</a>
    ```

---

## 🔐 Lưu ý cải thiện:
- [ ] Kết nối link "Forgot Password?" đến route xử lý quên mật khẩu.
- [ ] Bổ sung reCAPTCHA chống bot spam login.
- [ ] Thêm thông báo flash cho đăng nhập thất bại.
- [ ] Đăng nhập OAuth cần xử lý callback thành công/thất bại rõ ràng.

---

## 💡 Gợi ý mở rộng:
- Hỗ trợ thêm các hình thức đăng nhập khác như Google, Facebook, Zalo.
- Thêm hiển thị số lần đăng nhập sai liên tiếp và cảnh báo người dùng.
- Cho phép chuyển hướng sau khi đăng nhập về trang trước đó thay vì mặc định về home.
