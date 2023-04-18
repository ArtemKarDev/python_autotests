import requests

token = 'd5fe566ad2d94a1ac2dad5564c9df984'

response = requests.post('https://pokemonbattle.me:9104/pokemons', 
                        headers = {'Content_Type': 'application/json',
                                'trainer_token': token},
                        json = {'name': 'Завробульб',
                                'photo': 'https://dolnikov.ru/pokemons/albums/610.png'})
print(response.json())

response = requests.put('https://pokemonbattle.me:9104/pokemons', 
                        headers = {'Content_Type': 'application/json',
                                'trainer_token': token},
                        json = {'pokemon_id': '9339',
                                'name': 'Завробульб2',
                                'photo': 'https://dolnikov.ru/pokemons/albums/710.png'})
print(response.json())

response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
                        headers = {'Content_Type': 'application/json',
                                'trainer_token': token},
                        json = {'pokemon_id': '9339'})
print(response.json())