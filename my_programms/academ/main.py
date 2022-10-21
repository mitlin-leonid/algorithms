from email import encoders
from email.mime.base import MIMEBase
import smtplib
import os
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



me = 'mitlinleonid@gmail.com'
me2 = 'mitlinleonid@liceyklassic.ru'
password = 'CikjG6NiHtmawG1986'
password_2 = 'sonar078111986'
password_1 = 'pcxvmplounbgtfju'

email_getter = 'mitlinleonid@yandex.ru'

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(me2, password_2)

msg = MIMEMultipart()
msg["Subject"] = "Тут тема сообщени23232я"
msg.attach(MIMEText("Привет, это я сно232323ва и снова"))

file = "C:\\my_project\\algorithms\\my_programms\\academ\\Это приказ.docx"
filename = os.path.basename(file)
ftype, encoding = mimetypes.guess_type(file)
file_tupe, subtype = ftype.split("/")

with open(file, "rb") as f:
    file1 = MIMEBase(file_tupe, subtype)
    file1.set_payload(f.read())
    encoders.encode_base64(file1)

file1.add_header('content-disposition', 'attachment', filename=filename)

msg.attach(file1)


smtp_server.sendmail(me2, me2, msg.as_string())