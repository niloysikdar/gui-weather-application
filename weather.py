from tkinter import *
from tkinter import messagebox
import PIL.Image
import PIL.ImageTk
from configparser import ConfigParser
import requests


root = Tk()
root.title("Current weather app by @Niloy Sikdar")
root.geometry("420x550")
root.resizable(0, 0)
root.iconbitmap(r'icons/icon.ico')
root.config(bg="#52e0eb")

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config["api_key"]["key"]

def get_weather(city):
        result = requests.get(url.format(city, api_key))
        json = result.json()
        global country , weather , icon , temp_celcius , tempMin , tempMax , humidityVal , windval
        city = json["name"]
        country = json["sys"]["country"]
        weather = json["weather"][0]["description"]
        icon = json["weather"][0]["icon"]
        temp_kelvin = json["main"]["temp"]
        temp_celcius = round(float(temp_kelvin - 273.15), 2)
        tempMin = round((float((json["main"]["temp_min"]) - 273.15)), 2)
        tempMax = round((float((json["main"]["temp_max"]) - 273.15)), 2)
        humidityVal = json["main"]["humidity"]
        windval = json["wind"]["speed"]


def update_weather(city):
    button.config(state=DISABLED)
    try:
        get_weather(city)
        locationLabel.config(text="Location : "+city+" , "+country+"\n"+"Current weather : "+weather)

        im = PIL.Image.open("icons/{}.png".format(icon))
        photo = PIL.ImageTk.PhotoImage(im)
        imagelabel.config(image=photo)
        imagelabel.image = photo

        tempLabel.config(text="Current Temperature : "+ str(temp_celcius) +"°C")
        maxminTemp.config(text="Minimun Temperature : "+ str(tempMin) +"°C" +"\n"+
                                "Maximum Temperature : "+ str(tempMax) +"°C")

        humidity.config(text="Humidity : "+ str(humidityVal) + "%")
        windSpeed.config(text="Windspeed : "+ str(windval) +" m/s")

    except:
        messagebox.showerror("Error message", "Please enter correct city or check your internet connection !")

    button.config(state=ACTIVE)



entryLabel = Label(root, text="Enter the city :", bg="#52e0eb", font="10")
entryLabel.pack(pady=(15,5))

entryBox = Entry(root, width=25, borderwidth = 5, font=4)
entryBox.pack(padx=50, pady=(0,10), ipadx=3, ipady=3)

button = Button(root, text="Get weather", borderwidth=4, bg="#14f00c", activebackground="#fc6a6a", font=("Sans Serif", 12), command=lambda: update_weather(entryBox.get()))
button.pack(pady=10, ipadx=5, ipady=5)

locationLabel = Label(root, bg="#52e0eb", font=("Helvetica",15))
locationLabel.pack(pady=(10,5))

imagelabel = Label(root, bg="#52e0eb")
imagelabel.pack()

tempLabel = Label(root, bg="#52e0eb", font=("Courier", 12))
tempLabel.pack()

maxminTemp = Label(root, bg="#52e0eb", font=("Courier", 12))
maxminTemp.pack()

humidity = Label(root, bg="#52e0eb", font=("Courier", 12))
humidity.pack()

windSpeed = Label(root, bg="#52e0eb", font=("Courier", 12))
windSpeed.pack()

author = Label(root, text="By @Niloy Sikdar", bg="#52e0eb", font=("Times", "15", "bold italic"))
author.pack(side=BOTTOM, pady=5)


root.mainloop()