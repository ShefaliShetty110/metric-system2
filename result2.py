import flask, flask.views,twitter
import sys,cgi
import tweepy
import os
import oauth2 #.oauth2 as oauth2
app = flask.Flask(__name__)
# Don't do this!
app.secret_key = "bacon"

class View(flask.views.MethodView):
    def get(self):
	return flask.render_template('home.html')
    
    def post(self):
	log=str(flask.request.form['login'])
	CONSUMER_KEY = 'TroS6jwSabIDTsJt6cu2g'
	CONSUMER_SECRET = 'dvL7ElBM8xTO8bh6XVHlsWQ78tWSmiM3E5PPLrm0A'
	ACCESS_KEY = '126263523-Vj2Rj7RcNjzFa71nRG7FUsdTIIkSfAaLKHzLO8YA'
	ACCESS_SECRET = '9orpHsbfGpFfEDeAVWZrQpEb1JYKdILgVeErKXSi1cs'
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	#print [ u.name for u in user]
	user = tweepy.api.get_user(log)
	count = user.followers_count
	#return flask.render_template(st)
	return flask.render_template('next2.html',user=user) 

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST','SELF'])

app.debug = True
app.run()