from collections import defaultdict

def three_sum(arr, target):
    for a in range(len(arr) - 2):
        b = a + 1
        c = len(arr) - 1
        while b < c:
            s = arr[a] + arr[b] + arr[c]
            if s < target:
                b += 1
            elif s > target:
                c -= 1
            else:
                return (arr[a], arr[b], arr[c])

def max_subarr_length_with_sum_under(arr, k):
    left = 0
    s = 0
    max_l = 0
    for right in range(len(arr)):
        s += arr[right]
        while s > k:
            s -= arr[left]
            left += 1
        max_l = max(max_l, right - left + 1)
    return max_l

def number_of_pairs_with_sum(arr, target):
    pairs = set()
    lookup = set()
    for i in arr:
        if i in lookup:
            if i < target - i:
                pair = (i, target - i)
            else:
                pair = (target - i, i)
            pairs.add(pair)
        else:
            lookup.add(target - i)
    return len(pairs)

def closest_pair_sum(arr, target):
    l = 0
    r = len(arr) - 1
    min_diff = float('inf')
    closest_pair = (-1, -1)
    while l < r:
        s = arr[l] + arr[r]
        diff = abs(s - target)
        if diff == 0:
            return (arr[l], arr[r])
        elif diff < min_diff:
            min_diff = diff
            closest_pair = (l, r)
        if s > target:
            r -= 1
        else:
            l += 1
    return (arr[closest_pair[0]], arr[closest_pair[1]])

def longest_unique_substr(s):
    max_length = 1
    l = 0
    counter = defaultdict(int)
    counter[s[l]] += 1
    for r in range(1, len(s)):
        counter[s[r]] += 1
        while counter[s[r]] == 2:
            counter[s[l]] -= 1
            l += 1
        length = r - l + 1
        max_length = max(max_length, length)
    return max_length

def even_left_odd_right(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] & 1 and not arr[r] & 1:
            arr[l], arr[r] = arr[r], arr[l]
        elif arr[l] & 1:
            r -= 1
        else:
            l += 1
    return arr

def min_subaaray_with_sum_greater_than(arr, s):
    l = 0
    r = -1
    min_length = float('inf')
    sum = 0
    while r < len(arr) and sum <= s:
        r += 1
        sum += arr[r]
    if r == len(arr):
        return 0
    while sum > s:
        sum -= arr[l]
        l += 1
    min_length = r - l + 2
    for r in range(r + 1, len(arr)):
        sum += arr[r]
        while sum > s:
            sum -= arr[l]
            l += 1
        if sum + arr[l - 1] <= s:
            continue
        min_length = min(min_length, r - l + 2)
    return min_length

def consecutive_ones_with_one_gap(arr):
    toggled = False
    max_length = 0
    l = 0
    for r in range(len(arr)):
        if arr[r] == 1:
            continue
        if not toggled:
            toggled = True
        else:
            length = r - l
            max_length = max(max_length, length)
            while arr[l] != 0:
                l += 1
            while arr[l] == 0:
                l += 1
            toggled = False
    return max_length

def max_unique_subarray_sum_with_length_in_range(arr, small, large):
    counter = defaultdict(int)
    max_sum = 0
    l = 0
    s = arr[0]
    counter[arr[0]] += 1
    for r in range(1, len(arr)):
        counter[arr[r]] += 1
        s += arr[r]
        print(l, r, dict(counter), s)
        while counter[arr[r]] == 2:
            s -= arr[l]
            counter[arr[l]] -= 1
            l += 1
            print(l, r, dict(counter), s)
        while r - l + 1 > large:
            s -= arr[l]
            counter[arr[l]] -= 1
            l += 1
            print(l, r, dict(counter), s)
        if r - l + 1 < small:
            continue
        else:
            max_sum = max(s, max_sum)
    return max_sum

print(three_sum([-4, -1, -1, 0, 1, 2], 0))
print(max_subarr_length_with_sum_under([3, 1, 2, 7, 4, 2, 1], 8))
print(number_of_pairs_with_sum([1, 5, 7, -1, 5], 6))
print(closest_pair_sum([1, 3, 4, 7, 10], 15))
print(longest_unique_substr("abcabccbb"))
print(even_left_odd_right([1, 2, 3, 4, 5, 6, 7]))
print(min_subaaray_with_sum_greater_than([2, 3, 1, 2, 4, 3], 7))
print(consecutive_ones_with_one_gap([1, 0, 1, 1, 0, 1]))
print(max_unique_subarray_sum_with_length_in_range([4, 2, 1, 5, 6], 2, 3))