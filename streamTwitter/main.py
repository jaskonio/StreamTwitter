# get tweets
# save tweets in mongodb
import tweepy
import time
from tweepy import OAuthHandler
from tweepy import Stream


#Variables that contains the user credentials to access Twitter API 
config = {
    "consumer_key": "q1XsctQfkyWnzxktoHfiN6ELM",
    "consumer_secret": "1nXXoXK5mklJFCZ0GQtU11JwDHl5XOq8vfZErLPg83xDulBmPF",
    "access_key": "190651136-1WTRHboChmrM4wa0zjd7mnObbr5N7xQXRLTrO3lP",
    "access_secret": "2XmDcL46aZNVYnyOuLMJOPZ73Am22HCFtZmWQYUpGXi5s",
    "limitTrends" : ""
}

configForTrend = {
    "consumer_key" : "x4Zd1QTw3EWd5G5DsumfhQl09",
    "consumer_secret" : "NHkiTwVbCoVDkKZkRyEwSJeIlKedMJfxKEjK1dx227YS4mvCPC",
    "access_key" : "190651136-GE2QMmJwjfrrM2ZYSN4Ve9RfIMrJk4684ZiuIUti",
    "access_secret" :"am12qQpAv53Y3a1OQQt687691MS2DWtGhyQZiVGywGnqp",
    "idGeolocation" : 23424950 #id Spain
}

class StdOutListener( tweepy.StdOutListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

def getTrends():
    auth = tweepy.OAuthHandler(
        configForTrend["consumer_key"], configForTrend["consumer_secret"])
    auth.set_access_token(configForTrend["access_key"], configForTrend["access_secret"])
    api = tweepy.API(auth)
    trends1 = api.trends_place( configForTrend["idGeolocation"])


    print("SPAIN Trends")
    data = trends1[0]
    trends = data['trends']
    hastasgs = []
    names = [trend['name'] for trend in trends]
    #trendsName = ' '.join(names)
    for name in names:
        print(" - %s" % name)
        hastasgs.append(name)
    return hastasgs

def getMinute():
    return time.strftime("%M")

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()

    auth = OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_key"], config["access_secret"])

    stream = Stream(auth, l)


    trends = getTrends()
    print(trends)
    stream.filter(track=trends)
    


