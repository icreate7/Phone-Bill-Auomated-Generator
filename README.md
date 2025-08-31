📩 Vodafone Bill Email Automation

This Python project automates the process of:

Checking your Gmail inbox for Vodafone bill emails.

Extracting key bill details such as:

Account number

Invoice number

Total balance due

Due date

Sending yourself an email reminder with the extracted details.

The script runs in a loop and checks for new Vodafone emails every 15 days (configurable).

🚀 Features

Automatically fetches the latest Vodafone email (read or unread).

Parses email content using BeautifulSoup.

Extracts important billing information.

Sends a formatted reminder email via Gmail.

Securely manages credentials with .env file.

🛠️ Installation

Clone or download this project.

Install dependencies:

pip install beautifulsoup4 python-dotenv


(Python’s smtplib, imaplib, email, time, and os are built-in, no need to install them.)


🔒 Security Notes

Always use Gmail App Passwords. Normal Gmail passwords won’t work.

Don’t commit .env to public repositories.

Use a secondary Gmail account for testing, not your main one.

