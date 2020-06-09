import requests
import json
joke_as_str = requests.get('https://official-joke-api.appspot.com/random_joke').text
joke = json.loads(joke_as_str)
setup = joke['setup']
punchline = joke['punchline']
print(setup)
print(punchline)