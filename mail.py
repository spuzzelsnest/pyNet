import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
 
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
with open('secret.txt', 'r') as f:
    password =f.read() 

server.log('j.mpdesmet@gmail.com', 'password')

msg = MIMEMultipart()
msg['From'] = 'j.mpdesmet@gmail.com'
msg['To'] = 'helpdesk@sint-lievens-houtem.be'
msg['Subject'] = 'pyNet - Update'