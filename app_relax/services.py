import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_dog(params={}):
    response = generate_request('https://dog.ceo/api/breeds/image/random', params)
    if response:
       user = response.get('message')
       return user

    return ''