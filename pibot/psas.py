from time import strftime, localtime
import commands
import whiteboard
import logger
import forecast

class PublicServiceAnnaucments:
    def __init__(self):
        self.cmds = commands.Commands()
        self.fc = forecast.Forecast()
        self.timestamps = {
            '**:00:00': 'full_hour',
            '**:30:00': 'forecast',
            '09:30:00': 'standup',
            '10:00:00': 'standup'
        }

    def get_psa(self, cmd):
        hour = strftime("%H:%M", localtime())

        if cmd == 'full_hour':
            return self.cmds.get_psa('time').format(time=hour)
            
        if cmd == 'forecast':
            return self.fc.get_report()

        if cmd == 'standup':
            return self.cmds.get_psa('standup').format(time=hour)

        return False

    def check_scheduler(self):
        hour_now = strftime("%H", localtime())
        time_now = strftime("%H:%M:%S", localtime())
        for ts in self.timestamps:
            if ts.replace('**', hour_now) == time_now:
                return self.get_psa(self.timestamps[ts])
        return False
