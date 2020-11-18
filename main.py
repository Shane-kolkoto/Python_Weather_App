import tkinter
from tkinter import *
import requests

Weather = Tk()
Weather.title("Weather App")

#Welcome Frame
welcome = Frame(Weather)
welcome.pack(side=TOP)
wel_label = Label(welcome, text="Weather App", font="ariel")
wel_label.pack(side=LEFT)

#City and button
frame = Frame(Weather)
frame.pack(side=TOP)
city = Label(frame, text="Please enter city: ")
city.pack(side=LEFT)
city_entry = Entry(frame)
city_entry.pack(side=LEFT)
search = Button(frame, text="search", bd=2)
search.pack(side=LEFT)

#Displaying info frames
#Temp frame
frame1 = Frame(Weather)
frame1.pack(side=TOP)
temp = Label(frame1, text="tempreture: ")
temp.pack(side=LEFT)
temp_entry = Entry(frame1, bd=2)
temp_entry.pack(side=LEFT)

#Temp Max
frame2 = Frame(Weather)
frame2.pack(side=TOP)
temp_max = Label(frame2, text="Temp (Max): ")
temp_max.pack(side=LEFT)
max_entry = Entry(frame2, bd=2)
max_entry.pack(side=LEFT)


#Temp Min
frame3 = Frame(Weather)
frame3.pack(side=TOP)
temp_min = Label(frame3, text="Temp (Min): ")
temp_min.pack(side=LEFT)
min_entry = Entry(frame3, bd=2)
min_entry.pack(side=LEFT)


#Humidity
frame4 = Frame(Weather)
frame4.pack(side=TOP)
humidity = Label(frame4, text="Humidity: ")
humidity.pack(side=LEFT)
humidity_entry = Entry(frame4, bd=2)
humidity_entry.pack(side=LEFT)


#Wind speed
frame5 = Frame(Weather)
frame5.pack(side=TOP)
speed = Label(frame5, text="Wind Speed: ")
speed.pack(side=LEFT)
speed_entry = Entry(frame5, bd=2)
speed_entry.pack(side=LEFT)


#Clouds
frame6 = Frame(Weather)
frame6.pack(side=TOP)
clouds = Label(frame6, text="Clouds: ")
clouds.pack(side=LEFT)
clouds_entry = Entry(frame6, bd=2)
clouds_entry.pack(side=LEFT)






Weather.geometry('500x500')
Weather.config(bg="light blue")
Weather.mainloop()