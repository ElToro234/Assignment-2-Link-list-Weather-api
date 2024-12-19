import requests
class newsApiHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY"
        self.articles = []
        self.current_index = 0
    def get_top_headlines(self, country="us"):
        params = {"country": country, "apiKey": self.api_key}
        response = requests.get(self.base_URL, params=params)
        if response.status_code == 200:
            return response.json()["articles"]
        else:
            raise ValueError(f"Error fetching data: {response.status_code}")

# api_key = 'API_KEY'
# news_api = newsApiHandler(api_key)
#
# # Get the top headlines
# headlines = news_api.get_top_headlines()





