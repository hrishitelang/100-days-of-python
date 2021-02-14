##################### Hard Starting Project ######################
import datetime as dt
import pandas as pd
import smtplib, ssl
import random

my_email = "clareatkins7@gmail.com"
recipient_email = birthdays_dict[today]['email']
password = "gigudi1234"
PORT = 587

data = pd.read_csv('birthdays.csv')
now = dt.datetime.now()
today = (now.month, now.day)

# I am creating a dictionary from birthdays.csv that looks like this:
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()} #Note
# print(birthdays_dict)

if today in birthdays_dict:
    name = birthdays_dict[today]['name']
    # print(name)
    file_name = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_name, 'r') as file:
        a = file.read() #Note
        a = a.replace('[NAME]', name)
        # print(a)
        context = ssl.create_default_context()
        connection = smtplib.SMTP("smtp.gmail.com", port=PORT)
        #A way of securing our connection to our email server
        connection.starttls(context=context)
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Happy birthday {name} <3\n\n{a}"
        )
        connection.close()



