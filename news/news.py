import requests

def get_news():
    api_key = "4932cc44731a491996bc70450f381896"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    news = response.json()
    return news
