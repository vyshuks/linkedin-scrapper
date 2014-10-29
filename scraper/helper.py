from extract import Extract

class Helper(Extract):

	def sanitize(self, text, return_list = False):
		if type(text) is list:
			if len(text) == 1:
				return text[0].strip() if not return_list else [word.strip() for word in text]
			elif len(text) == 0:
				return "" if not return_list else []
			else:
				new_text = [word.strip() for word in text]
				return " ".join(new_text) if not return_list else new_text

		elif text:
			return text.strip()

	def check_new_profile(self):
		if self.get_xpath('//div[@role="main"]'):
			return True
		else:
			return False

	def check_old_profile(self):
		if self.get_xpath('//div[@class="profile-header"]'):
			return True
		else:
			return False

	
	