# Author: Vysakh K.S
# Module for scrpping details from old linkedin profile
from scraper import helper

class Linkedin_old(helper.Helper):
	def __init__(self): pass
		

	def name(self):
		"""
		Return name of the profile

		"""
		return self.sanitize(self.get_xpath('//title/text()')).split('|')[0].strip()


	def current_designation(self):
		"""
		Return current designation
		"""
		return self.sanitize(self.get_xpath('//dd[@class="summary-current"]/ul[@class="current"]/li//text()'))
		

	def current_location(self):
		"""
		Return current location
		"""
		return self.sanitize(self.get_xpath('//dd/span/text()'))
		

	def current_industry(self):
		"""
		Return current industry
		"""
		return  self.sanitize(self.get_xpath('//dd[@class="industry"]/text()'))
		

	def experience(self):
		"""
		Return Experience details
		"""
		details = []
		for scope in self.get_xpath('//div[contains(@class, "experience")]'):
			data = {}
			data['designation'] = self.sanitize(scope.xpath('./div[@class="postitle"]/h3/span/text()'))
			data['company'] = self.sanitize(scope.xpath('./div[@class="postitle"]/h4//span/text()'))
			data['company_url'] = self.sanitize(scope.xpath('./div[@class="postitle"]/h4//a/@href'))
			data['company_img_url'] = None
			data['area'] = self.sanitize(scope.xpath('./p//span[@class="location"]/text()'))
			from_dates  = self.sanitize(scope.xpath('./p//abbr[@class="dtstart"]/text()'))
			if from_dates:
				try:
					data['from_month'], data['from_year'] =from_dates.split()
				except ValueError:
					data['from_year'], data['from_month'] = from_dates, None
					
			else:
				data['from_month'] = data['from_year'] = None
			to_dates = self.sanitize(scope.xpath('./p//abbr[@class="dtend"]/text()'))
			if to_dates:
				try:
					data['to_month'] , data['to_year'] = to_dates.split()
				except ValueError:
					data['to_year'], data['to_month'] = to_dates, None
			else:
				data['to_month'] = data['to_year'] = None
			details.append( data )
		return details

	def education(self):
		"""
		Return Education details
		"""
		details = []
		for scope in self.get_xpath('//div[contains(@class, "education vevent")]'):
			data = {}
			data['degree'] = self.sanitize(scope.xpath('./h4[@class="details-education"]//span[@class="degree"]/text()'))
			data['major'] = self.sanitize(scope.xpath('./h4[@class="details-education"]//span[@class="major"]/text()'))
			data['university'] = self.sanitize(scope.xpath('./h3/text()'))
			data['university_url'] = self.sanitize(scope.xpath('./h3/a/@href'))
			data['university_img_url'] = None
			from_dates = self.sanitize(scope.xpath('./p//abbr[@class="dtstart"]/text()'))
			if from_dates:
				data['from_year'] = from_dates.split()
				data['from_month'] = None # month not present
			else:
				data['from_month'] = data['from_year'] = None

			to_year = self.sanitize(scope.xpath('./p//abbr[@class="dtend"]/text()'))
			if to_year:
				data['to_year']  = to_year.split()
				data['to_month'] = None # month not present
			else:
				data['to_year'] = data['to_month'] = None
			details.append(data)
		return details

	def project(self):
		"""
		Return Project details
		"""
		details = []
		for scope in self.get_xpath('//li[contains(@class, "project")]'):
			data = {}
			data['title'] = self.sanitize(scope.xpath('./h3/cite/text()'))
			data['desc'] = self.sanitize(scope.xpath('./div[2]/p/text()'))
			team_members = scope.xpath('./div[1]/a/text()')
			team_members_url = scope.xpath('./div[2]/a/@href')
			teams = []
			map(lambda name, url: teams.append({'name': name, 'pub_url': url}), team_members, team_members_url)
			data['team_members'] = teams
			dates = self.sanitize(scope.xpath('./ul/li/text()')).split('to')
			if dates and len(dates) == 2:
				data['from_month'] , data['from_year'] = self.sanitize(dates[0]).split()
				if self.sanitize(dates[1]) == 'Present':
					data['to_year'] = data['to_month'] = 'Present'
				else:
					data['to_year'] , data['to_month'] = self.sanitize(dates[1]).split() 
			else:
				data['to_year'] = data['to_month'] = data['from_month'] = data['from_year'] = None

			details.append(data)

		return details

	def skills(self):
		"""
		Return Skills
		"""
		return self.sanitize(self.get_xpath('//ol[@class= "skills"]/li/span/text()'), True)

	def course(self):
		"""
		Return Course details
		"""
		return None


	def interests(self):
		"""
		Return Interests
		"""
		interest = self.sanitize(self.get_xpath('//dd[@class="interests"]/p/text()'))
		return interest.split(',')
		

	def groups(self):
		"""
		Return Groups
		"""
		names = self.get_xpath('//ul[@class="groups"]/li/a/img/@alt')
		imgs = self.get_xpath('//ul[@class="groups"]/li/a/img/@src')
		urls = self.get_xpath('//ul[@class="groups"]/li/a/@href')
		details = []
		map(lambda name,img,url: details.append({'name': name, 'group_img': img, 'group_url': 'http://www.linkedin.com'+url}), names,imgs,urls)
		return details

	def profile_img_url(self):
		return self.get_xpath('//div[@id="profile-picture"]/img/@src')

	def summary(self):
		smry = self.get_xpath('//p[@class=" description summary"]//text()')
		smry = [sentence.strip() for sentence in smry]
		return "".join(smry)


	def to_json(self):
		data = {
		'name': self.name(),
		'summary': self.summary(),
		'profile_img_url': self.profile_img_url(),
		'current_designation': self.current_designation(),
		'current_location': self.current_location(),
		'current_industry': self.current_industry(),
		'experience': self.experience(),
		'education': self.education(),
		'project': self.project(),
		'skills': self.skills(),
		'course': self.course(),
		'interests': self.interests(),
		'groups': self.groups()
		}
		return data






