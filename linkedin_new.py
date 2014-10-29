# Author: Vysakh K.S
# Module for scapping new Linkedin profiles
from scraper import helper

class Linkedin_new(helper.Helper):
	def __init__(self):
		super(Linkedin_new, self).__init__()

	def name(self):
		"""
		Return name of the profile

		"""
		return self.sanitize(self.get_xpath('//span[@class="full-name"]/text()'))



	def current_designation(self):
		"""
		Return current designation
		"""
		return self.sanitize(self.get_xpath('//*[@id="headline"]/p/text()'))


	def current_location(self):
		"""
		Return current location
		"""
		return self.sanitize(self.get_xpath('//dd/span/text()'))

	def current_industry(self):
		"""
		Return current industry
		"""
		return self.sanitize(self.get_xpath('//dd[@class="industry"]/text()'))

	def experience(self):
		"""
		Return Experience details
		"""
		count = int(self.get_xpath('count(//div[@id="background-experience"]/div[contains(@id, "experience-")])'))
		details = []
		for i in range(1, count+1):
			data = {}
			data['designation'] = self.sanitize(self.get_xpath('//div[@id="background-experience"]/div[%s]/div//h4/text()' % i))
			data['company'] = self.sanitize(self.get_xpath('//div[@id="background-experience"]/div[%s]/div//h5[2]/a/text()' % i))
			data['company_url'] = self.sanitize(self.get_xpath('//div[@id="background-experience"]/div[%s]/div//h5[2]/a/@href' % i))
			data['company_img_url'] = self.sanitize(self.get_xpath('//div[@id="background-experience"]/div[%s]/div//img/@src' % i))
			data['area'] = self.sanitize(self.get_xpath('//div[@id="background-experience"]/div[%s]/div//span[@class="locality"]/text()' % i))
			from_dates = self.sanitize(self.get_xpath('//div[@id="background-experience"]/div[%s]/div//span[@class="experience-date-locale"]/time[1]/text()' % i))
			if from_dates:
				data['from_month'] , data['from_year'] = from_dates.split()
			else:
				data['from_month'] = data['from_year'] = None
			to_dates = self.sanitize(self.get_xpath('//div[@id="background-experience"]/div[%s]/div//span[@class="experience-date-locale"]/time[2]/text()' % i))
			if to_dates:
				data['to_year'] , data['to_month'] = to_dates.split()
			else:
				data['to_year'] = data['to_month'] = None, 'Present'
			details.append( data )

		return details

	def education(self):
		"""
		Return Education details
		"""

		count = int(self.get_xpath('count(//div[@id="background-education"]/div[contains(@id, "education-")])'))
		details = []
		for i in range(1, count+1):
			data = {}
			data['degree'] = self.sanitize(self.get_xpath('//div[@id="background-education"]/div[%s]/div//span[@class="degree"]/text()' % i))
			data['major'] = self.sanitize(self.get_xpath('//div[@id="background-education"]/div[%s]/div//span[@class="major"]/text()' % i))
			data['university'] = self.sanitize(self.get_xpath('//div[@id="background-education"]/div[%s]/div//h4/a/text()' % i))
			data['university_url'] = self.sanitize(self.get_xpath('//div[@id="background-education"]/div[%s]/div//h4/a/@href' % i))
			data['university_img_url'] = self.sanitize(self.get_xpath('//div[@id="background-education"]/div[%s]/div//img/@src' % i))
			from_dates = self.sanitize(self.get_xpath('//div[@id="background-education"]/div[%s]/div//span[@class="education-date"]/time[1]/text()' % i))
			if from_dates:
				try:
					data['from_month'] , data['from_year'] = from_dates.split()
				except ValueError:
					data['from_year'], data['from_month'] = from_dates, None
			else:
				data['from_month'] = data['from_year'] = None
			to_dates = self.sanitize(self.get_xpath('//div[@id="background-education"]/div[%s]/div//span[@class="education-date"]/time[2]/text()' % i))
			if to_dates:
				try:
					data['to_year'] , data['to_month'] = to_dates.split()
				except ValueError:
					data['to_year'], data['to_month'] = to_dates, None
			else:
				data['to_year'] = data['to_month'] = None
			details.append(data)

		return details

	def project(self):
		"""
		Return Project details
		"""
		count = int(self.get_xpath('count(//div[@id="background-projects"]/div[contains(@id, "project-")])'))
		details = []
		for i in range(1, count+1):
			data = {}
			data['title'] = self.sanitize(self.get_xpath('//div[@id="background-projects"]/div[%s]//h4/text()' % i))
			data['desc'] = self.sanitize(self.get_xpath('//div[@id="background-projects"]/div[%s]//p[@class="description"]/text()' % i))
			team_members = self.get_xpath('//div[@id="background-projects"]/div[%s]//dd[@class="associated-endorsements"]/ul[1]/li/a/text()' % i)
			team_members_url = self.get_xpath('//div[@id="background-projects"]/div[%s]//dd[@class="associated-endorsements"]/ul[1]/li/a/@href' % i)
			teams = []
			map(lambda name, url: teams.append({'name': name, 'pub_url': url}), team_members, team_members_url)
			data['team_members'] = teams
			from_dates = self.sanitize(self.get_xpath('//div[@id="background-projects"]/div[%s]/div//span[@class="projects-date"]/time[1]/text()' % i))
			if from_dates:
				data['from_month'] , data['from_year'] = from_dates.split()
			else:
				data['from_month'] = data['from_year'] = None
			to_dates = self.sanitize(self.get_xpath('//div[@id="background-projects"]/div[%s]/div//span[@class="projects-date"]/time[2]/text()' % i))
			if to_dates:
				data['to_year'] , data['to_month'] = to_dates.split()
			else:
				data['to_year'] , data['to_month'] = None , 'Present'
			details.append(data)
		return details

	def skills(self):
		"""
		Return Skills
		"""
		return self.get_xpath('//span[@class="endorse-item-name-text"]/text()')

	def course(self):
		"""
		Return Course details
		"""
		count = int(self.get_xpath('count(//div[@id="background-courses"]/div[contains(@id, "courses")])'))
		details = []
		for i in range(1, count+1):
			data = {}
			data['name'] = self.sanitize(self.get_xpath('//div[@id="background-courses"]/div[%s]//h4/text()' % i))
			data['org']  = self.sanitize(self.get_xpath('//div[@id="background-courses"]/div[%s]//li/text()' % i))
			from_dates = self.sanitize(self.get_xpath('//div[@id="background-courses"]/div[%s]/div//span[@class="courses-date"]/time[1]/text()' % i))
			if from_dates:
				data['from_month'] , data['from_year'] = from_dates.split()
			else:
				data['from_month'] = data['from_year'] = None
			to_dates = self.sanitize(self.get_xpath('//div[@id="background-projects"]/div[%s]/div//span[@class="courses-date"]/time[2]/text()' % i))
			if to_dates:
				data['to_year'] , data['to_month'] = to_dates.split()
			else:
				data['to_year'] = data['to_month'] = None

			details.append(data)
		return details


	def interests(self):
		"""
		Return Interests
		"""
		return self.get_xpath('//ul[@class="interests-listing"]/li/text()')

	def groups(self):
		"""
		Return Groups
		"""
		names = self.get_xpath('//p[@class="groups-name"]/a/img/@alt')
		imgs = self.get_xpath('//p[@class="groups-name"]/a/img/@src')
		urls = self.get_xpath('//p[@class="groups-name"]/a[1]/@href')
		details = []
		map(lambda name,img,url: details.append({'name': name, 'group_img': img, 'group_url': 'http://www.linkedin.com'+url}), names,imgs,urls)
		return details

	def profile_img_url(self):
		return self.get_xpath('//div[@class="profile-picture"]/img/@src')

	def to_json(self):
		data = {
		'name': self.name(),
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

