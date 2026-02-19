text = input().split()
text.sort()
for i in range(1, len(text)):
    if text[i] == text[i-1]:
        print(text[i])
        break
