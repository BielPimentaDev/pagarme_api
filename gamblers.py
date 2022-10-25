import time
import requests
from random import uniform, choice, randint, shuffle
import threading


URL = 'https://gerador-nomes.wolan.net/nome/aleatorio'


def make_gamblers(gamblers_list):

    colors = ["#1B8EFF", "#F9FD4A", "#EA5FBF"]
    for a in range(0, 100):
        response = requests.get(URL)
        names = response.json()
        names.pop(2)
        names.append(f"_{randint(0, 50)}")
        name = "".join(names)

        bet = randint(100, 8000)

        multiplier = f"{uniform(1, 8):.1f}"

        color = choice(colors)

        gamblers_list.append({
            "name": name,
            "color": color,
            "bet": bet,
            "multiplier": multiplier
        })


def read_gamblers(gamblers_list):
    shuffle(gamblers_list)
    return gamblers_list[:8]


# numero de jogadores 80 - 2400

# nome de usuario

# aposta R$ 100 - 6000

# multiplicador 1x - 8x
