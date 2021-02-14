import requests
from datetime import datetime
import smtplib, ssl
import time

my_email = "clareatkins7@gmail.com"
recipient_email = "telang.hrishikesh@gmail.com"
password = "gigudi1234"
PORT = 587

MY_LAT = 19.249206
MY_LONG = 72.853555

def is_iss_up():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if iss_latitude-5 <= MY_LAT <= iss_latitude+5 and iss_longitude-5 <= MY_LAT <= iss_longitude+5:
        return True
    else:
        return False

def is_it_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1][:2])
    sunset = int(data["results"]["sunset"].split('T')[1][:2])
    time_now = datetime.now()
    if now.hour >= sunset or now.hour <= sunrise:
        return True
    else:
        return False

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_iss_up() and is_it_night():
        context = ssl.create_default_context()
        connection = smtplib.SMTP("smtp.gmail.com", port=PORT)
        # A way of securing our connection to our email server
        connection.starttls(context=context)
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look up! \n\nISS is above you!"
        )
        connection.close()



