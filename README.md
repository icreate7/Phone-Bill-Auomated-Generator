📧 Email Sender with Python

This project allows you to send emails securely using Python’s built-in smtplib and email.mime modules. It also uses python-dotenv to load sensitive credentials (like email and app password) from a .env file instead of hardcoding them in your script.


🚀 Features

Send emails through Gmail (can be modified for other providers).

Secure authentication using App Passwords (not your real Gmail password).

Keeps credentials safe in a .env file.

Easy to configure and run.


🛠️ Installation

Clone or download this project.

Install dependencies:

pip install python-dotenv


(Python’s smtplib and email.mime are built-in, so no need to install them separately.)


⚙️ Setup

Create a .env file in the root of your project and add your credentials:

EMAIL_TO_SEND=your_email@gmail.com
APP_PASSWORD_02=your_generated_app_password


⚠️ Use a Gmail App Password (not your Gmail login password).
You can generate one at: Google App Passwords

Make sure your .env file is in the same folder as your script.


📌 Notes

Works with Gmail by default. For Outlook, Yahoo, etc., you’ll need to update the SMTP server and port.

If the email fails, check that your .env is loaded correctly and that your app password is valid.

Never commit your .env file to GitHub – add it to .gitignore.
