import requests
import hashlib
from datetime import datetime as dt
import random


def create_card():
    public = "d826285d434dddb9a88bb49910818d40"
    private = "28f9ac62fa2009ba154f05e6709068cdbe8f45d9"
    ts = str(dt.now())
    my_string = ts + private + public
    hash_string = hashlib.md5(bytes(my_string, "utf-8")).hexdigest()
    num = random.randint(0, 1492)
    response = requests.get(
        f"http://gateway.marvel.com/v1/public/characters?limit=1&offset={num}&ts={ts}&apikey={public}&hash={hash_string}")
    data = response.json()
    name = data['data']['results'][0]['name'].lower()
    card_types = ['regular', 'silver', 'gold', 'premium']
    type = random.choices(card_types, weights=(57.5, 25, 12.5, 7.5), k=1)
    if type[0] == 'silver':
        power = 100
    elif type[0] == 'gold':
        power = 500
    elif type[0] == 'premium':
        power = 1000
    else:
        power = 0
    if 'iron man' in name or 'spider-man' in name or 'hulk' in name or 'thor' in name or 'captain america' in name or 'black widow' in name or 'doctor strange' in name or 'thanos' in name:
        power += 1000
    elif 'black panther' in name or 'gamora' in name or 'winter soldier' in name or 'ant-man' in name or 'falcon' in name or 'wolverine' in name or 'venom' in name:
        power += 500
    else:
        power += 100
    details = data['data']['results'][0]['urls'][0]['url']
    return [name, power, details, type[0]]
