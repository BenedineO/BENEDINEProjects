import smtplib
from email.mime.text import MIMEText

# Storing our credentials
SMTP_SERVER = "mail.alamonkrecyclers.com"
SMTP_PORT = 587
SMTP_USER = 'automation@alamonkrecyclers.com'
SMTP_PASSWORD = '-.6L;i[06Fex'

recipients = ["obiekeabb@gmail.com", "benedinenokeke@gmail.com", "cajeto2003@yahoo.com", "cokeke@alamonkrecyclers.com"]

# Establish SMTP Connection
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SMTP_USER, SMTP_PASSWORD)

# Create the email content
subject = "Welcome to ALAMONK RECYCLERS LTD"
body = """This is an email sent by Alamonk Recyclers Limited. We can assist in automating your various tasks using our upgraded AI Model.\n
Kindly, contact us by replying through this email to know your position. \n
Thank you."""


# Create a loop to send the email to individual recipients
for recipient in recipients:
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = recipient

    server.sendmail(SMTP_USER, [recipient], msg.as_string())
    print(f"Email sent successfully to {recipient}.")

# Close the connection
server.quit()