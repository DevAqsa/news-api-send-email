import requests

api_key = "d477a92e969944babdaa79e70a11c579"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-11-30&sortBy=publishedAt&apiKey=d477a92e969944babdaa79e70a11c579"


# make a request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access a article titles and descriptions
for article in content['articles']:
    print(article['title'])
    print(article['description'])

