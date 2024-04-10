import requests
from send_email import send_email



api_key = "812f337180d74507be3a2764dbe69a26"
url = ("https://newsapi.org/v2/everything?q=japan&"
       "from=2024-04-09&sortBy=publishedAt&"
       "apiKey=812f337180d74507be3a2764dbe69a26")

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Access the article titles, description
body = ''
for article in content["articles"]:
    if article["title"] is not None: # тут нужно обработчик ошибок написать
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
#send email
send_email(body)

