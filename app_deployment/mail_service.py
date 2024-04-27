import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config as c

def send_email(body):
    
    # Create a message
    msg = MIMEMultipart()
    msg['From'] = c.sender_email
    msg['To'] = c.receiver_mail  # Recipient's email address
    msg['Subject'] = 'Recorded Text'
    
    # Add body to email
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server and send the email
    with smtplib.SMTP(c.smtp_server, c.smtp_port) as server:
        server.starttls()
        server.login(c.sender_email, c.sender_password)
        server.sendmail(c.sender_email, c.receiver_mail, msg.as_string())
        print("the recorded text has been sent to your mail - ",c.receiver_mail)


# send_email("hello hi skfvbksbvfasjhvf lhv flk sicg isv wsif oidfgsdufg iwudf w")