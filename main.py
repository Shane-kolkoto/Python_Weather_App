import tkinter
from tkinter import *
from tkinter import messagebox
import requests
from configparser import ConfigParser

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ad1afec188a74ee6ddf2c04804728b4f'

def get_weather(city):
    reslts = requests.get(url.format(city, url))
    if reslts:
        json = reslts.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_cel = temp_kelvin - 273.15
        temp_fah = (temp_kelvin-273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_cel, temp_fah, icon, weather)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        Location['text'] = '{}, {}'.format(weather[0], weather[1])
        images['bitmap'] = 'Weather_icons/{}.png'.format(weather[4])
        Temp['text'] = '{:.2f}°C {:2f}°F'.format(weather[2], weather[3])
        weather['text'] = weather[5]
    else:
        messagebox.showerror('Error!', 'Place not found!')


Win = Tk()
Win.title("Weather App")

city_text = StringVar()
city_entry = Entry(Win, textvariable=city_text)
city_entry.pack()

city_lbl = Label(Win, text="Please enter city")
city_lbl.pack()

#buttom
search = Button(Win, text="search", width=12, command=search)
search.pack()

#Location name
Location = Label(Win, text="Location", font=('bold', 20))
Location.pack()

#images
images = Label(Win, bitmap='')
images.pack()

#Temp
Temp = Label(Win, text="Temp")
Temp.pack()

#Weather
Weather = Label(Win, text="Weather")
Weather.pack()

Win.geometry('700x350')
Win.mainloop()