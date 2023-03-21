import json
import pytest
from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture
def app():
    from app import app
    return app


@pytest.fixture
def client(app: Flask):
    return app.test_client()


def test_favorite_pokemon_stats(app: Flask, client: FlaskClient):
    response = client.get('/api/v1/favorite-pokemon-stats')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'pokemon_data' in data
    assert 'average_base_happiness' in data
    assert 'mean_base_happiness' in data
    assert 'median_base_happiness' in data
