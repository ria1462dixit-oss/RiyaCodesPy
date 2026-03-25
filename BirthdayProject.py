import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time

sender = "your email"
password = "your password"

receiver = input("Enter email: ")
name = input("Enter name: ")
birthdate = input("Enter birthdate (dd-mm): ")
print("info taken")

send_time = 12
send_minute = 45

while True:
    now = datetime.now()
    today = now.strftime("%d-%m")

    print("checking conditions")

    if birthdate == today and now.hour == send_time and now.minute == send_minute:
        msg = MIMEText(f"Happy birthday {name} 🎉")
        msg['Subject'] = "Happy Birthday"
        msg['From'] = sender
        msg['To'] = receiver
        
        
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(sender, password)
            server.send_message(msg)
            server.quit()
            print("Email sent 🎉")
            break
        except Exception as e:
            print("Failed:", e)

    time.sleep(30)