import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 465
smtp_server = 'smtp.gmail.com'

sender_email = 'peach.cobbler.report@gmail.com'
receiver_email = 'ericstone111@gmail.com'
password = input('Type password and press enter: ')






message = MIMEMultipart('alternative')
message['subject'] = 'multipart test'
message['from'] = sender_email
message['to'] = receiver_email


text = '''\
Hi,
How are you?
This is a test.'''
html = '''\
<html>
    <body>
        <p>Hi,<br>
            <a href='http://www.realpython.com'>Real Python</a>
            has many great tutorials.
        </p>
    </body>
</html>
'''
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

message.attach(part1)
message.attach(part2)





context  = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    