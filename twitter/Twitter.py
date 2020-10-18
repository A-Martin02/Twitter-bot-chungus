import tweepy as tp
import time
import os
import requests
import random

def tweetToTwitter():
    consumer_key = 'A2pMY3f8bo8EuwjnwlDHBjvuf'
    consumer_secret = '8J4UoNapWjZqcHhVucBqbtxxq3YJHIA08pb2wU4lT663BmRWh2'
    access_token = '1240275761195552769-BxLDfRCtP6cRShyM1CmI9PgTiivLuI'
    access_secret = 'wrqe51u1SzDINhneIvFmeygz2p1mdPnBKsHlYvLdLdyNI'

    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tp.API(auth)

    responses = ['Hello, this is bot',
                 'Pog Valorant Gamer',
                 'i need to tell you guys now, sex is myth made up by the government and ill tell you why, okay first they tell that sex is "technically" p in v or willy in vagina, which is what they tell us in class which is completely false a can tell you if sex was a thing id be having plenty of it, im sorry if someones gonna tell me im a little virgin FUCK OFF im a shagger by nature part 1 - Quote from @MilkGodLactator',
                 'Big Big Chungus',
                 'Oh hello everyone, wanna get some pizza?']

    responeData = (random.choice(responses))
    mystatustext = str(responeData)
    api.update_status(status=mystatustext)

def main():
    print('welcome to my twitter')
while True:
    tweetToTwitter()
    time.sleep(24 * 3600)

if __name__ == '--__main__':
    MAIN()
