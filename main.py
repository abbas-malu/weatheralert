import datetime
import json
import time

from pushbullet import PushBullet, Pushbullet
import requests

api_key_open_weather = '70121c1eaf3d32f16cef18f3b0ee3b5c'
api_key_push_bullet = 'o.d127KfpZF6bs88SzEIxF54govzvQRkau'
notifier = PushBullet(api_key=api_key_push_bullet)

notify_time = str(datetime.time(hour=9))
# print(notify_time)
# print(datetime.datetime.now().strftime('%H:%M'))
def kelvin_to_celsius(kelvin_temp:float):
    celsius_temp = kelvin_temp-273.15
    return round(celsius_temp,2)
# print(kelvin_to_celsius(308.25))
def wind_speed_converter(wind_Speed_in_meter_per_sec):
    return round(wind_Speed_in_meter_per_sec*3.6,2)
def time_converter(timestamp_format_time):
    return datetime.datetime.fromtimestamp(timestamp_format_time).strftime('%H:%M:%S')
while True:
    print(notify_time,':::',datetime.datetime.now().strftime('%H:00:00'))
    if notify_time == datetime.datetime.now().strftime('%H:00:00'):
        # notifier.push_note('Hello baby!!!')
        weather_data = json.loads(requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=indore&appid={api_key_open_weather}').text)
        weather_heading = weather_data['weather'][0]['main']
        weather_desc = weather_data['weather'][0]['description']
        current_temp = kelvin_to_celsius(weather_data['main']['temp'])
        temp_min = kelvin_to_celsius(weather_data['main']['temp_min'])
        temp_max = kelvin_to_celsius(weather_data['main']['temp_max'])
        humidity = weather_data['main']['humidity']
        wind_speed = wind_speed_converter(weather_data['wind']['speed'])
        sunrise = time_converter(weather_data['sys']['sunrise'])
        sunset = time_converter(weather_data['sys']['sunset'])
        Notification_title = 'Good Morning! Abbas:)\n'
        Notification_body = f"Today's Weather:\n{weather_heading} : {weather_desc}\nCurrent Temprature : {current_temp} C\nMinimum Temprature : {temp_min} C\nMaximum Temprature : {temp_max} C\nHumidity : {humidity}%\nWind Speed : {wind_speed} Km/H \nSunrise : {sunrise}\nSunset : {sunset}"
        notifier.push_note(title=Notification_title,body=Notification_body)
        requests.get(f'https://api.telegram.org/bot1860349034:AAGsBHLtzExP5rcK9AHlUEqrgtaLAaiw1SI/sendMessage?chat_id=860825699&text={Notification_title+Notification_body}')
        time.sleep(86400)
