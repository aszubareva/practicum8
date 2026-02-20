import time

clue = input('Подсказка: ')
secret_word = input('Слово: ')

time.sleep(3)
print("\n" * 25)

print(clue)
line = list('*' * len(secret_word))
print("".join(line))

lives = 10
while lives > 0:
    print("Буква или слово (0 - буква, 1 - слово)?")
    choice = int(input())

    if choice == 0:
        letter = input("Введите букву: ")
        for i in range(len(line)):
            if secret_word[i] == letter:
                line[i] = letter
        print("".join(line))
        if secret_word == "".join(line):
            print("Победа!")
            break

    elif choice == 1:
        word = input("Введите слово: ")
        if word == secret_word:
            print("Победа!")
        else:
            print("Проигрыш!")
        break

    lives -= 1
    if lives == 0:
        print("Проигрыш! Жизни закончились...")







