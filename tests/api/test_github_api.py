# all apin tests is here
import pytest


@pytest.mark.api
def test_user_exist(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exist(github_api):

    r = github_api.get_user('tarasyakushevych')

    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')

    assert r['total_count'] == 58 # at the moment of the test
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('taras_yakushevych_repo')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_first_commit_author_email(github_api):
    r = github_api.search_commits('TarasPyAuto', 'Course-project')
    assert  r[0]['commit']['author']['email'] == 'taras03101999@ukr.net'

@pytest.mark.api
def test_repo_owner_cannot_be_found(github_api):
    r = github_api.search_commits('Taras0310', 'Course-project')
    assert  r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_name_cannot_be_found(github_api):
    r = github_api.search_commits('TarasPyAuto', 'My-project')
    assert  r['message'] == 'Not Found'

@pytest.mark.api
def test_commiter_name_can_be_found(github_api):
    r = github_api.search_commits('TarasPyAuto', 'Course-project', 'Taras0310')
    assert r[0]['committer']['login'] == 'Taras0310'

@pytest.mark.api
def test_commiter_name_can_not_be_found(github_api):
    r = github_api.search_commits('TarasPyAuto', 'Course-project', 'TarasQA')
    assert len(r) == 0

@pytest.mark.api
def test_total_count_emojis(github_api):
    r = github_api.get_emojis()
    assert len(r) == 1935

@pytest.mark.api
def test_emoji_can_be_found(github_api):
    r = github_api.get_emojis()
    assert 'zombie_woman' in r.keys()

@pytest.mark.api
def test_emoji_can_not_be_found(github_api):
    r = github_api.get_emojis()
    assert 'qq'  not in r.keys()