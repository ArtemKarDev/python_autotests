import requests
import pytest
import json


def test_authorization():
    response = requests.post('https://k-ampus.dev/api/v1/login',
                            json = {'username': 'skhalipa@gmail.com',
                                    'password': 'skhalipa@gmail.com'})
    assert response.status_code == 200
    assert bool(response.json().get('accessToken'))
    accessToken = response.json()['accessToken']
    return accessToken


# функция проверки полей и их типов в массиве или объекте json
def validate_fields(json_obj, fields):
    if not all(field in json_obj for field in fields):
        return False    
    # Если хоть одно из полей отсутствует в JSON файле, то сразу возвращаем False
    for field, field_type in fields.items():
        if not isinstance(json_obj[field], field_type):
            return False    
        # Если тип поля не соответствует заданному, возвращаем False
    # Если все проверки были успешны, возвращаем True
    return True

# словари для проверок 
content_field = {
    'content': list
}

content_fields = {
    "id": int,
    "name": str,
    "isHardSkill": bool,
    "skillIds": list
}

pageable_field = {
    'pageable': dict
}
pageable_fields = {
    'pageSize': int,
    'pageNumber': int,
    'offset': int,
    'unpaged': bool,
    'paged': bool
} 

sort_field = {
    'sort': dict
}

sort_fields = {
    'sorted': bool,
    'unsorted': bool,
    'empty': bool
} 


# @pytest.mark.parametrize('key, value', [
#                                         (None , content_field),         # Тест, что json содержит объект content и данный объект является массивом
#                                         ('content' , content_fields),        # Проверка каждого эелемента массива content на соответсвие типу
#                                         ('pageable', pageable_field),        # Тест, что json содержит объект pageable
#                                         ('pageable', pageable_fields),       # Проверка присутсвия полей в объекте pageable и соответствия типам
#                                         ('pageable', sort_field),           # Тест, что в объекте pageable присутствует подобъект sort
#                                         ('sort', sort_fields)           # Тест, что объект sort содержит поля и данные поля соответствуют типам
#                                         ]
#                         )

def test_get_competence():
    response = requests.get('https://k-ampus.dev/api/v1/competence',
                        headers={'Authorization': test_authorization()})
    # Тест, что статус операции, которую возвращает бэкенд равна 200
    assert response.status_code == 200



    # assert validate_fields(response.json()[key], value)



    # # Тест, что json содержит объект content и данный объект является массивом
    assert validate_fields(response.json(),content_field)
    # Тест, что объект content не является пустым, а содержит элементы
    assert bool(response.json()['content'])
    # Проверка каждого эелемента массива content на соответсвие типу
    assert validate_fields(response.json()['content'][0], content_fields)
    # Тест, что json содержит объект pageable
    assert validate_fields(response.json(), pageable_field)
    # Проверка присутсвия полей в объекте pageable и соответствия типам
    assert validate_fields(response.json()['pageable'], pageable_fields)
    # Тест, что в объекте pageable присутствует подобъект sort
    assert validate_fields(response.json()['pageable'], sort_field)
    # Тест, что объект sort содержит нижеописанные поля и данные поля соответствуют типам
    assert validate_fields(response.json()['sort'], sort_fields)
