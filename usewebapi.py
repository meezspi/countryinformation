import webapp2
from google.appengine.api import urlfetch

import StringIO
import csv

urlb = "https://restcountries.eu/rest/v2/name/"

class MainPage(webapp2.RequestHandler):
    def get(self):
	self.response.write('<html><body><h1>Country Information</h1>')
	self.response.write(""" <hr> <form method="post">
	Enter the country NAME:
	<input type="textarea" name="ecountry"></input>
	<input type="submit"></input>
	</form>""")
	self.response.write('</body></html>')
	
    def post(self):
	symbol_entered = self.request.get('ecountry')
	url = urlb + symbol_entered
	whitespace = "%20"
	result = urlfetch.fetch(str(url).replace(" ",whitespace))
	if result.status_code == 200:
	    # get the reply contents from the Web Service Server
	    sresult = str(result.content)
	    # Split the string in CSV into pieces
	    s = StringIO.StringIO(sresult)
	    myreader = csv.reader(s, delimiter=',')
	    for row in myreader:
	        self.response.write('<html><body>Country: ')
		l = row[0].split('"')[3]
		m = row[5].split('"')[1]
		for i in range(0,len(row)-1):
		    if row[i].split(':')[0] == "population":
	                n = row[i].split(':')[1]
	        self.response.write(' <b> %s </b>' % l)
	        self.response.write('<p> Capital: <b> %s </b>' % m)
		self.response.write('<p> Population: <b> %s </b>' % n)
	        self.response.write('</body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

