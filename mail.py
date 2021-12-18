import os
import smtplib
import pandas as pd
import traceback
import logging

email_data = pd.read_csv('selected_candidates_list_prac.csv') #provide path of sample.csv
df = pd.DataFrame(email_data)
emails = list(df['Email_address'])

print(emails)


sender_email = "aniketphadtare5511@gmail.com"

#login credentials
username = "aniketphadtare5511@gmail.com"
password = 9922325511

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
print("connected")

for email in emails:
    try:
        rec_email= email
        message="Hey,You are selected"
        server.login(username,password)
        print("Login success")
        server.sendmail(sender_email,rec_email,message)
        print("Email has been sent")
        print('sent')
    except Exception as e:
        logging.error(traceback.format_exc())
        print(email)
        continue




server.quit()
