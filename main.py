import requests
from send_email import send_email

topic = "tesla"
api_key = "d477a92e969944babdaa79e70a11c579"
url = "https://newsapi.org/v2/everything?q={topic}}&from=2025-11-30&sortBy=publishedAt&apiKey=d477a92e969944babdaa79e70a11c579&language=en"


# make a request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access a article titles and descriptions
body = ""
for article in content['articles'][:20]:
    # Check if description exists (is not None)
    if article['description'] is not None:
        body += "subject :Today's news" "\n" + article['title'] + "\n" + article['description'] + "\n" + article['url'] + "\n\n"
    else:
        # If no description, use title and url only
        body += article['title'] + "\n" + article['url'] + "\n\n"

body = body.encode("utf-8")
send_email(message=body)
