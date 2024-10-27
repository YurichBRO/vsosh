n = 1
data = [
    [2,2,4,5],
    [3,4,9,7],
    [2,9,9,10],
    [7,1,9,7]
]

coords = set()
for i in data:
    coords.add(i[1])
    coords.add(i[3] + 1)
coords = list(coords)

data.sort(key=lambda x: x[0])

regions = [[] for i in range(len(coords) - 1)]
for i in data:
    l = 0
    r = len(coords) - 1
    while l <= r:
        m = (l + r) >> 1
        if coords[m] < i[1]:
            l = m + 1
        elif coords[m] > i[1]:
            r = m - 1
        else:
            start = m
            break
    l = 0
    r = len(coords) - 1
    while l <= r:
        m = (l + r) >> 1
        if coords[m] < i[3] + 1:
            l = m + 1
        elif coords[m] > i[3] + 1:
            r = m - 1
        else:
            end = m
            break
    
    for j in range(start, end):
        regions[j].append((i[0],i[2]))

for i, region in enumerate(regions):
    if not region:
        continue
    new_region = [list(region[0])]
    for j in range(1, len(region)):
        if new_region[-1][1] + 1 >= region[j][0]:
            new_region[-1][1] = max(new_region[-1][1], region[j][1])
        else:
            new_region.append(list(region[j]))
    regions[i] = new_region

from collections import defaultdict
pairs = defaultdict(int)
max_pairs = {}
for i in range(len(regions)):
    start = coords[i]
    end = coords[i+1]
    width = end - start
    for j in regions[i]:
        t = tuple(j)
        pairs[t] += width
        if t not in max_pairs:
            max_pairs[t] = [[width], i]
            continue
        elif max_pairs[t][1] == i - 1:
            max_pairs[t][0][-1] += width
        else:
            max_pairs[t][0].append(width)
        max_pairs[t][1] = i

for i in max_pairs:
    max_pairs[i] = max(max_pairs[i][0])
            

from pprint import pprint
print(len(pairs.keys()))
for i in pairs:
    print(*i, pairs[i], max_pairs[i])