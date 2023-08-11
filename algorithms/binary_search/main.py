from typing import List

arr_range = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50
]


def binary_search(array: List[int], seeking_value: int) -> int | None:
    left_idx = 0
    right_idx = len(array) - 1

    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2
        found_value = array[middle_idx]

        if found_value == seeking_value:
            return middle_idx

        if found_value < seeking_value:
            left_idx = middle_idx + 1
        elif found_value > seeking_value:
            right_idx = middle_idx - 1

    return


result = binary_search(arr_range, 35)
print(result)
