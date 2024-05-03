import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config as c
import properties1 as p 
from database import fetch_texts_by_id

def send_email(id, receiver_mail):

    recorded_text, summarized_text = fetch_texts_by_id(id)
    
    # Create a message
    msg = MIMEMultipart()
    msg['From'] = p.sender_email
    msg['To'] = receiver_mail  # Recipient's email address
    msg['Subject'] = 'Recorded Text'
    
    # Add body to email
    body = f"Recorded Text:\n{recorded_text}\n\nSummarized Text:\n{summarized_text}"
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server and send the email
    with smtplib.SMTP(c.smtp_server, c.smtp_port) as server:
        server.starttls()
        server.login(p.sender_email, p.sender_password)
        server.sendmail(p.sender_email, receiver_mail, msg.as_string())
        print("the recorded text has been sent to your mail - ", receiver_mail)


# send_email("hello hi skfvbksbvfasjhvf lhv flk sicg isv wsif oidfgsdufg iwudf w")