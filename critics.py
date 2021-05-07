import requests
import random
from data import URL_MOVIES, params
from urllib.parse import quote


def get_critics():
    url = f"{URL_MOVIES}critics/all.json"
    response = requests.get(url, params=params)
    return response.json(), response.json()["num_results"]


def pick_random_critic():
    all_critics, number_of_all = get_critics()
    pick_one = random.randint(0, number_of_all-1)
    random_critic_pick = all_critics["results"][pick_one]
    display_name = str(random_critic_pick["display_name"])
    return random_critic_pick, display_name


def url_builder(source):
    return quote(source)


def random_critic():
    individual = url_builder(pick_random_critic()[1])
    url = f"{URL_MOVIES}critics/{individual}.json"
    response = requests.get(url, params=params)
    return response.json()


def the_one_critic(source="Stephen Holden"):
    critic = url_builder(source)
    url = f"{URL_MOVIES}critics/{critic}.json"
    response = requests.get(url, params=params)
    return response.json()
