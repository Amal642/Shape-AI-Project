import requests
#import os
from datetime import datetime

api_key = '6cb37541b015e1f470e16654f123e3b9'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

with open("weather_output.txt","w") as out_file:
    #out_file.write(str(temp_city))
    out_file.write("-------------------------------------------------------------\n"+
                   "Weather Stats for - {}  || {}".format(location.upper(), date_time)+
                   "\n-------------------------------------------------------------\n"+
                   "Current temperature is: {:.2f} deg C".format(temp_city)+"\n"+
                   "Current weather desc  :{}".format(weather_desc)+"\n"+
                   "Current Humidity      :{}".format(hmdt)+'%'+"\n"+
                   "Current wind speed    :{}".format(wind_spd)+'kmph'
                   )



print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')