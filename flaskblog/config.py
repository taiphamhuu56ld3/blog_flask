import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com' # Địa chỉ máy chủ SMTP sử dụng để gửi email
    MAIL_PORT = 587 # Cổng máy chủ SMTP (thường là 587 với TLS hoặc 465 với SSL).
    MAIL_USE_TLS = True # Bật hoặc tắt sử dụng TLS (Transport Layer Security) cho kết nối email.
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
