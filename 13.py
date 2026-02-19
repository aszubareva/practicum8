flag = 0
counter = 0
while flag != 1:
    ticket = input()
    counter += 1
    if len(ticket) % 2 == 0:
        sum1 = sum2 = 0
        for i in range(len(ticket)//2):
            sum1 += int(ticket[i])
        for i in range(len(ticket)//2, len(ticket)):
            sum2 += int(ticket[i])
        if sum1 == sum2:
            flag = 1
print(counter)
