import pytest
from app import app


keys_should_de = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
}


def test_api_all_posts():
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200
    print(response.status_code, end=' ')
    api_response = response.json
    assert type(api_response) == list
    assert set(api_response[0].keys()) == keys_should_de


def test_api_post():
    response = app.test_client().get('/app/posts/')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == dict
    assert set(api_response.keys()) == keys_should_de

