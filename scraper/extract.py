# Author: vysakh k.s
# Core module dealing with xpath query
from lxml import html

class Extract(object):

	def __init__(self):
		self.tree = None
		
	@property
	def text(self):
		"""
		Return the text or html
		"""
		return self.tree

	@text.setter
	def text(self, obj):
		self.tree = html.fromstring( obj.text )

	@text.deleter
	def text(self):
		del self.tree

	def get_xpath(self, xpath):
		"""
		Return xpath query result
		"""
		return self.tree.xpath( xpath )

