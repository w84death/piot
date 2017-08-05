from time import localtime, strftime

class Logger:
    def __init__(self):
        self.log = []

    def get_log(self):
        return self.log

    def get_timestamp(self):
        t = strftime("%H:%M:%S", localtime())
        return '[{time}]'.format(time=t)

    def format(self, event):
        log_msg = '{message}'.format(message=event.get('type'))
        if event.get('user'):
            log_msg += ' <' + str(event.get('user')) + '> '
        if event.get('text'):
            log_msg += event.get('text').encode('ascii', 'replace')
        return log_msg

    def save_event(self, message):
        self.save(self.format(message))
        return True

    def save(self, message):
        log_msg = '{time} {message}'.format(
            time=self.get_timestamp(), 
            message=unicode( message, "utf8" ) )
        self.log.append(log_msg)
        return True