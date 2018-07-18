#coding: utf-8
import RPi.GPIO as gpio

motorPin = 37

class Motor:
    def on(self):
        gpio.output(motorPin,True)

    def off(self):
        gpio.output(motorPin,False)

    @staticmethod
    def finish():
        gpio.cleanup()

    @staticmethod
    def setup():
        gpio.setmode(gpio.BOARD)
        gpio.setup(motorPin,gpio.OUT)
