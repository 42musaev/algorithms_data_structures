from typing import List

lst = [54, 2234, 542, 432, 563, 563]


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr
    else:
        center_idx = len(arr) // 2
        center = arr.pop(center_idx)
        left = [i for i in arr if i <= center]
        right = [i for i in arr if i >= center]
        return quick_sort(left) + [center] + quick_sort(right)


r = quick_sort(lst)
print(r)
