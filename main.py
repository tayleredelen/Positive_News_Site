import requests
from send_email import send_email

topic = "tesla"
api_key = "c0bb248e83674588a3b909f3118faf6d"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&from=2023-09-18&sortBy=publishedAt&apiKey="
       "c0bb248e83674588a3b909f3118faf6d&"
       "language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = ("Subject: Today's news" + "\n" +
                body + article["title"] + "\n"
                + str(article["description"]) +
                "\n" + article["url"] + 2 * "\n")


body = body.encode("utf-8")
send_email(message=body)


