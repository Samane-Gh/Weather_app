import sqlite3
import requests
import time

def sql_connector():
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    return con,cur
def create_table(con,cur):
    cur.execute("CREATE TABLE IF NOT EXISTS weather(name TEXT, datetime TEXT,temp TEXT,humidity TEXT)")
    con.commit()
def insert_data(con,cur,data):
    cur.execute("INSERT INTO weather values(?,?,?,?)", tuple([v for k,v in data.items()]))
    con.commit()
    
def process_data(data):
    return {"city": data["name"], "datetime": time.ctime(int(data["dt"])), "temp" : data['main']['temp'], "humidity" : data['main']['humidity']}


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

con , cur = sql_connector()
create_table(con,cur)
while True:
    data_weather = get_weather_data("Tehran")
    insert_data(con,cur,data_weather)
    print(data_weather)
    time.sleep(5)