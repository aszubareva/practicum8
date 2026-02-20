import time

secret_number = input('Загадайте число: ')

time.sleep(3)
print("\n" * 25)

lives = 10

while lives > 0:
    cows = bulls = 0
    print("Введите число: ")
    number = input()
    for i in range(4):
        if number[i] == secret_number[i]:
            bulls += 1
        elif number[i] in secret_number:
            cows += 1
    print("Быков:", bulls, " Коров:", cows)

    if secret_number == number:
        print("Победа!")
        break

    lives -= 1
    if lives == 0:
        print("Проигрыш! Жизни закончились...")





