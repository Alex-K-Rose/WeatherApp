from tkinter import *
from tkinter import ttk
from apiWeather import *
import datetime
from PIL import Image, ImageTk

root = Tk()
root.geometry("1000x530")
root.title("Weather App")

sun_hs = 1
ms_hs = 1
moon_hs = 1

def get_weather_details(weather_day):
    temp = weather_day['main']['temp']
    feels_like = weather_day['main']['feels_like']
    pressure = weather_day['main']['pressure']
    humidity = weather_day['main']['humidity']
    description = weather_day['weather'][0]['description']

    weather_string = f"\nWeather of:{cityVar.get()}\nTemperature (F):{temp}°\nFeels like: {feels_like}°\nPressure:{pressure} hPa\nHumidity:{humidity}\nInfo:{description}\n"
    return weather_string

def failed_weather_details():
    weather_fail = "Could not Retrieve Location Details"
    sun_fail = "Could not Retrieve Location Details"
    moon_fail = "Could not Retrieve Location Details"
    milkshake_fail = "Could not Retrieve Location Details"

    weather_box.delete('1.0', END)
    weath_box_inserts(weather_fail)

    moon_box.delete('1.0', END)
    moon_box.insert(INSERT, moon_fail)

    sun_box.delete('1.0', END)
    sun_box.insert(INSERT, sun_fail)

    milkshake_box.delete('1.0', END)
    milkshake_box.insert(INSERT, milkshake_fail)

def get_weather_img(description):
    global weath_img
    if description.find("clear"):
        weath_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/weather_icon/clear.png")

    elif description.find("few"):
        weath_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/weather_icon/partly.png")

    elif description.find("scattered"):
        weath_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/weather_icon/scattered.png")

    elif description.find("broken"):
        weath_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/weather_icon/brokenclouds.png")

    elif description.find("shower"):
        weath_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/weather_icon/showerrain.png")

    elif description.find("rain"):
        weath_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/weather_icon/rain.png")

    elif description.find("thunderstorm"):
        weath_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/weather_icon/thunder.png")

    elif description.find("snow"):
        weath_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/weather_icon/snow.png")

    elif description.find("mist"):
        weath_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/weather_icon/mist.png")

    return weath_img

def get_moon_img(phase):
    global moon_img
    if phase.find("Gibbous") != -1:
        moon_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/moon_icon/waning-gibbous.png")

    elif phase.find("Crescent") != -1:
        moon_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/moon_icon/waning-crescent.png")

    elif phase.find("New") != -1:
        moon_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/moon_icon/new-moon.png")

    elif phase.find("Full") != -1:
        moon_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/moon_icon/full-moon.png")

    elif phase.find("First") != -1:
        moon_img = PhotoImage(file="/home/clean_skulll/PycharmProjects/WeatherApp/moon_icon/first-quarter.png")

    return moon_img

def get_sun(city_sun):
    sunrise=(datetime.datetime.fromtimestamp(city_sun)).time()
    sunset = (datetime.datetime.fromtimestamp(city_sun)).time()
    sun_string = f"\nSunrise at {sunrise}\n\n\nSunset at {sunset}"
    return sun_string

def setup_weather_items(weather_body):
    day0_details = get_weather_details(weather_body[0])
    day1_details = get_weather_details(weather_body[1])
    day2_details = get_weather_details(weather_body[2])
    day3_details = get_weather_details(weather_body[3])
    day4_details = get_weather_details(weather_body[4])

    global day0_img
    day0_img = get_weather_img(weather_body[0]['weather'][0]['description'])
    global day1_img
    day1_img = get_weather_img(weather_body[1]['weather'][0]['description'])
    global day2_img
    day2_img = get_weather_img(weather_body[2]['weather'][0]['description'])
    global day3_img
    day3_img = get_weather_img(weather_body[3]['weather'][0]['description'])
    global day4_img
    day4_img = get_weather_img(weather_body[4]['weather'][0]['description'])

    return [day0_details, day1_details, day2_details, day3_details, day4_details]

def weath_box_inserts(weath_descrips):
    weather_box.delete('1.0', END)

    weather_box.image_create("end", image=day0_img)
    weather_box.insert(INSERT, weath_descrips[0])

    weather_box.image_create("end", image=day1_img)
    weather_box.insert(INSERT, weath_descrips[1])

    weather_box.image_create("end", image=day2_img)
    weather_box.insert(INSERT, weath_descrips[2])

    weather_box.image_create("end", image=day3_img)
    weather_box.insert(INSERT, weath_descrips[3])

    weather_box.image_create("end", image=day4_img)
    weather_box.insert(INSERT, weath_descrips[4])

