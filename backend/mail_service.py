import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config as c

def send_email(body):
    # Set up the SMTP server
    # smtp_server = 'smtp.gmail.com'  # Your SMTP server address
    # smtp_port = 587  # Your SMTP server port
    # sender_email = 'aksht757@gmail.com'  # Your email address
    # sender_password = 'qjpp pvsf wzmv vzde'  # Your email password
    # receiver_mail = 'akert263@gmail.com'
    
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