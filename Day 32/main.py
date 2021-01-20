import smtplib

my_email = "clareatkins7@gmail.com"
password = "gigudi1234"
connection = smtplib.SMTP("smtp.gmail.com")

#A way of securing our connection to our email server
connection.starttls()
connection.login(user=my_email, password=password)

connection.sendemail(from_addr=my_email, to_addrs="jeffroberts1003@yahoo.com", msg="Hello Jeff, love you.")
connection.close()