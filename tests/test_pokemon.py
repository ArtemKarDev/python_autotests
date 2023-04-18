import requests
import pytest

@pytest.mark.parametrize('key, value', [('trainer_name', 'ArTiger007')])

def test_parametrs_body(key,value):
    response = requests.get('https://pokemonbattle.me:9104/trainers',
                            params = {'trainer_id' : 4051})
    assert response.status_code == 200
    assert response.json()[key] == value