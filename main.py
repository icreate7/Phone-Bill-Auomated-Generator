import imaplib
import email
import smtplib
import time
from bs4 import BeautifulSoup
from email.header import Header
import os

from dotenv import load_dotenv

load_dotenv()

# Email login details
EMAIL_TO_CHECK = os.getenv('EMAIL_TO_CHECK')
APP_PASSWORD_01 = os.getenv('APP_PASSWORD_01')
IMAP_SERVER = os.getenv('IMAP_SERVER')

EMAIL_TO_SEND = os.getenv('EMAIL_TO_SEND')
APP_PASSWORD_02 = os.getenv('APP_PASSWORD_02')

count = 0

while True:
    try:
        # Connect to Gmail
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_TO_CHECK, APP_PASSWORD_01)
        mail.select("inbox")

        # Search for Vodafone emails (read + unread)
        status, data = mail.search(None, '(SUBJECT "Vodafone")')
        email_ids = data[0].split()

        if not email_ids:
            print("No Vodafone bill emails found.")
        else:
            latest_email_id = email_ids[-1]

            # Fetch the latest email
            status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            body = None
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/html":
                        body = part.get_payload(decode=True).decode(errors="ignore")
                        break
            else:
                if msg.get_content_type() == "text/html":
                    body = msg.get_payload(decode=True).decode(errors="ignore")

            if body:
                # Parse HTML with BeautifulSoup
                soup = BeautifulSoup(body, "html.parser")
                text = soup.get_text(" ", strip=True)

                # Extract bill details
                details = {}
                keywords = ["Account number", "Invoice number", "Total balance due", "Due"]

                for kw in keywords:
                    idx = text.find(kw)
                    print(f"Found '{kw}' at index: {idx}")

                    if idx != -1:
                        snippet = text[idx + len(kw): idx + len(kw) + 50]
                        parts = snippet.split()
                        print(f"Parts for '{kw}': {parts}")

                        if kw == "Due":
                            details[kw] = " ".join(parts[:3]) if parts else "Not found"
                        else:
                            details[kw] = parts[0] if parts else "Not found"
                    else:
                        details[kw] = "Not found"

                # Print results
                print("\n--- Vodafone Bill ---")
                for k, v in details.items():
                    print(f"{k}: {v}")

                # Format all details into one email
                subject = Header("Vodafone Bill Reminder 📩", "utf-8").encode()
                body = f"""
                Here are your latest Vodafone bill details:

                Account number: {details.get("Account number", "Not found")}
                Invoice number: {details.get("Invoice number", "Not found")}
                Total balance due: {details.get("Total balance due", "Not found")}
                Due date: {details.get("Due", "Not found")}
                Pay within 24 hours to avoid $15 (late fee)
                """

                msg_out = f"Subject: {subject}\n\n{body}"

                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    connection.login(user=EMAIL_TO_SEND, password=APP_PASSWORD_02)
                    connection.sendmail(
                        from_addr=EMAIL_TO_SEND,
                        to_addrs=EMAIL_TO_SEND,
                        msg=msg_out
                    )

                count += 1
                print(f'cycle count = {count}')

        mail.logout()

    except Exception as e:
        print(f"Error: {e}")

    # Run daily (change as needed)
    time.sleep(30)
