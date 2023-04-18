import requests

token = 'd5fe566ad2d94a1ac2dad5564c9df984'

respons = requests.post('https://pokemonbattle.me:9104/trainers/reg', headers = {'Content-Type': 'application/json'},
                        json = { 'trainer_token': token, 'email': 'GERMANqa@dolnikov.ru', 'password':'Iloveqa1'})

print(respons.text)

respons_confirm = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', headers = {'Content-Type': 'application/json'},
                                json = { 'trainer_token': token})

print(respons_confirm.text)

add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 
                                                                                        'trainer_token': token},
                                                                                        json = { 'name': 'Бульбазавр', 
                                                                                                'photo': 'https://dolnikov.ru/pokemons/albums/010.png'})

print(add_pokemon_response.text)

