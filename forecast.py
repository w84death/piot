import os
import pyowm
import config
import commands

class Forecast:
    def __init__(self):
        self.cmds = commands.Commands()
        self.cfg = config.Config()
        self.owm = pyowm.OWM(self.cfg.get_api_key('forecast'))

    def get_file(self, item):
        return self.file[item]

    def get_weather(self):
        observation = self.owm.weather_at_place('Poznan,pl')
        weather = observation.get_weather()
        temp = weather.get_temperature('celsius')['temp']
        speed = weather.get_wind()['speed']
        clouds = weather.get_clouds()
        return temp, speed, clouds

    def get_report(self):
        temp, speed, clouds = self.get_weather()
        message = self.cmds.get_cmd('forecast')['success']
        report = message.format(temp=temp, speed=speed, clouds=clouds )
        return report 