# file for test http request
import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers
    print(headers['Server'])

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'github.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/taras_yakushevych')

    assert r.status_code == 404
