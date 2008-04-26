import os
import sys
import string

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class ScoreKeeper(webapp.RequestHandler):
	def template_path(self, model, action):
		return os.path.join(os.path.dirname(__file__), 'templates', model, action + '.html')

	def default_template_values(self):
		template_values = {}

		user = users.get_current_user()
		if user:
			template_values['logged_in'] = True
			template_values['nickname'] = user.nickname()
			template_values['email'] = user.email()
			template_values['signout_url'] = users.create_logout_url("/")
		else:
			template_values['logged_in'] = False
			template_values['signin_url'] = users.create_login_url("/")

		template_values['mainContentClass'] = 'mainContent'
		
		return template_values
		
	def render_default_template(self, model, action, template_values):
		self.response.out.write(template.render(self.template_path(model, action), template_values))