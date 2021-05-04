import pytest
import responses
from critics import get_critics, pick_random_critic, individual_critic
from data import expected_result, expected_result_one, URL_MOVIES
import json

URL_CRITICS_ALL = f"{URL_MOVIES}critics/all.json"


@responses.activate
def test_all_critics():
    responses.add(responses.GET, URL_CRITICS_ALL, json=expected_result, status=200)
    query = get_critics()
    expected = expected_result, expected_result["num_results"]
    assert query == expected


@responses.activate
def test_pick_random_critic():
    responses.add(responses.GET, URL_CRITICS_ALL, json=expected_result, status=200)
    random_id = pick_random_critic()
    assert random_id != None


@responses.activate
def test_individual_critic():
    URL = f"{URL_MOVIES}critics/A.%20O.%20Scott.json"
    responses.add(responses.GET, URL, json=expected_result_one, status=200)
    print(individual_critic())




