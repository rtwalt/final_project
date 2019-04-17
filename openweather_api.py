import requests
import json
import secrets
import api_ow_info

def make_requests_with_caching(url, ident, key):
	#or params['q']
	try:
		cache_file = open('cache-openweather.json', 'r')
		cache_contents = cache_file.read()
		CACHE_DICTION = json.loads(cache_contents)
		cache_file.close()
	except:
		CACHE_DICTION = {}
	if ident in CACHE_DICTION:
		return CACHE_DICTION[ident]
	else:
		response = requests.get(url + "q=" + ident + "&APPID=" + key)
		CACHE_DICTION[ident] = response.text
		JSONdumps = json.dumps(CACHE_DICTION)
		f = open('cache-openweather.json', 'w')
		f = f.write(JSONdumps)
		f.close()
	return CACHE_DICTION[ident]

def make_request(city):
	#q = city name or get city id
	#response = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=miami&id=524901&APPID=836d82e650676a734c1f9fe9449f3beb")
	#params = {}
	#params['q'] = city
	ident = city
	#params['id'] = id_
	#params['APPID'] = api_ow_info.og_api
	key = api_ow_info.og_api
	url = "http://api.openweathermap.org/data/2.5/weather?"
	#data = {"q": city, "id": "524901", "APPID":"836d82e650676a734c1f9fe9449f3beb"}
	response = make_requests_with_caching(url, ident = ident, key = key)
	data = json.loads(response)
	return data

# miami = make_request("Miami")
# newyork = make_request("New York")
# la = make_request("Los Angeles")
# Austin = make_request("Austin")
# aa = make_request("Ann Arbor")


def city_info(city):
	fn = 'cache-openweather.json'
	with open(fn, 'r') as f:
		data = json.loads(f)
	city = make_request(city)
	list1 = city_info["list"]
	for l in list1:

# def average_temp(city):
# 	#city_info = 
# 	pass







