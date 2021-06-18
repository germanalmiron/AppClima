#Desarrollar un script en Python que consuma datos del clima, 
# actuales o pronostico desde la API https://openweathermap.org/ , 
# a partir del nombre de la ciudad.

#Consume datos desde el nombre de la Ciudad

from tkinter import *
import requests

#API Key
#b934f535e5b642a4b7e70de0c3a5a0e3

#By city name
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def mostrar_respuesta(clima):
    nombre_ciudad = clima["name"]
    desc = clima["weather"][0]["description"]
    temp = clima["main"]["temp"]

    ciudad["text"] = nombre_ciudad
    temperatura["text"] = str(int(temp)) + "°C"
    descripcion["text"] = desc

def clima(ciudad):
    API_Key = "b934f535e5b642a4b7e70de0c3a5a0e3"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {"APPID" : API_Key, "q": ciudad, "units": "metric", "lang": "es" }
    response = requests.get(URL, params = parametros)
    clima = response.json()
    #print(response.json())

    mostrar_respuesta(clima)


    print(clima["name"])
    print(clima["weather"] [0]["description"])
    print(clima["main"]["temp"])

ventana = Tk()
ventana.geometry("350x550")

texto_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify = "center")
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text="Obtener clima",font= ("Courier", 20, "normal"), command = lambda: clima(texto_ciudad.get()))
obtener_clima.pack()

ciudad= Label(font= ("Courier", 20, "normal" ))
ciudad.pack(padx= 20, pady = 20)

temperatura= Label(font= ("Courier", 50, "normal" ))
temperatura.pack(padx= 10, pady = 10)

descripcion= Label(font= ("Courier", 20, "normal" ))
descripcion.pack(padx= 10, pady = 10)

ventana.mainloop()
