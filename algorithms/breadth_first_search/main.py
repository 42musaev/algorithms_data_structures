from collections import deque
from typing import Dict

graph = {
    'name': 'I''m',
    'seller_mango': False,
    'friends': [
        {
            'name': 'Bob',
            'seller_mango': False,
            'friends': []
        },
        {
            'name': 'Clary',
            'seller_mango': False,
            'friends': [
                {
                    'name': 'Tailer',
                    'seller_mango': True,
                    'friends': []
                },
                {
                    'name': 'John',
                    'seller_mango': True,
                    'friends': [
                        {
                            'name': 'Jax',
                            'seller_mango': False,
                            'friends': []
                        },
                    ]
                },
            ]
        },
        {
            'name': 'Smith',
            'seller_mango': False,
            'friends': []
        }
    ]
}


def find_mango_seller(tree: Dict) -> Dict | False:
    que = deque()
    que += [tree]

    while que:
        person = que.popleft()
        if person.get('seller_mango'):
            return person['name']
        friends = person.get('friends')
        if friends:
            que += friends
    return False


print(find_mango_seller(graph))
