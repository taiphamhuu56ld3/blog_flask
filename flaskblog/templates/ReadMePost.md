# 📝 `post.html` – Trang chi tiết bài viết

---

## ✅ Chức năng:
`post.html` hiển thị **nội dung chi tiết của một bài viết** cụ thể trong blog, đồng thời cung cấp các chức năng **chỉnh sửa (Update)** và **xoá (Delete)** nếu người xem là tác giả bài viết.

---

## 🏗️ Cấu trúc chính:
| Thành phần | Chức năng |
|------------|-----------|
| `{% extends "layout.html" %}` | Kế thừa giao diện tổng thể của website. |
| Ảnh đại diện tác giả | Lấy từ thư mục `static/profile_pics/`. |
| Thông tin metadata | Hiển thị tên tác giả và ngày đăng. |
| Nút Update/Delete | Chỉ hiển thị khi `current_user` là tác giả bài viết. |
| Modal xác nhận xoá | Popup xác nhận trước khi xoá bài viết. |
| Tiêu đề và nội dung bài viết | Hiển thị chi tiết của bài viết hiện tại. |

---

## 🔍 Chi tiết nổi bật:
- **Kiểm tra quyền hạn tác giả**:  
  Các nút Update và Delete chỉ hiện nếu tác giả bài viết trùng với người dùng đang đăng nhập:
  
  ```jinja
  {% if post.author == current_user %}
    <!-- Hiển thị nút Update và Delete -->
  {% endif %}
  ```

- **Modal xác nhận xoá bài viết**:  
  Khi nhấn nút Delete, modal Bootstrap bật lên để xác nhận thao tác trước khi gửi form `POST` tới route `delete_post`.

  ```html
  <form action="{{ url_for('delete_post', post_id=post.id) }}" method="POST">
      <input class="btn btn-danger" type="submit" value="Delete">
  </form>
  ```

- **Ngày đăng** được định dạng rõ ràng:
  
  ```jinja
  {{ post.date_posted.strftime('%Y-%m-%d') }}
  ```

- **Nội dung bài viết** hiển thị rõ ràng với tiêu đề lớn và nội dung đầy đủ.

---

## 🛠️ Cần cải thiện:
- [ ] Thêm xác thực CSRF cho form xoá bài viết.
- [ ] Thêm thông báo flash sau khi xoá thành công hoặc thất bại.
- [ ] Cải thiện UX modal bằng cách thêm mô tả cảnh báo rõ ràng về hành động xoá.
- [ ] Chuyển hướng thông minh sau khi xoá bài viết (về trang chủ hoặc trang bài viết của tác giả).

---

## 💡 Gợi ý mở rộng:
- Cho phép hiển thị bình luận ngay dưới bài viết.
- Thêm chức năng "Like" hoặc "Bookmark" bài viết.
- Hiển thị tag/chủ đề bài viết kèm theo.
- Thêm lịch sử chỉnh sửa bài viết nếu có cập nhật.
