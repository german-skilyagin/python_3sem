n = int(input())
books = list(map(int, input().split()))
book_heights = sorted(set(books))
stacks = []
for height in book_heights:
    stacks.append(books.count(height))
print(len(book_heights))
print(*sorted(stacks))
