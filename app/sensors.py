import time

import adafruit_dht
import board

class Sensors:

    def __init__(self):
        self.dht = adafruit_dht.DHT22(board.D18)


    def getData(self):

        try:
            temperature = self.dht.temperature
            humidity = self.dht.humidity
            if humidity == None or temperature == None:
                return (None, None)
            if humidity >= 100:
                humidity = 99.99
            if temperature >= 100:
                temperature = 99.99
            return (temperature, humidity)

        except RuntimeError as e:
            print("Reading from DHT failure: ", e.args)
            return (None, None)
