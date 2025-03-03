# 🎨 `main.css` – Giao diện chính của Flask Blog  

---

## ✅ Chức năng:
`main.css` định nghĩa **style tổng thể** cho trang web Flask Blog, đảm bảo tính thẩm mỹ, dễ đọc, và nhất quán trong toàn bộ giao diện.

---

## 🏗️ Cấu trúc chính:

| Thành phần | Mục đích |
|------------|----------|
| **body** | Thiết lập màu nền, màu chữ, khoảng cách từ top để tránh đè lên navbar. |
| **h1, h2, h3** | Đồng bộ màu tiêu đề trang. |
| `.bg-steel` | Tô màu nền cho các khu vực như navbar. |
| `.site-header .navbar-nav .nav-link` | Tạo màu chữ và hiệu ứng hover cho các liên kết trên navbar. |
| `.content-section` | Style cho phần nội dung chính với padding, border, bo góc. |
| `.article-title` | Style tiêu đề bài viết và hiệu ứng hover chuyển màu. |
| `.article-content` | Giữ định dạng xuống dòng của bài viết bằng `white-space: pre-line`. |
| `.article-img` | Avatar nhỏ của tác giả bài viết (65x65px). |
| `.account-img` | Avatar lớn hơn trong trang cá nhân (125x125px). |
| `.account-heading` | Phóng to tiêu đề tên tài khoản. |

---

## 🔍 Một số chi tiết nổi bật:
- **Màu nền dịu nhẹ**:  
  ```css
  background: #fafafa;
  ```

- **Tông màu chủ đạo**:  
  Xanh thép (`#5f788a`) làm nổi bật navbar, kết hợp chữ xám trắng (`#cbd5db`) để tạo độ tương phản tốt.

- **Hover navbar**:  
  Chuyển từ xám nhạt sang trắng khi rê chuột để làm nổi bật lựa chọn.
  
- **Hover tiêu đề bài viết**:  
  ```css
  a.article-title:hover {
    color: #428bca;
    text-decoration: none;
  }
  ```

- **Giữ định dạng nội dung bài viết**:  
  ```css
  .article-content {
    white-space: pre-line;
  }
  ```

---

## 🚀 Cần cải thiện/ý tưởng thêm:
- [ ] Thêm **responsive design** để hiển thị tốt trên mobile (media queries).
- [ ] Bổ sung hiệu ứng chuyển động (animation) khi hover.
- [ ] Sử dụng biến màu sắc với `:root` để dễ đổi theme.
- [ ] Hỗ trợ chế độ **dark mode**.
- [ ] Thêm `box-shadow` nhẹ cho `.content-section` để tạo chiều sâu.

---

## 💡 Gợi ý mở rộng:
- Kết hợp thêm **CSS framework** như Bootstrap (nếu chưa dùng).
- Viết thêm `main-dark.css` để chuyển theme bằng toggle.
- Cho phép người dùng cá nhân hóa giao diện.
