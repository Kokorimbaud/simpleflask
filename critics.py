import requests
from requests.auth import HTTPBasicAuth
import random
from data import URL_CRITICS, params


def get_critics():
    URL = f"{URL_CRITICS}/critics/all.json"
    response = requests.get(URL, params=params)
    print(response.json()["num_results"])
    return response.json(), response.json()["num_results"]


def pick_random_critic():
    all, number_of_all = get_critics()
    pick_one = random.randint(0, number_of_all)
    print(f'The one: {pick_one}')
    random_critic = all["results"][pick_one]
    display_name = list(random_critic["display_name"])
    return random_critic, display_name


def name_to_url():
    display_name = pick_random_critic()[1]
    names = []
    for n in display_name:
        if n != ' ':
            names.append(n)
        elif n == ' ':
            names.append("%20")
    url_suffix = ''.join(names)
    return url_suffix


def individual_critic():
    individual = name_to_url()
    URL = f"{URL_CRITICS}critics/{individual}.json"
    print(URL)
    response = requests.get(URL, params=params)
    return response.json()