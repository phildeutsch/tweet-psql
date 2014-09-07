import sys
sys.path.append('../TwitterAPI')
from keys import *
from TwitterAPI import TwitterAPI

api = TwitterAPI(con_key, con_secret, app_key, app_secret)
r = api.request('search/tweets', {'q':'pizza'})
 
time     = []
user     = []
tweet    = []
location = []

for t in r.get_iterator():
    time.append(t['created_at'])
    user.append(t['user'])
    tweet.append(t['text'])
    location.append(t['geo'])

    print(t.keys())
