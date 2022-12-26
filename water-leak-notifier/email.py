import smtplib
import email.mime.multipart
from email.mime.text import MIMEtext

def send_mail(message):
    gmail_user = 'gmail@account'
    gmail_password = 'password'

    try:
        msg = email.mime.multipart.MIMEmultipart()
        msg['to'] = 'Your Name<your-email-adress@domain.com>'
        msg['from'] = 'Your gmail<gmail-account-name@gmail.com>'
        msg['subject'] = 'test'
        msg.add_header('reply-to', 'your-gmail-account-name@gmail.com')
        msg.attach(MIMEtext(message, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(gmail_user, gmail_password)
        message = msg.as_string()
        session.sendmail('your-gmail-account-name@gmail.com',
                         'your-email-adress@domain.com', message)
        session.quit()
        print('email sent.')
    except:
        print('email failed to sent.')

send_mail('this is the body of the email test message.')
