text = input()
symbols = set(text)
for ch in symbols:
    if text.count(ch) == 3:
        print(ch)
        break


