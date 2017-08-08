
from twython import Twython

class Twit:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.twitter = Twython(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret)

    def twit(self, message):
        self.twitter.update_status(status=message)
        return message