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

▶️ Usage

Example script (send_email.py):

from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

EMAIL = os.getenv("EMAIL_TO_SEND")
PASSWORD = os.getenv("APP_PASSWORD_02")

# Email details
to_email = "receiver@example.com"
subject = "Test Email"
body = "Hello, this is a test email sent from Python!"

# Create message
msg = MIMEMultipart()
msg["From"] = EMAIL
msg["To"] = to_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Send email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, to_email, msg.as_string())
    server.quit()
    print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Error:", e)

🧪 Run the script
python send_email.py

📌 Notes

Works with Gmail by default. For Outlook, Yahoo, etc., you’ll need to update the SMTP server and port.

If the email fails, check that your .env is loaded correctly and that your app password is valid.

Never commit your .env file to GitHub – add it to .gitignore.
