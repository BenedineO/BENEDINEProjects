# Importing Email libraries
import smtplib
from email.mime.text import MIMEText

# Storing email credentials
SMTP_SERVER = "mail.alamonkrecyclers.com"
SMTP_PORT = 587
SMTP_USER = 'automation@alamonkrecyclers.com'
SMTP_PASSWORD = '-.6L;i[06Fex'

# Dictionary with recipient emails and names
recipients ={
    "assignments@ritaafrica.com": "RITAAfrica",
    "obiekeabb@gmail.com": "Benedine",
    "cajeto2003@yahoo.com": "Nwabueze",
    "cokeke@alamonkrecyclers.com": "C.O",
    "fredalamptey@hotmail.com": "Freda",
    "olajudeadebayo93@gmail.com": "Olajide"
}

try:
    # Establish SMTP Connection with exception handling
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASSWORD)

    # Create a loop to send personalized emails to individual recipients
    for recipient, name in recipients.items():
        # Create the email content with personalization
        subject = f"Welcome to ALAMONK RECYCLERS LTD"
        body = f"""
Hello {name},
This is an email sent by Alamonk Recyclers Limited. 
We can assist in automating your various tasks using our upgraded AI Model.\n
Kindly, contact us by replying through this email to know your position.\n
Thank you,
Benedine Okeke
IT Support
"""

        # Creating a loop to send the email to individual recipients
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SMTP_USER
        msg["To"] = recipient

        # Sending the email
        server.sendmail(SMTP_USER, [recipient], msg.as_string())
        print(f"Email sent successfully to {recipient}.")

except smtplib.SMTPAuthenticationError as err:
    print(f"Connection error: {err}")
except smtplib.SMTPException as err:
    print(f"SMTP Server error: {err}")
except Exception as err:
    print(f"An error occurred: {err}")

# Close the connection
server.quit()

