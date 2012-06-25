import flask, flask.views,twitter
import os
import oauth2 #.oauth2 as oauth2
app = flask.Flask(__name__)
# Don't do this!
app.secret_key = "bacon"

class View(flask.views.MethodView):
    def get(self):
		return flask.render_template('home.html')
    
    def post(self):
        #return str(flask.request.form['login'])
		#pass1 = str(flask.request.form['password'])
		#log = str(flask.request.form['login'])
		log = eval(flask.request.form['login'])
		auth=oauth2.Token(log, '9orpHsbfGpFfEDeAVWZrQpEb1JYKdILgVeErKXSi1cs' , 'dvL7ElBM8xTO8bh6XVHlsWQ78tWSmiM3E5PPLrm0A', 'TroS6jwSabIDTsJt6cu2g')
		t = twitter(auth)
        #flask.flash(result)
    	#print auth
        #consumer_key = "TroS6jwSabIDTsJt6cu2g"
        #consumer_secret = "dvL7ElBM8xTO8bh6XVHlsWQ78tWSmiM3E5PPLrm0A"
        #consumer = oauth2.Consumer(consumer_key, consumer_secret)
        #access_token_url = 'https://api.twitter.com/oauth/access_token'
        #token = oauth2.Token('126263523-Vj2Rj7RcNjzFa71nRG7FUsdTIIkSfAaLKHzLO8YA','9orpHsbfGpFfEDeAVWZrQpEb1JYKdILgVeErKXSi1cs')
        #token.set_verifier(oauth2_verifier)
        #client = oauth2.Client(consumer, token)
        #resp, content = client.request(access_token_url, "POST")
        #access_token = dict(urlparse.parse_qsl(content))
        #print "Access Token:"
        #print "    - oauth_token        = %s" % access_token['126263523-Vj2Rj7RcNjzFa71nRG7FUsdTIIkSfAaLKHzLO8YA']
        #print "    - oauth_token_secret = %s" % access_token['9orpHsbfGpFfEDeAVWZrQpEb1JYKdILgVeErKXSi1cs']
        #print "You may now access protected resources using the access tokens above."
		#api = twitter.Api('TroS6jwSabIDTsJt6cu2g', 'dvL7ElBM8xTO8bh6XVHlsWQ78tWSmiM3E5PPLrm0A', '126263523-Vj2Rj7RcNjzFa71nRG7FUsdTIIkSfAaLKHzLO8YA','9orpHsbfGpFfEDeAVWZrQpEb1JYKdILgVeErKXSi1cs')
		print t.VerifyCredentials() 
	
    
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()
