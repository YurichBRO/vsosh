def bubble_sort(arr):
    if len(arr) < 2:
        return len(arr)
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def count_unique(arr):
    bubble_sort(arr)
    count = 1
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            count += 1
    return count

from collections import defaultdict

def bubble_sort_and_get_number_of_unique(arr):
    bubble_sort(arr)
    unique = defaultdict(int)
    for i in arr:
        unique[i] += 1
    return unique

def selection_sort(arr):
    if len(arr) < 2:
        return arr
    for i in range(len(arr) - 1):
        j = min(range(i, len(arr)), key=lambda x: arr[x])
        arr[i], arr[j] = arr[j], arr[i]

def selection_sort_and_get_number_of_unique(arr):
    selection_sort(arr)
    unique = defaultdict(int)
    for i in arr:
        unique[i] += 1
    return unique

def insertion_sort(arr):
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def insertion_sort_and_get_number_of_first_letter(arr):
    insertion_sort(arr)
    unique = defaultdict(int)
    for i in arr:
        unique[i[0]] += 1
    return unique

def quick_sort(arr, key=lambda x: x):
    if len(arr) < 2:
        return arr
    pivot = key(arr[len(arr) // 2])
    left = []
    middle = []
    right = []
    for i in arr:
        val = key(i)
        if val < pivot:
            left.append(i)
        elif val > pivot:
            right.append(i)
        else:
            middle.append(i)
    return quick_sort(left, key=key) + middle + quick_sort(right, key=key)


def merge(arr1, arr2, key=lambda x: x):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        val1 = key(arr1[i])
        val2 = key(arr2[j])
        if val1 < val2:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

def merge_sort(arr, key=lambda x: x):
    if len(arr) < 2:
        return arr
    mid = len(arr) >> 1
    return merge(merge_sort(arr[:mid], key=key), merge_sort(arr[mid:], key=key), key=key)


def merge_sort_and_find_average(arr):
    arr = merge_sort(arr, lambda x: x['score'])
    return (arr, sum(i['score'] for i in arr) / len(arr))


arr = [
    {'name': 'a', 'score': 1234},
    {'name': 'b', 'score': 4321},
    {'name': 'c', 'score': 3412},
]
print(merge_sort_and_find_average(arr))