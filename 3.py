text = input().lower()
symbols = set(text)
letters = 0
for ch in symbols:
    if ch.isalpha():
        letters += 1
print(letters)
