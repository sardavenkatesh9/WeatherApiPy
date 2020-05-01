import sys
import pyowm

class weather:
    _api_key = '6763272ec78ec164d1cce20853cc9108' # private variable of class 
    connection = None
    def __init__(self):
        try:
            self.connection = pyowm.OWM(self._api_key)
        except Exception as err:
             print('Func : weather initialization ',err )
        return None 

    def get_temperature(self,city = 'Mumbai'):
        temperature = 0.0
        try:
            place_string = city + ',IN'
            observation = self.connection.weather_at_place(place_string)
            temperature= observation.get_weather().get_temperature('celsius')['temp']
        except Exception as err:
            print('Func : get_temperature ',err )
        return temperature

            
#Testing Code for class function excel        
##x = weather()
##print(x.get_temperature('solapur'))



