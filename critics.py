import requests
from requests.auth import HTTPBasicAuth
import random
from data import URL_MOVIES, params
from urllib.parse import quote


def get_critics():
    URL = f"{URL_MOVIES}critics/all.json"
    response = requests.get(URL, params=params)
    print(URL)
    print(response.json()["num_results"])
    return response.json(), response.json()["num_results"]


def pick_random_critic():
    all, number_of_all = get_critics()
    pick_one = random.randint(0, number_of_all-1)
    print(f'The one: {pick_one}')
    random_critic = all["results"][pick_one]
    display_name = str(random_critic["display_name"])
    return random_critic, display_name


def individual_critic():
    individual = quote(pick_random_critic()[1])
    URL = f"{URL_MOVIES}critics/{individual}.json"
    print(URL)
    response = requests.get(URL, params=params)
    return response.json()