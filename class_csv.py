import sys
import csv
from datetime import datetime
import os

class excel:
    _file_name = ''
    _file = None
    def __init__(self):
        self._file_name = os.getcwd() + "\\" + datetime.now().strftime("%Y_%m_%d") + ".csv"
        if not os.path.exists(self._file_name):
            with open(self._file_name, "w") as file:
                writer = csv.writer(file)
                writer.writerow(["SN", "Temperature", "Time"])
        else:
            print('Warning: File already exists')
        return None

    def write_data(self,data = 0.0):
        with open(self._file_name, "a+")as file:
            writer = csv.writer(file)
            writer.writerow(["loop", str(data), datetime.now().strftime("%H:%M:%S")])
        return None

            
#Testing Code for class function excel        
##x = excel()
##x.write_data(02.0)



