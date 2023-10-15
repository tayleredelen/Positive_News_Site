import requests

api_key = "c0bb248e83674588a3b909f3118faf6d"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2023-09-15&sortBy=publishedAt&apiKey="
       "c0bb248e83674588a3b909f3118faf6d")

request = requests.get(url)
content = request.text
print(content)