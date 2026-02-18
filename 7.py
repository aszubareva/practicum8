text = input().split()
mn = 10**9
for word in text:
    if len(word) < mn:
        mn = len(word)
print(mn)
