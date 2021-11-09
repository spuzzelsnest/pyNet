import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
 
server = smtplib.SMTP('smtp.office365.com', 587)

server.ehl0()
with open('secret.txt', 'r') as f:
    password =f.read() 

server.log('jan.desmet@sint-lievenshoutem.be', 'password')

msg = MIMEMultipart()
msg['From'] = 'noreply@sint-lievens-houtem.be'
msg['To'] = 'helpdesk@sint-lievens-houtem.be'
msg['Subject'] = 'pyNet - Update'