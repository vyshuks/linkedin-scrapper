# Author: vysakh k.s
# for testing only..
import requests
import randomua
from linkedin import Linkedin
from pymongo import MongoClient
connection = MongoClient("localhost", 27017)  # create connection change port no if different
db = connection["linkedin"]   # select DB
profiles = db["profiles"]  # select collection


print "Input the linkedin url to scrap:"

url  = raw_input()

l = Linkedin()
print requests.get( url , headers = {'User-Agent': randomua.getUserAgent()} ).text
l.text = requests.get( url , headers = {'User-Agent': randomua.getUserAgent()} )
linkedin = l.get_profile()
if linkedin:
	profiles.insert(linkedin.to_json())



