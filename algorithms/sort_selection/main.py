from typing import Dict

x = {
    'a': 4442,
    'b': 442,
    'c': 42,
}


def get_max(d: Dict) -> Dict:
    max_dict = {}
    max_value = 0
    for k, v in d.items():
        if v > max_value:
            max_value = v
            max_dict = {k: v}
    return max_dict


def sort_selection(d: Dict) -> Dict:
    sort_dict = {}
    for _ in range(0, len(d.values())):
        max_dict = get_max(d)
        sort_dict = sort_dict | max_dict
        d.pop(list(max_dict.keys())[0])
    return sort_dict


print(sort_selection(x))
