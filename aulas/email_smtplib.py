# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:55:37 2024

@author: Riartts
"""

from email.message import EmailMessage
import smtplib

msg = EmailMessage()
payload = payload = """Olá! Tudo bem?

Este é um e-mail automático para testar o disparo de e-mails.

Atenciosamente,

WManero Devops

"""

msg.set_content(payload)
msg['From'] = "wmanero@hotmail.com"
msg['To'] = "wmanero@hotmail.com"
msg['Subject'] = 'Email Automático - SMTPLIB'

with open ('Obiwan.jpg', 'rb') as file:
    file_data = file.read()
    
msg.add_attachment(file_data, maintype='image', subtype='jpg')
smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtp.starttls()
smtp.login('wmanero@hotmail.com','jrzouxsubnvoybhx')

smtp.send_message(msg)
smtp.quit()

    
















