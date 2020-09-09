import requests
import json
joke = requests.get('https://official-joke-api.appspot.com/random_joke').json()
setup = joke['setup']
punchline = joke['punchline']
print(setup)
print(punchline)
