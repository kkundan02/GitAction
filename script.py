#main.py
#print("Hello, Kundan it's your GithubAction Demo Project")
import requests
def call_api():
    url = "https://api.example.com/data"
    response = requests.get(url)
    print(response.json())

call_api()
