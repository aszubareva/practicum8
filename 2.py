text = input()
if not text:
    print(0)
else:
    mx = 1
    cur = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            cur += 1
            if cur > mx:
                mx = cur
        else:
            cur = 1
    print(mx)
