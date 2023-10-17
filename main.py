import requests
from send_email import send_email


api_key = "c0bb248e83674588a3b909f3118faf6d"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-09-16&sortBy=publishedAt&apiKey"
       "=c0bb248e83674588a3b909f3118faf6d")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

