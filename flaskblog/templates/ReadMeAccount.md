# 👤 `account.html` – Trang cập nhật thông tin tài khoản

---

## ✅ Chức năng:
`account.html` là template phục vụ cho việc **xem và chỉnh sửa thông tin tài khoản người dùng**.  
Tại đây, người dùng có thể:
- Xem avatar, tên tài khoản, email.
- Thay đổi tên tài khoản (`username`) và email.
- Cập nhật hình đại diện mới.
- Submit form để lưu thông tin chỉnh sửa.

---

## 🏗️ Cấu trúc chính:
| Thành phần | Chức năng |
|------------|-----------|
| `{% extends "layout.html" %}` | Kế thừa giao diện từ layout chính. |
| Avatar (`image_file`) | Hiển thị ảnh đại diện hiện tại của user. |
| `current_user.username` và `current_user.email` | Thông tin hiện tại của tài khoản. |
| Form `POST` + `multipart/form-data` | Gửi dữ liệu form bao gồm file ảnh lên server. |
| `form.hidden_tag()` | CSRF token bảo vệ form. |
| Các input | Sử dụng Flask-WTF forms với field: `username`, `email`, `picture`. |
| Hiển thị lỗi | Nếu có lỗi validate từ backend thì sẽ render ngay dưới mỗi input. |
| Submit button | Nút cập nhật thông tin. |

---

## 🔍 Chi tiết nổi bật:
- **Avatar hiện tại**:
  ```html
  <img class="rounded-circle account-img" src="{{ image_file }}">
  ```

- **Form xử lý lỗi validation**:
  - Nếu có lỗi, input sẽ có class `is-invalid`.
  - Hiển thị lỗi chi tiết bên dưới từng field.
  ```html
  {% if form.username.errors %}
      {{ form.username(class="form-control form-control-lg is-invalid") }}
      <div class="invalid-feedback">
          {% for error in form.username.errors %}
              <span>{{ error }}</span>
          {% endfor %}
      </div>
  {% endif %}
  ```

- **Upload ảnh đại diện**:
  ```html
  {{ form.picture.label() }}
  {{ form.picture(class="form-control-file") }}
  ```

---

## 🔐 Lưu ý cải thiện:
- [ ] **Preview ảnh trước khi upload**: Hiện tại không có preview ảnh mới chọn. Có thể dùng JavaScript thêm tính năng xem trước ảnh trước khi submit.
- [ ] **Giới hạn dung lượng và định dạng ảnh** ở backend để tránh upload file không hợp lệ.
- [ ] **Thông báo thành công/ thất bại** sau khi cập nhật bằng `flash()` và hiển thị ở giao diện.

---

## 💡 Gợi ý mở rộng:
- Thêm mục "Đổi mật khẩu".
- Thêm liên kết quay về trang cá nhân của người dùng.
- Cho phép thêm mô tả ngắn về bản thân (bio).
- Cập nhật avatar bằng cách kéo thả (drag & drop).
