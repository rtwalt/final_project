import requests
import json
import secrets

try:
	cache_file1 = open('cache-openweather.json', 'r')
	cache_contents1 = cache_file1.read()
	CACHE_DICTION1 = json.loads(cache_contents1)
	cache_file1.close()
except:
	CACHE_DICTION1 = {}

def make_request():
	pass
