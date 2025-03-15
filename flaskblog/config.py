import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com' # SMTP server address to use for sending emails
    MAIL_PORT = 587 # SMTP server port (usually 587 with TLS or 465 with SSL).
    MAIL_USE_TLS = True # Enable or disable the use of TLS (Transport Layer Security) for email connections.
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
