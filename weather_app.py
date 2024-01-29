import requests
def process_data(data):
    return {"city": data["name"], "datetime": data["dt"], "temp" : data['main']['temp'], "humidity" : data['main']['humidity']}


def get_weather_data(city ="Tehran",appid ="f7724e8aed23c33e6018eb622216937f"):
    # api-endpoint
    URL = f"https://api.openweathermap.org/data/2.5/weather"

    # location given here
    location = "delhi technological university"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'q':city , 'appid':appid }
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()
    return process_data(data)

print(get_weather_data("kokkola"))