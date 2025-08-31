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

⚙️ Setup

Create a .env file in the root of your project and add the following:

EMAIL_TO_CHECK=your_email@gmail.com
APP_PASSWORD_01=your_app_password_for_inbox
IMAP_SERVER=imap.gmail.com

EMAIL_TO_SEND=your_email@gmail.com
APP_PASSWORD_02=your_app_password_for_smtp


EMAIL_TO_CHECK: Gmail account to monitor for Vodafone bills

APP_PASSWORD_01: App password for inbox (generated in Google Account → Security → App Passwords)

EMAIL_TO_SEND: Gmail account used to send reminders (can be the same as above)

APP_PASSWORD_02: App password for sending emails via SMTP

⚠️ Do not use your real Gmail password. Always use App Passwords.

Add .env to .gitignore to prevent leaking credentials if using GitHub.

▶️ Usage

Run the script:

python main.py


What it does:

Connects to Gmail inbox.

Searches for emails with subject "Vodafone".

Extracts bill details (account number, invoice number, balance, due date).

Prints the details in the console.

Sends a reminder email to yourself with these details.

Waits 15 days before checking again.

📌 Customization

Change the subject filter:

status, data = mail.search(None, '(SUBJECT "Vodafone")')


Replace "Vodafone" with another keyword if your email subject is different.

Adjust the frequency (currently every 15 days):

time.sleep(15 * 24 * 60 * 60)


For daily checks, change to:

time.sleep(24 * 60 * 60)

🧪 Example Output

Console log:

Found 'Account number' at index: 377
Parts for 'Account number': ['959879262', 'Invoice', 'number', '1788828296', 'Total', 'balance']
Found 'Invoice number' at index: 402
Parts for 'Invoice number': ['1788828296', 'Total', 'balance', 'due', '$135.99DR', 'Due', '21', 'Aug']
Found 'Total balance due' at index: 428
Parts for 'Total balance due': ['$135.99DR', 'Due', '21', 'Aug', '2025']
Found 'Due' at index: 456
Parts for 'Due': ['21', 'Aug', '2025']
--- Vodafone Bill ---
Account number: 959879262
Invoice number: 1788828296
Total balance due: $135.99DR
Due: 21 Aug 2025
cycle count = 1


Email received:

Subject: Vodafone Bill Reminder 📩

Here are your latest Vodafone bill details:

Account number: 959879262
Invoice number: 1788828296
Total balance due: $135.99DR
Due date: 21 Aug 2025
Pay within 24 hours to avoid $15 (late fee)

🔒 Security Notes

Always use Gmail App Passwords. Normal Gmail passwords won’t work.

Don’t commit .env to public repositories.

Use a secondary Gmail account for testing, not your main one.

