import smtplib
from email.message import EmailMessage
import imghdr

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("멋사 10기 코드라이언 수업 중 입니다.")

message["Subject"] = "제목: 읽어보세요."
message["From"] = "본인이메일@gmail.com"
message["To"] = "###@gmail.com"

with open("frog.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('frog',image_file)
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("본인 이메일@gmail.com","발급 받은 앱 비밀번호")
smtp.send_message(message)
smtp.quit()