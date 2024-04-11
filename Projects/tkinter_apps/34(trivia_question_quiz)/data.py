import requests

link = "https://opentdb.com/api.php?amount=10&type=boolean"

response = requests.get(url=link)
response.raise_for_status()
data = response.json()

question_data = data['results']


