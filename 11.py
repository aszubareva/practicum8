text = input().split()
if len(text) == 1:
    print("Петя")
else:
    for i in range(1, len(text)):
        if text[i-1][-1] != text[i][0]:
            if (i-1) % 2 != 0:
                print("Ваня")
            else:
                print("Петя")
            break
        elif i == len(text) - 1:
            if i % 2 != 0:
                print("Ваня")
            else:
                print("Петя")
            break
