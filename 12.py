import keyword
name = input()
if name:
    if keyword.iskeyword(name) or name[0].isdigit():
        print("NO")
    else:
        flag = 0
        for ch in name:
            if (48 <= ord(ch) <= 57 or
                    65 <= ord(ch) <= 90 or
                    97 <= ord(ch) <= 122 or
                    ord(ch) == 95) == 0:
                print("NO")
                flag = 1
                break
        if flag == 0:
            print("YES")
else:
    print("NO")
