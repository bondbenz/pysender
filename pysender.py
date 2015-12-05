#!/usr/bin/python
import smtplib

print '''
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<   ___       __                _           <
<  / _ \_   _/ _\ ___ _ __   __| | ___ _ __ <
< / /_)/ | | \ \ / _ \ '_ \ / _` |/ _ \ '__|<
</ ___/| |_| |\ \  __/ | | | (_| |  __/ |   <
<\/     \__, \__/\___|_| |_|\__,_|\___|_|   <
<       |___/                               <                      
<        [+] Developed & Coded by Bond Benz <
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

     '''

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Send Informations
sender = raw_input('Sender Email : ')
to = raw_input('To : ')
subj = raw_input('Subject : ')
message = raw_input('Message : ')

#SMTP Server
smtpserver = raw_input('SMTP Server : ')
smtpuser = raw_input('SMTP Username : ')
smtppass = raw_input('SMTP Password : ')
smtpport = raw_input('SMTP Port : ')

#MIME Infos
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = to
msg['Subject'] = subj
msg.attach(MIMEText(message))
#Don't Edit
try:
    server = smtplib.SMTP(smtpserver)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(smtpuser,smtppass)
    server.sendmail(sender,to,msg.as_string())
    server.quit()
    print '[+] Mail Successfully Sent.'
except SMTPException:
    print '[!] Error : Unable to connect to smtp.'
    
    




