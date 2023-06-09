import requests

API_KEY = "a033d83875a96369e9407b97df8cf124"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = round(data["main"]["temp"] - 273.15, 2)
    
    print("Weather:", weather)
    print("Temperture:", temp, "celsius")

else:
    print("An error accured.")