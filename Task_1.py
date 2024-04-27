isOpen = True
while isOpen:
    charChecker = True
    print("Выход-exit")
    userInput = (input("Введите число:"))
    for ch in userInput:
        if(ch == '0' or ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or
           ch == '8' or ch == '9'):
            pass
        else:
            charChecker=False
    if(charChecker):
        print(len(userInput))
    elif(userInput=="exit"):
        isOpen=False
    else:
        print("Ну ерунду ввёл какую-то")
    
    