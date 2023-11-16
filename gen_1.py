def prime_generator(x):
    prs = {}
    p = 2
    while p < x:
        if p not in prs:
            yield p
            prs[p * p] = [p]
        else:
            for s in prs[p]:
                prs.setdefault(s + p, []).append(s)
            del prs[p]
        p += 1
print(*prime_generator(100))
print(prime_generator(100))
m = prime_generator(5)
print(m)
print(next(m))