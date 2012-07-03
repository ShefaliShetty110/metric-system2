import flask, flask.views,twitter
import sys,cgi
import tweepy
import os
import datetime
import oauth2 #.oauth2 as oauth2
from datetime import timedelta


app = flask.Flask(__name__)
# Don't do this!
app.secret_key = "bacon"

class View(flask.views.MethodView):
    @app.route('/GET')
    def get(self):
        return flask.render_template('home.html')
    @app.route('/POST')
    def post(self):
        log=str(flask.request.form['username'])
        if not log:
            return flask.render_template('error.html',msg="Enter the Username!!")
        else:
            CONSUMER_KEY = 'plRdBYjdicAUbzM5O5zA'
            CONSUMER_SECRET = '4LnBUaGgJqKwYnr64FfZD3PLtm5HwltPN6O7kh9pU'
            ACCESS_KEY = '600746849-bgDXhEn5fUmWlgpMFI61KFvQWbDlp3nLKlRr3uEW'
            ACCESS_SECRET = 'MySpI4OjOkorVaYrp2jnZ2iDTLTnvAYw3l9G0RyB0'
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            try:
                user = tweepy.api.get_user(log)
            except tweepy.error.TweepError:
                return flask.render_template('error.html',msg="Invalid Username!!") 
            max1=0
            now = datetime.datetime.now()
            pqr =  now.date()
            for status in api.user_timeline(user.id):
                abc = status.created_at
                datedff = pqr - abc.date()
                max1=datedff.days
                break
            max2=0
            for a in api.user_timeline(user.id):
                m = a.retweet_count
                if max2 < m:
                    max2 = m
            return flask.render_template('index.html',user=user,api=api,max1=max1,max2=max2) 

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST','SELF'])

app.debug = True
app.run()