def rem_box_inserts(phase, the_moon, sun, ms_details, ms_loc):
    moon_box.delete('1.0', END)
    moon_box.image_create("end", image=the_moon)
    moon_box.insert(INSERT, phase)

    sun_box.delete('1.0', END)
    sun_box.insert(INSERT, sun)

    milkshake_box.delete('1.0', END)
    milkshake_box.insert(INSERT, ms_details)
    milkshake_box.insert(INSERT, ms_loc)

def func_run():
    if (len(cityVar.get()) != 0 and len(stateVar.get()) != 0):
        funcRes = getAll(cityVar.get(), stateVar.get())

    elif len(cityVar.get()) != 0:
        funcRes = getAll(cityVar.get())

    if type(funcRes[0]) != str:
        weath_descrips = setup_weather_items(funcRes[0]['list'])

        phase = f"\n\n{funcRes[1]}"
        the_moon=get_moon_img(phase)

        sun = get_sun(funcRes[0]['city']['sunrise'])

        ms_loc = f"\n{funcRes[3]['loc1']}\n{funcRes[3]['loc2']}\n{funcRes[3]['loc3']}"
        ms_details = f"\n\n{funcRes[2][2:-1]}"

        weath_box_inserts(weath_descrips)
        rem_box_inserts(phase, the_moon, sun, ms_details, ms_loc)

    else:
        failed_weather_details()

def hide_show_sun():
    global sun_hs

    if sun_hs == 1:
        sun_box.place_forget()
        sun_curr.place_forget()
        sun_hs = 0

    elif sun_hs == 0:
        sun_box.place(y=120, x=275)
        sun_curr.place(y=100, x=280)
        sun_hs = 1

def hide_show_moon():
    global moon_hs

    if moon_hs == 1:
        moon_box.place_forget()
        moon_curr.place_forget()
        moon_hs = 0

    elif moon_hs == 0:
        moon_box.place(y=350, x=275)
        moon_curr.place(y=330, x=280)
        moon_hs = 1

def hide_show_milkshake():
    global ms_hs

    if ms_hs == 1:
        milkshake_box.place_forget()
        milkshake_curr.place_forget()
        ms_hs = 0

    elif ms_hs == 0:
        milkshake_box.place(y=580, x=275)
        milkshake_curr.place(y=560, x=280)
        ms_hs = 1

cityVar = StringVar(root)
stateVar = StringVar(root)

#Search Bar Declarations, Details, and Placement
search = Label(root, text='Location Search:', font='Times 12').place(y=10)

searchBarCity = Label(root, text='City', font='Times 12').place(y=30)
searchBarState = Label(root, text='State (if relevant)', font='Times 12').place(y=30, x=200)

enterLoc = Entry(root, textvariable=cityVar, width=24, font='Times 12').place(x=5, y=50)  # entry field
enterState = Entry(root, textvariable=stateVar, width=5, font='Times 12').place(x=225, y=50)  # entry field

weathButton = Button(root, text = "Search", command=func_run, font='Times 12')
weathButton.place(x=305, y=49)

#Text Box Labels, Declarations, Details, and Placement
weather_curr = Label(root, text = "City Weather", font = 'Times 12').place(y=95, x=10)
weather_box = Text(root, width=30, height =200)
weather_box.config(state=NORMAL)
weather_box.place(y=120, x=10)

sun_curr = Label(root, text = "City Sunrise & Sunset", font = 'Times 12', state=NORMAL)
sun_curr.place(y=100, x=280)
sun_box = Text(root, width=30, height=10)
sun_box.config(state=NORMAL)
sun_box.place(y=120, x=275)

moon_curr = Label(root, text = "City Moonphase", font = 'Times 12', state=NORMAL)
moon_curr.place(y=330, x=280)
moon_box = Text(root, width=30, height=10)
moon_box.config(state=NORMAL)
moon_box.place(y=350, x=275)

milkshake_curr = Label(root, text = "Milkshake Conditions", font = 'Times 12', state=NORMAL)
milkshake_curr.place(y=560, x=280)
milkshake_box = Text(root, width=30, height=10)
milkshake_box.config(state=NORMAL)
milkshake_box.place(y=580, x=275)

#Settings Declarations, Details, and Placement
bar = Menu(root)
root.config(menu=bar)

file = Menu(bar, tearoff=0)

settings_menu = Menu(file, tearoff=0)

settings_menu.add_checkbutton(label="Hide Sun Results", command=hide_show_sun, onvalue=1, offvalue=0)
settings_menu.add_checkbutton(label="Hide Moon Results", command=hide_show_moon, onvalue=1, offvalue=0)
settings_menu.add_checkbutton(label="Hide Milkshake Results", command=hide_show_milkshake, onvalue=1, offvalue=0)

file.add_cascade(label='Settings', menu=settings_menu)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

bar.add_cascade(label='File', menu=file, underline=0)

root.mainloop()