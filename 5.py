text1 = input()
text2 = input()
text3 = input()
text = text1 + text2 + text3
symbols = set(text)
for ch in sorted(symbols):
    count1 = text1.count(ch)
    count2 = text2.count(ch)
    count3 = text3.count(ch)
    ar = sorted([count1, count2, count3])
    if ar[0] == ar[1] == 0 and ar[2] != 0:
        print(ch, end=" ")

