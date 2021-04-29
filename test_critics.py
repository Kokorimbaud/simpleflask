import pytest
import responses
from critics import get_critics, pick_random_critic, name_to_url, individual_critic
from data import expected_result, expected_result_one, URL_CRITICS
import json


@responses.activate
def test_all_critics():
    responses.add(responses.GET, URL_CRITICS, json=expected_result, status=200)
    query = get_critics()
    expected = expected_result, expected_result["num_results"]
    assert query == expected


@responses.activate
def test_pick_random_critic():
    responses.add(responses.GET, URL_CRITICS, json=expected_result, status=200)
    random_id = pick_random_critic(id)
    assert random_id != None


@responses.activate
def test_name_to_url():
    responses.add(responses.GET, URL_CRITICS, json=expected_result_one, status=200)
    name = name_to_url()
    assert name == "A.%20O.%20Scott"

