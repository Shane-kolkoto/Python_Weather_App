import requests
from pprint import pprint


city = input("Please enter city")
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ad1afec188a74ee6ddf2c04804728b4f&units=metric'.format(city)

res = requests.get(url)

data = res.json()

#Tempreture
temp = data['main']['temp']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']
humidity = data['main']['humidity']

#Wind speed
wind_speed = data['wind']['speed']

#Clouds
clouds = data['clouds']['all']


print(temp)
print(temp_min)
print(temp_max)
