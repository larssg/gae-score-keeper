import wsgiref.handlers
import os
import sys
import string

from google.appengine.ext import webapp
from models import *
from scorekeepr import *

class AccountPage(ScoreKeeper):
	def get(self):
		template_values = self.default_template_values()
		
		user = users.get_current_user()
		account = Account.gql("WHERE email = :email", email = user.email()).get()
		if not account:
			account = Account(email = user.email(), name = user.nickname())
			account.put()
		
		template_values['account'] = account
		self.render_default_template('account', 'edit', template_values)
		
	def post(self):
		user = users.get_current_user()
		
		account = Account.gql("WHERE email = :email", email = user.email()).get()
		account.name = self.request.get('name')
		account.put()
		
		self.redirect('/account')

def main():
	application = webapp.WSGIApplication(
		[('/account', AccountPage)],
		debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
	main()