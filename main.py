import requests
import random
import os
LAST_ID = 0
CURRENT_ID = 0


def get_posts():
    token = os.environ.get("token")
    url = 'https://api.vk.com/method/wall.get'
    params = {'owner_id': '-187962937',
              'offset': 1,
              'count': 1,
              'access_token': token,
              'v': '5.126'}
    r = requests.get(url, params=params)
    data = r.json()['response']['items']
    return int(data[0]['id'])


def like(tokens, count, post_id):
    for i in range(count):
        url = 'https://api.vk.com/method/likes.add'
        params = {
            "owner_id": -187962937,
            "type":"post",
            "item_id": post_id,
            "v": "5.126",
            "access_token": random.choice(tokens)
        }
        r = requests.get(url, params=params)
        print(r.text)


def read(name):
    with open(name, "r", encoding="utf-8") as f:
        data = f.read()

    return data

if __name__ == '__main__':
    tokens = os.environ.get("tkns").split(',')

    while True:
        CURRENT_ID = get_posts()
        if CURRENT_ID != LAST_ID:
            likes_count = random.randint(12, 36)
            print(f"Кручу {likes_count} на {CURRENT_ID}")
            like(tokens, likes_count, CURRENT_ID)
            LAST_ID = CURRENT_ID

