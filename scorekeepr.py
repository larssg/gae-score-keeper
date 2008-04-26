import wsgiref.handlers
import os
import sys
import string

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from models import *

class MainPage(webapp.RequestHandler):
	template_path = os.path.join(os.path.dirname(__file__), 'templates', 'main.html')
	
	def get(self):
		matches = Match.gql("ORDER BY played_at DESC LIMIT 10")
		
		template_values = {
			'matches' : matches,
			'mainContentClass': 'mainContent'
      	}
		self.response.out.write(template.render(MainPage.template_path, template_values))
		
	def post(self):
		match = Match(
			player1 = self.request.get('player1'),
			player2 = self.request.get('player2'),
			score1 = string.atoi(self.request.get('score1')),
			score2 = string.atoi(self.request.get('score2')))
		match.put()
		
		self.redirect('/')

def main():
	application = webapp.WSGIApplication(
		[('/', MainPage)],
		debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
	main()