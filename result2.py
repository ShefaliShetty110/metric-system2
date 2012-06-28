import flask, flask.views,twitter
import sys,cgi
import tweepy
import os
import datetime
import oauth2 #.oauth2 as oauth2

app = flask.Flask(__name__)
# Don't do this!
app.secret_key = "bacon"

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('backgd.html')
    
    def post(self):
        log=str(flask.request.form['username'])
        CONSUMER_KEY = 'TroS6jwSabIDTsJt6cu2g'
        CONSUMER_SECRET = 'dvL7ElBM8xTO8bh6XVHlsWQ78tWSmiM3E5PPLrm0A'
        ACCESS_KEY = '126263523-Vj2Rj7RcNjzFa71nRG7FUsdTIIkSfAaLKHzLO8YA'
        ACCESS_SECRET = '9orpHsbfGpFfEDeAVWZrQpEb1JYKdILgVeErKXSi1cs'
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        user = tweepy.api.get_user(log)

        max=0
        for a in api.followers_ids(user.id):
            x = tweepy.api.get_user(a)
        if max < x.followers_count :
                max = x.followers_count
        
        now = datetime.datetime.now()
        pqr =  now.date()
     
        for status in api.user_timeline(user.id):
            abc = status.created_at
            datedff = pqr - abc.date()
            break
        max2=0
        for a in api.user_timeline(user.id):
            m = a.retweet_count
            if max2 < m:
                max2 = m
        return flask.render_template('next2.html',user=user,api=api,max=max,datedff=datedff,max2=max2) 

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST','SELF'])

app.debug = True
app.run()
