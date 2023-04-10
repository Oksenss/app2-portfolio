import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

username = 'oksens.company@gmail.com'
password = 'qnuktwacsilblgoh'

receiver = 'oksens.company@gmail.com'
context = ssl.create_default_context()

message = '''\
Subject: Wazne informacje na temat pedofilii w kosciele
How are you?
Bye
'''
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)