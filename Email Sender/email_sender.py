import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Patricia Faria'
email['to'] = 'andrei@zerotomastery.io'
email['subject'] = 'Sorry'


email.set_content(html.substitute(name='Andrei'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pyth0n.t3st1@gmail.com', 'python!123')
    smtp.send_message(email)
    print('All Good!')