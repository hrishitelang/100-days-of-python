# import smtplib, ssl
#
# my_email = "clareatkins7@gmail.com"
# recipient_email = "jeffroberts1003@yahoo.com"
# password = "gigudi1234"
# PORT = 587
#
# context = ssl.create_default_context()
# connection = smtplib.SMTP("smtp.gmail.com", port=PORT)
#
# #A way of securing our connection to our email server
# connection.starttls(context=context)
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=recipient_email,
#     to_addrs=my_email,
#     msg="Subject:Mail from your bf <3\n\nHello Clare, love you too babe."
# )
# connection.close()
#
# '''
# # This is another code that also works
# port = 465  # For SSL
# my_email = "clareatkins7@gmail.com"
# password = "gigudi1234"
#
# # Create a secure SSL context
# context = ssl.create_default_context()
#
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login(my_email, password)
#     server.sendmail(from_addr=my_email, to_addrs="jeffroberts1003@yahoo.com", msg="Hello Jeff, love you.")
# '''
#

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
second = now.second
milliseconds = now.microsecond
day_of_week = now.weekday()
print(now)
print(year)
print(month)
print(second)
print(second)
print(milliseconds)
print(day_of_week)
