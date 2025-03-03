# 🏠 `home.html` – Trang chủ của Flask Blog

---

## ✅ Chức năng:
`home.html` là template đảm nhiệm việc hiển thị **trang chủ** của blog, nơi người dùng xem danh sách các bài viết (`posts`) từ cơ sở dữ liệu.

Template này:
- **Kế thừa** từ `layout.html` để sử dụng chung giao diện.
- Duyệt qua danh sách bài viết và hiển thị từng bài dưới dạng thẻ (`article`).
- Show hình đại diện tác giả, tên tác giả, ngày đăng, tiêu đề bài viết và nội dung.

---

## 🏗️ Cấu trúc:
| Thành phần | Chức năng |
|------------|-----------|
| `{% extends "layout.html" %}` | Kế thừa giao diện chung từ `layout.html`. |
| `{% block content %}` | Khối nội dung chính hiển thị danh sách các bài viết. |
| `{% for post in posts %}` | Lặp qua danh sách các bài viết lấy từ Flask backend. |
| `<article>` | Thẻ chứa từng bài viết, styled với Bootstrap. |

---

## 🔍 Chi tiết đặc biệt:
- **Hiển thị avatar tác giả:**  
  ```html
  <img class="rounded-circle article-img" src="{{ url_for('static', filename='profile_pics/' + post.author.image_file) }}">
  ```

- **Tác giả và ngày đăng:**  
  ```html
  <a class="mr-2" href="#">{{ post.author.username }}</a>
  <small class="text-muted">{{ post.date_posted.strftime('%Y-%m-%d') }}</small>
  ```

- **Tiêu đề bài viết:**  
  Có link đến chi tiết bài viết (`post/<post_id>`).
  ```html
  <h2><a class="article-title" href="{{ url_for('post', post_id=post.id) }}">{{ post.title }}</a></h2>
  ```

- **Nội dung bài viết:**  
  ```html
  <p class="article-content">{{ post.content }}</p>
  ```

---

## 🔐 Lưu ý cải thiện:
- [ ] **Pagination:** Hiện tại, nếu nhiều bài viết sẽ tải tất cả cùng lúc. Nên thêm phân trang (`paginate`) để tối ưu.
- [ ] **Link tác giả:** Thẻ `<a>` tên tác giả hiện để `href="#"`, có thể mở rộng để dẫn tới trang thông tin người dùng (profile).
  ```html
  <a href="{{ url_for('user_posts', username=post.author.username) }}">{{ post.author.username }}</a>
  ```
- [ ] **Giới hạn độ dài nội dung:** Nếu `post.content` dài, có thể cắt bớt với Jinja filter như:
  ```html
  {{ post.content[:150] }}...
  ```

---

## 💡 Gợi ý mở rộng:
- Thêm nút "Read More" dẫn đến chi tiết bài viết.
- Hiển thị số lượt xem hoặc lượt thích.
- Hỗ trợ markdown hoặc rich-text cho nội dung bài viết.
- Thêm hiệu ứng loading hoặc skeleton khi đang tải bài viết.