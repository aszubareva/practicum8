text = input()
balance = 0
for i in range(len(text)):
    if text[i] == '(':
        balance += 1
    elif text[i] == ')':
        balance -= 1
        if balance < 0:
            break
if balance == 0:
    print("correct")
else:
    print("incorrect")
