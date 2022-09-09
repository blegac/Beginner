from email.message import EmailMessage
import ssl
import smtplib

email_sender = "blegac3@gmail.com"
email_password = "jnepiogaalrgcmua"

email_receiver = "nacofip270@lurenwu.com"

subject = "Hello future me"
body = """
Bonjour comment vas-tu ?"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())