import requests

api_key = "c0bb248e83674588a3b909f3118faf6d"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-09-16&sortBy=publishedAt&apiKey"
       "=c0bb248e83674588a3b909f3118faf6d")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
