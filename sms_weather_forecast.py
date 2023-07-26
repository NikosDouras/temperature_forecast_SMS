import requests
from twilio.rest import Client


MY_LATITUDE = 40.629269
MY_LONGITUDE = 22.947412
URL = "https://api.open-meteo.com/v1/" \
      "forecast?latitude=40.641282&longitude=22.948381&daily=weathercode,temperature_2m_max&timezone=Europe%2FBerlin"
SID =
TOKEN =
MY_PHONE_NUMBER =
CLIENT =

def getting_temp():
    temporary = requests.get(url=URL)
    data = temporary.json()
    temp_today = data["daily"]["temperature_2m_max"][0]

    return temp_today


def sending_sms():
    temp = getting_temp()
    sms_client = Client(SID, TOKEN)
    sms_message = sms_client.messages.\
        create(from_=MY_PHONE_NUMBER, to=CLIENT, body=f"Highhest temperature today, {temp}C")


sending_sms()