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
	response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=836d82e650676a734c1f9fe9449f3beb")
	data = response.json()
	print(data)

make_request()


