import os
import sys
import class_weather
import class_csv
import threading

city= 'Mumbai'
seconds = 60
timer = None
timer_run = False
def start_timer_thread():
    global timer
    
    return None

def get_city_name():
    global city
    city = input("Enter Indian City Name Only:\n")
    return None

def log_temperature():
    global weather
    global excel
    while timer_run:
        temperature  = weather.get_temperature(city)
        print(temperature)
        excel.write_data(temperature)

if __name__ ==  "__main__":
    weather = class_weather.weather()
    excel = class_csv.excel()
    get_city_name()
    timer_run = True
    log_temperature()




