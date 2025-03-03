# 📝 `create_post.html` – Trang tạo/chỉnh sửa bài viết

---

## ✅ Chức năng:
`create_post.html` là template dùng để **tạo mới hoặc chỉnh sửa bài viết** trên blog.  
Form trong trang cho phép người dùng nhập:
- Tiêu đề bài viết (`title`).
- Nội dung bài viết (`content`).
- Gửi form để lưu bài viết lên database.

---

## 🏗️ Cấu trúc chính:
| Thành phần | Chức năng |
|------------|-----------|
| `{% extends "layout.html" %}` | Kế thừa giao diện chung từ layout chính. |
| `{{ name }}` | Hiển thị tiêu đề của form (ví dụ: "New Post" hoặc "Update Post"). |
| Form `POST` | Gửi dữ liệu bài viết lên server để xử lý. |
| `form.hidden_tag()` | Tự động chèn CSRF token bảo vệ form. |
| Các input | Dùng Flask-WTF để render field: `title`, `content`. |
| Hiển thị lỗi | Nếu có lỗi validate từ backend, thông báo sẽ hiển thị dưới từng trường. |
| Submit button | Gửi form để lưu bài viết. |

---

## 🔍 Chi tiết nổi bật:
- **Tiêu đề động của form**:
  ```html
  <legend class="border-bottom mb-4">{{ name }}</legend>
  ```

- **Form xử lý lỗi validation**:
  - Nếu field bị lỗi, thêm class `is-invalid`.
  - Lỗi hiển thị chi tiết ngay bên dưới input.
  ```html
  {% if form.title.errors %}
      {{ form.title(class="form-control form-control-lg is-invalid") }}
      <div class="invalid-feedback">
          {% for error in form.title.errors %}
              <span>{{ error }}</span>
          {% endfor %}
      </div>
  {% endif %}
  ```

- **Gợi ý đăng ký tài khoản nếu chưa có**:
  ```html
  <small class="text-muted">
      Need An Account? <a class="ml-2" href="{{ url_for('register') }}">Sign Up Now</a>
  </small>
  ```

---

## 🔐 Lưu ý cải thiện:
- [ ] Thêm xác nhận khi người dùng thoát trang nếu nội dung chưa lưu (`onbeforeunload` JS).
- [ ] Giới hạn độ dài tiêu đề và nội dung phía backend lẫn frontend.
- [ ] Hiển thị thông báo thành công sau khi đăng bài bằng `flash()`.

---

## 💡 Gợi ý mở rộng:
- Thêm hỗ trợ **Markdown** cho phần `content`.
- Cho phép upload ảnh đính kèm vào bài viết.
- Thêm **auto-save** bản nháp định kỳ.
- Thêm editor WYSIWYG như **QuillJS**, **TinyMCE**, hoặc **CKEditor** để soạn thảo trực quan.
