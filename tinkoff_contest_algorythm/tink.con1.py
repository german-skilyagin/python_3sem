def calculate_score(x, y):
    distance = (x**2 + y**2)**0.5
    if distance <= 0.1:
        return 3
    elif distance <= 0.8:
        return 2
    elif distance <= 1:
        return 1
    else:
        return 0

total_score = 0
for _ in range(3):
    x, y = map(float, input().split())
    total_score += calculate_score(x, y)

print(total_score)
