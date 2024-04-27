print("Эта программа выведет вам длину введённого числа")
print("Для выхода введите - exit\n")
while True:
    charChecker = True
    userInput = input("Введите число:")
    if(userInput=="exit"):
        break
    for character in userInput:
        if(character == '0' or character == '1' or character == '2' or character == '3' 
           or character == '4' or character == '5' or character == '6' or
             character == '7' or character == '8' or character == '9'):
            pass
        else:
            charChecker=False
    if(charChecker):
        print(len(userInput))
    else:
        print("Вы ввели что-то не то")
    
    