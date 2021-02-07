
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
import requests
import tweepy #https://github.com/tweepy/tweepy
import csv
import os
import json
#from tqdm import tqdm
from time import sleep
import oauth2 as oauth
from django.template import loader
#from .apps import TwitterapiConfig
from django.http import HttpResponseServerError
from .forms import Twitter_Api,Twitter_Api_Hashtags

twitter_exception="<html><body background=#dddddd font-family:sans-serif><h1> Something is not happening!</h1></body></html>"
name = 'TwitterApi'
thisdict = {
  "consumer_key": "0",
  "consumer_secret": "0",
  "access_token":"0",
  "access_token_secret":"0"
}

#consumer_key:"QXrNpWVbUyYdiXVoUGtbZlDJL"
#consumer_secret:"lREYmZMZrm5tsWZfV9iChhmBSU8BtabIcQYeEuvI2hhu2AI2Lm"
#access_token:"105053184-1JHgKk8fxR6o7TljN5Sh1iQjEJXtiHtVGo2wyMvl"
#access_token_secret:"1LocIjNfQViocOhdkLiplUUiXeRD0mIGnH3vTBrUODCSw"
#consumer_key = "QXrNpWVbUyYdiXVoUGtbZlDJL"
#consumer_secret = "lREYmZMZrm5tsWZfV9iChhmBSU8BtabIcQYeEuvI2hhu2AI2Lm"
#access_token = "105053184-1JHgKk8fxR6o7TljN5Sh1iQjEJXtiHtVGo2wyMvl"
#access_token_secret = "1LocIjNfQViocOhdkLiplUUiXeRD0mIGnH3vTBrUODCSw"

def index(request):
    form = Twitter_Api(request.POST)
    if request.method=='POST':
        try:
            if form.is_valid():
                consumer_key = request.POST.get('consumer_key')
                consumer_secret = request.POST.get('consumer_secret')
                access_token = request.POST.get('access_token')
                access_token_secret = request.POST.get('access_token_secret')
                searchtag=request.POST.get('Hashtags')
                sincedate=request.POST.get('since_Date')
                untildate=request.POST.get('until_Date')
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                #auth.set_access_token(access_token, access_token_secret)
                #api = tweepy.API(auth)
                # Open/create a file to append data t
                api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True )
                public_tweet =tweepy.Cursor(api.search,
                                        q = searchtag,
                                        since = sincedate,
                                        until = untildate,
                                        lang = "en").items(100)

                filename=os.path.join(os.environ["HOMEDRIVE"],os.environ["HOMEPATH"], "Downloads","pythonscsv.csv")
                with open(filename,"a", encoding="utf-8") as f:
                    csvWriter = csv.writer(f)
                    csvWriter.writerow(['CREATED_AT', 'TWEET ID','LIKES COUNT','RETWEETS COUNT','USER ID','USER_LOCATION','USER_SCREEN_NAME' ,'SOURCE','TWEETS'])
                    for tweet in public_tweet:
                        csvWriter.writerow([tweet.created_at,tweet.id,tweet.favorite_count, tweet.retweet_count, tweet.user.id,tweet.user.location,tweet.user.screen_name,tweet.source,tweet.text])
                        #print (tweet.created_at, tweet.text)
                    return redirect("sucex")
            else:
                form = Twitter_Api()

        except Exception as e:
            print(e)
            return HttpResponse(e)
            
        
    return render(request, 'TwitterApi/home.html', {"form":form})
def succes(request):
    return render(request, 'TwitterApi/sucess.html')

def loginmsg(request):
    return render(request, 'TwitterApi/loginmsg.html')

    
