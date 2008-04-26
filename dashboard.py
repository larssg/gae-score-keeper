import wsgiref.handlers
import os
import sys
import string

from google.appengine.ext import webapp
from models import *
from scorekeepr import *

class Dashboard(ScoreKeeper):
	def get(self):
		matches = Match.gql("ORDER BY played_at DESC LIMIT 10")

		template_values = self.default_template_values()
		template_values['matches'] = matches
		self.render_default_template('dashboard', 'index', template_values)
		
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
		[('/', Dashboard)],
		debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
	main()