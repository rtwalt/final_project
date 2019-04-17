import requests
import json
import secrets
import api_ow_info
import sqlite3


def make_request(city):
	key = api_ow_info.og_api
	url = "http://api.openweathermap.org/data/2.5/weather?"
	response = requests.get(url + "q=" + city + "&units=imperial" + "&appid=" + key)
	new = json.loads(response.text)

	# if city not in "openweather.txt":
	# 	with open("openweather.txt", 'w') as fd:
	# 		fd.write(response.text)
	# 		fd.close()

	return new

# miami = make_request("Miami")
# newyork = make_request("New York")
# la = make_request("Los Angeles")
# Austin = make_request("Austin")
# aa = make_request("Ann Arbor")


def city_info():

	city = input_city()
	data = make_request(city)
	#print(data.keys())
	new_dict = {}
	new_dict['city'] = city	
	new_dict['temp'] = data['main']["temp"]
	new_dict['humidity'] = data['main']['humidity']
	#new_dict['temp_min'] = data['main']['temp_min']
	#new_dict['temp_max'] = data['main']['temp_max']
	new_dict['wind_speed'] = data['wind']['speed']
	for i in data['weather']:
		new_dict['clouds'] = i['description']
	
	print(new_dict)
	return new_dict
	

	# new_dict['clouds'] = city_info[city]['clouds']
	# new_dict['longitude'] = city_info[city]['coord']['lon']
	# new_dict['latitude'] = city_info[city]['coord']['lat']
	#for i in data['weather']: THIS
		#for k in i: THIS
			#print(i[k])
			# if k == 'id':
			# 	new_dict['weather_id'] = i[k]
			# if k == 'sky':
			# 	new_dict['clouds'] = i[k]
			# if k == 'description': THIS
			# 	new_dict['clouds_description'] = i[k] THIS
			# # if k == 'icon':
			# 	new_dict['icon'] = i[k]
	#new_dict['pressure'] = city_info[city]['main']['pressure']
	#new_dict['type'] = list_cities[city]['sys']['type']
	#new_dict['id'] = list_cities[city]['sys']['id']
	#new_dict['message'] = list_cities[city]['sys']['message']
	#new_dict['country'] = list_cities[city]['sys']['country']
	# new_dict['sunrise'] = city['sys']['sunrise']
	# new_dict['sunset'] = city['sys']['sunset']
	
		
def input_city():
	user = input("Please enter a city name")
	return user

#print(city_info())

def openweather_db():

	try:
		city_weather = city_info()
	
		conn = sqlite3.connect('openweather.db')
		cur = conn.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS Weather(city TEXT, temp REAL, humidity INTEGER , wind_speed REAL, clouds TEXT)')

		city = city_weather['city']
		temp = city_weather['temp']
		humidity = city_weather['humidity']
		wind_speed = city_weather['wind_speed']
		clouds = city_weather['clouds']
		cur.execute('INSERT INTO Weather (city, temp, humidity, wind_speed, clouds) VALUES (?, ?, ?, ?, ?)',
                	(city, temp, humidity, wind_speed, clouds))
	
		conn.commit()
	
	except:
		return "not a valid city"

def main():
	for i in range(19):
		print(openweather_db())

main()

def average_temp(): #calculate this info from the data- most, average, whatever from data set
	pass
	