print("В этой программе вы должны ввести трёхзначное число. Цифры в нём не должны повторяться.\nПрограмма выведет все возможные комбинации при перестановке")
print("Для выхода введите - exit\n")
while True:
    charCheker = True
    userInput = input("Введите своё число:")
    if(userInput =="exit"):
        break
    for character in userInput:
        if character not in['1','2','3','4','5','6','7','8','9','0']:
            charCheker = False
    if(charCheker):
        if(len(userInput) == 3):
            if((userInput[0]!= userInput[1] and userInput[0]!= userInput[2]) 
            and (userInput[1]!= userInput[0] and userInput[1]!= userInput[2])
            and(userInput[2]!= userInput[0] and userInput[2]!= userInput[1])):
                print(userInput[0],userInput[1],userInput[2])
                print(userInput[0],userInput[2],userInput[1])
                print(userInput[1],userInput[0],userInput[2])
                print(userInput[1],userInput[2],userInput[0])
                print(userInput[2],userInput[0],userInput[1])
                print(userInput[2],userInput[1],userInput[0])
            else:
                print("Введите разные цифры")
        elif(len(userInput) > 3):
            print("Слишком много цифр")
        elif(len(userInput) < 3):
            print("Слишком мало цифр")
    elif(charCheker == False):
        print("Не вводите буквы и символы")
