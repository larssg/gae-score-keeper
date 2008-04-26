from google.appengine.api import users
from google.appengine.ext import db

class Match(db.Model):
	"""A single match"""
	
	player1 = db.StringProperty(required=True)
	player2 = db.StringProperty(required=True)
	score1 = db.IntegerProperty(required=True)
	score2 = db.IntegerProperty(required=True)
	played_at = db.DateTimeProperty(auto_now_add=True)
	created = db.DateTimeProperty(auto_now_add=True)
	last_modified = db.DateTimeProperty(auto_now=True)
	
	def winner(self):
		if self.score1 > self.score2:
			return self.player1
		else:
			return self.player2
			
class Account(db.Model):
	email = db.StringProperty(required=True)
	name = db.StringProperty(required=True)