import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(email, title, text):
    try:
        addr_form = 'tinttyebot@yandex.ru'
        password = 'jkyqkquxqmdmcdnz'

        msg = MIMEMultipart()
        msg['From'] = addr_form
        msg['To'] = email
        msg['Subject'] = title

        body = text
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.login(addr_form, password)

        server.send_message(msg)
        server.quit()
        return True
    except:
        return False