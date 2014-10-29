# author: Vysakh K.S
from linkedin_new import Linkedin_new
from linkedin_old import Linkedin_old
from scraper import helper

class Linkedin(helper.Helper):
	def __init__(self): pass


	def get_profile(self):
		
		if self.text is not None:
			print self.get_xpath('//div[@class="profile-header"]')
			if self.check_new_profile():
				obj = Linkedin_new()
			elif self.check_old_profile():
				obj = Linkedin_old()
			else:
				print "Invalid url"
				exit()
				return False
			obj.tree = self.text
			return obj
		else:
			return False

