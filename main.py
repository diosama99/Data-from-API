import requests

api_key = "812f337180d74507be3a2764dbe69a26"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-01-17&sortBy=publishedAt&"
       "apiKey=812f337180d74507be3a2764dbe69a26")

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Access the article titles, description
for article in content["articles"]:
       print(article["description"])
       print(article["title"])

#check