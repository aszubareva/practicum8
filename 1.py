text = input()
cur = 0
mx = 0
for ch in text:
    if ch.isspace():
        cur += 1
        if cur > mx:
            mx = cur
    else:
        cur = 0
print(mx)