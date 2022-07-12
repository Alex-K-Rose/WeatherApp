from tkinter import *
from tkinter import ttk
from apiWeather import *
import datetime

root = Tk()
root.geometry("1000x530")
root.title("Weather App")

def func_run():
    if (len(cityVar.get()) != 0 and len(stateVar.get()) != 0):
        funcRes = getAll(cityVar.get(), stateVar.get())

    elif len(cityVar.get()) != 0:
        funcRes = getAll(cityVar.get())

    temp = funcRes[0]['list'][0]['main']['temp']
    feels_like = funcRes[0]['list'][0]['main']['feels_like']
    pressure = funcRes[0]['list'][0]['main']['pressure']
    humidity = funcRes[0]['list'][0]['main']['humidity']
    sunrise = (datetime.datetime.fromtimestamp(funcRes[0]['city']['sunrise'])).time()
    sunset = (datetime.datetime.fromtimestamp(funcRes[0]['city']['sunset'])).time()
    description = funcRes[0]['list'][0]['weather'][0]['description']

    #timezone = funcRes[0]['city']['timezone']
    weather = f"\nWeather of: {cityVar.get()}\nTemperature (Farenheight): {temp}°\nFeels like: {feels_like}°\nPressure: {pressure} hPa\nHumidity: {humidity}\nInfo: {description}"
    sun = f"\nSunrise at {sunrise}\n\n\nSunset at {sunset}"
    moon = f"\n\n{funcRes[1]}"

    weather_box.delete('1.0', END)
    weather_box.insert(INSERT, weather)

    sun_box.delete('1.0', END)
    sun_box.insert(INSERT, sun)

    moon_box.delete('1.0', END)
    moon_box.insert(INSERT, moon)

def show_sun():
    sun_box.place(y=120, x=5)
    sunButton.configure(text="Hide", command=hide_sun)

def hide_sun():
    sun_box.delete('1.0', END)
    sun_box.place_forget()
    sunButton.configure(text="Show", command=show_sun)

def show_moon():
    moon_box.place(y=120, x=5)
    moonButton.configure(text="Hide", command=hide_moon)

def hide_moon():
    moon_box.delete('1.0', END)
    moon_box.place_forget()
    moonButton.configure(text="Show", command=show_moon)

cityVar = StringVar(root)
stateVar = StringVar(root)

search = Label(root, text='Location Search:', font='Times 12').place(y=10)

searchBarCity = Label(root, text='City', font='Times 12').place(y=30)
searchBarState = Label(root, text='State (if relevant)', font='Times 12').place(y=30, x=200)

enterLoc = Entry(root, textvariable=cityVar, width=24, font='Times 12').place(x=5, y=50)  # entry field
enterState = Entry(root, textvariable=stateVar, width=5, font='Times 12').place(x=225, y=50)  # entry field

weathButton = Button(root, text = "Search", command=func_run, font='Times 12')
weathButton.place(x=305, y=49)

sunButton = Button(root, text = "Hide", command=hide_sun, font='Times 12')
sunButton.place(y=83, x=148)

moonButton = Button(root, text = "Hide", command=hide_moon, font='Times 12')
moonButton.place(y=83, x=415)

weather_curr = Label(root, text = "City Weather", font = 'Times 12').place(y=320, x=10)
weather_box = Text(root, width=100, height =10)
weather_box.config(state=NORMAL)
weather_box.place(y=350, x=10)

sun_curr = Label(root, text = "City Sunrise & Sunset", font = 'Times 12').place(y=95, x=3)
sun_box = Text(root, width=30, height=10)
sun_box.config(state=NORMAL)
sun_box.place(y=120, x=5)

moon_curr = Label(root, text = "City Moonphase", font = 'Times 12').place(y=95, x=305)
moon_box = Text(root, width=30, height=10)
moon_box.config(state=NORMAL)
moon_box.place(y=120, x=305)

root.mainloop()