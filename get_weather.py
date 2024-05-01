import tkinter as tk
import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f'https://ja.weather-forecast.com/locations/{city}/forecasts/latest'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        weather_desc = soup.find(class_='b-forecast__table-description-content').text.strip()
        weather_info = f'Weather: {weather_desc}'
        result_label.config(text=weather_info)
    else:
        result_label.config(text="City not found")

def search():
    city = city_entry.get()
    get_weather(city)

root = tk.Tk()
root.title("get_weather App")

city_label = tk.Label(root, text="都市名をローマ字で入力: ")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

search_button = tk.Button(root, text="天気を表示", command=search)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()