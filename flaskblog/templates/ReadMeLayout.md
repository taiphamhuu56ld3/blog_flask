# 📌 `layout.html` – Template cơ sở cho Flask Blog

---

## ✅ Chức năng:
`layout.html` là template nền tảng (base template) cho toàn bộ hệ thống giao diện trong Flask Blog. Template này dùng để:
- Định nghĩa bố cục chung cho các trang (`home`, `about`, `login`, `register`, `account`, `post`, ...).
- Giúp **kế thừa** dễ dàng thông qua Jinja2 (`{% extends "layout.html" %}`).
- Chứa các phần giao diện lặp lại như:
  - Navbar.
  - Footer (nếu có).
  - Load các file CSS/JS dùng chung.
  - Thông báo flash messages.
  - Phần hiển thị thông tin phụ bên phải (sidebar).

---

## 🏗️ Cấu trúc chính của file:
| Khu vực | Chức năng |
|---------|-----------|
| `<head>` | Load Bootstrap 4, CSS custom (`main.css`), và tiêu đề động (title). |
| `<header>` | Navbar với các link điều hướng (`Home`, `About`, `Create Post`, `Login`, `Logout`, ...) dựa vào trạng thái đăng nhập của người dùng (`current_user.is_authenticated`). |
| `<main>` | Chia layout thành 2 cột: <br> ➤ Cột trái (8/12): Nội dung chính của từng page (`{% block content %}`). <br> ➤ Cột phải (4/12): Sidebar chứa thông tin phụ (`Infor`, `Latest Posts`, ...). |
| Flash Messages | Hiển thị thông báo lỗi/thành công với `get_flashed_messages`. |
| Footer (nếu có) | Hiện tại chưa có, có thể mở rộng thêm ở cuối file. |
| JS Scripts | Load các thư viện JS của Bootstrap 4, jQuery và Popper.js. |

---

## 🔍 Chi tiết đặc biệt:
- **Title động:**  
  ```html
  {% if title %}
    <title>Tai's Blog - {{title}}</title>
  {% else %}
    <title>Tai's Blog</title>
  {% endif %}
  ```

- **Kiểm tra đăng nhập để đổi menu navbar:**  
  ```html
  {% if current_user.is_authenticated %}
    <a href="{{ url_for('account') }}">Account</a>
    <a href="{{ url_for('logout') }}">Logout</a>
  {% else %}
    <a href="{{ url_for('login') }}">Login</a>
    <a href="{{ url_for('register') }}">Register</a>
  {% endif %}
  ```

- **Flash message:**  
  Hiển thị thông báo từ Flask (ví dụ khi đăng nhập lỗi, tạo bài viết thành công):
  ```html
  {% for category, message in messages %}
    <div class="alert alert-{{ category }}">
      {{ message }}
    </div>
  {% endfor %}
  ```

---

## 🔐 Lưu ý cải thiện:
- [ ] ⚠️ **Bug nhỏ:** Flash messages bị lỗi khoảng trắng trong class.
  ```html
  <div class="alert alert -{{ category }}"> <!-- Sai -->
  <div class="alert alert-{{ category }}">   <!-- Đúng -->
  ```

- [ ] **Responsive:** Nên kiểm tra lại hiển thị trên mobile, nhất là Navbar.
- [ ] **Nâng cấp phiên bản Bootstrap:** Bootstrap 4 đã cũ, cân nhắc lên Bootstrap 5 hoặc TailwindCSS.
- [ ] **Footer:** Thêm một footer đơn giản để cung cấp thêm thông tin bản quyền hoặc liên hệ.

---

## 💡 Gợi ý mở rộng:
- Thêm dark mode cho giao diện.
- Tích hợp Google Analytics hoặc Meta tags để tối ưu SEO.
- Load thông tin **"Latest Posts"** trong sidebar tự động từ database thay vì cố định.
