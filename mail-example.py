import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
 
server = smtplib.SMTP('smtp.xxxx', 587)

server.ehlo()
server.starttls()
with open('secret.txt', 'r') as f:
    passw = f.read() 

server.login('zz@xx', passw)

msg = MIMEMultipart()
msg['From'] = 'No-Reply'
msg['To'] = 'ab@yy'
msg['Subject'] = 'pyNet - Update'


with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

file = 'file.png'
attachment = open(file, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disiposition',f'attachment; filename={file}')
msg.attach(p)

text = msg.as_string()
server.sendmail('noreply@xx', 'ab@yy', text)
server.quit()