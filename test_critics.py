
import responses
from critics import get_critics, pick_random_critic, the_one_critic
from data import expected_result, URL_MOVIES, expected_result_one

URL_CRITICS_ALL = f"{URL_MOVIES}critics/all.json"
URL_INDIVIDUAL = f"{URL_MOVIES}critics/A.%20O.%20Scott.json"


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
    assert random_id is not None


@responses.activate
def test_stephen_holden():
    responses.add(responses.GET, URL_INDIVIDUAL, json=expected_result_one, status=200)
    query = the_one_critic("A. O. Scott")
    assert query == expected_result_one




