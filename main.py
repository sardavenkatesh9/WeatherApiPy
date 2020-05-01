import os
import sys
import class_weather
import class_csv
import time
from timeloop import Timeloop
from datetime import timedelta


city= 'Mumbai'
WAIT_SECONDS = 60
timer = None
timer_run = False
tl = Timeloop()

## Time start 
def start_timer_thread():
    global t1
    tl.start()
    return None

## Get city name runtime logic
def get_city_name():
    global city
    city = input("Enter Indian City Name Only:\n")
    return None

## Repeat Loop after interval
@tl.job(interval=timedelta(seconds=WAIT_SECONDS))
def log_temperature():
    global weather
    global excel
    temperature  = weather.get_temperature(city)
    print(temperature)
    excel.write_data(temperature)

if __name__ ==  "__main__":
    weather = class_weather.weather()
    excel = class_csv.excel()
    get_city_name()
    start_timer_thread()
    while True:
        pass




