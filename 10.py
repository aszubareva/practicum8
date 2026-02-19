text = input().split()
if text:
    word = text[0]
    for i in range(1, len(text)):
        if text[i] != word and len(set(text[i])) == len(text[i]):
            print(text[i])

