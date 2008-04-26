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

		template_values = self.default_template_values('dashboard')
		template_values['matches'] = matches
		self.render_default_template('dashboard', 'index', template_values)

def main():
	application = webapp.WSGIApplication(
		[('/', Dashboard)],
		debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
	main()