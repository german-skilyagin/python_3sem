def can_send_gifts(p, gifts):
    gifts.sort(key=lambda x: x[2])
    day = 1
    for gift in gifts:
        d, c, s = gift
        if day < d:
            day = d
        if day + c - 1 > s:
            return "NO"
        day += c
    return "YES"
p = int(input())
gifts = []
for _ in range(p):
    d, c, s = map(int, input().split())
    gifts.append((d, c, s))

result = can_send_gifts(p, gifts)
print(result)
