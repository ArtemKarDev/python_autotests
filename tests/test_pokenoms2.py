import requests
import pytest


def test_check_status_code():
    response = requests.get('https://pokemonbattle.me:9104/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response = requests.get('https://pokemonbattle.me:9104/trainers', 
                            params = {'trainer_id' : 4051})
    assert response.json()['trainer_name'] == 'ArTiger007'

@pytest.mark.parametrize('key, value', [('trainer_name', 'ArTiger007'),('city', 'Kostroma')])

def test_parameters_body(key, value):
    response = requests.get('https://pokemonbattle.me:9104/trainers',
                            params = {'trainer_id' : 4051})
    assert response.json()[key] == value