import requests

def get_weather(city):
    api_key = "ab365baf6721be32e96687c938d415bc"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data
