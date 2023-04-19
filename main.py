import requests

token = ''
with open('token.txt','r') as f:
    token = f.read()

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