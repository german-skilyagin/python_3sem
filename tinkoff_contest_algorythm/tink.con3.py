def check_level(heights, level):
    total_up = 0
    total_down = 0
    for h in heights:
        if h < level:
            total_up += level - h
        else:
            total_down += h - level
    return total_up, total_down

def find_magnitude_height(n, heights):
    left = 0
    right = max(heights)
    while right - left > 1e-4:
        mid = left + (right - left) / 2
        up, down = check_level(heights, mid)
        if up < down:
            left = mid
        else:
            right = mid
    return left

n = int(input())
heights = list(map(int, input().split()))

result = find_magnitude_height(n, heights)
print("{:.1f}".format(result))

