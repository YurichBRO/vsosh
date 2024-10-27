from pprint import pprint

n = 4
answer = []
data = [
    [2,2,4,5],
    [3,4,9,7],
    [2,9,9,10],
    [7,1,9,7],
]

for io in range(n):
    a, b, c, d = data[io]
    i = [[a, c], [b, d]]
    s = []
    de = []
    for j in answer:
        x_1 = i[0][0]
        x_2 = i[0][1]
        x_1j = j[0][0]
        x_2j = j[0][1]
        y_1 = i[1][0]
        y_2 = i[1][1]
        y_1j = j[1][0]
        y_2j = j[1][1]
        
        if (x_2 + 1 >= x_1j and x_2 + 1 < x_2j) or (x_1 - 1 <= x_2j and x_1 > x_1j):
            if y_1 <= y_2j and y_2 >= y_1j:
                s.append([[min(x_1, x_1j), max(x_2, x_2j)], [max(y_1, y_1j), min(y_2j, y_2)]])

    answer.append(i)
    answer.extend(s)
f = []
for i in answer:
    if not i in f:
        f.append(i)
        
answer = f

dic = {}
t = []
for w in range(len(answer)):
    i = answer[w]
    dic[str(i[0])] = i[1][1] - i[1][0] + 1
    if not i in t:
        for j in [*(answer[:i]), *(answer[i::])]:
            x_1 = i[0][0]
            x_2 = i[0][1]
            x_1j = j[0][0]
            x_2j = j[0][1]
            y_1 = i[1][0]
            y_2 = i[1][1]
            y_1j = j[1][0]
            y_2j = j[1][1]
            print(x_1, x_1j, x_1 >= x_1j, x_2, x_2j, x_2 <= x_2j, dic[str(i[0])])
            if  x_1 >= x_1j and x_2 <= x_2j:

                #print([dic.get(str(i[0]), 0) + j[1][1] - j[1][0] + 1])
                dic[str(i[0])] = dic.get(str(i[0]), 0) + j[1][1] - j[1][0]

    t.append(i)



pprint(dic)