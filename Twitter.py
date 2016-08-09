__author__ = 'Bharath'


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "127748173-DJjKvt92xeTtyP5ERhAIvR33Mn7pdZCsKun5VoRE"
access_token_secret = "EK4jk2Au5wMME7uPORJP4iMTuGAcRSPnk1Lxn3Hyg0aSX"
consumer_key = "WHD81FGlONrQSyhZ9rkimrIYD"
consumer_secret = "8V69CGm51ZKa5lmuHyCmnMCMU5yGo58iaXitj6w5OF4pzjJNC6"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python','javascript','ruby'])
