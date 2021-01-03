import json
from urllib.request import urlopen , Request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


req = Request("https://pokeapi.co/api/v2/", headers={'User-Agent': 'XYZ/3.0'})
webpage = urlopen(req).read()



data = json.loads(webpage)

# print(json.dumps(data, indent=2))
print(len(data))

