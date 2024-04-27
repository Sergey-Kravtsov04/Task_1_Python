isOpen = True
print("Эта программа выведет вам длину введённого числа")
print("Для выхода введите - exit\n")
while isOpen:
    charChecker = True
    userInput = (input("Введите число:"))
    if(userInput=="exit"):
        isOpen=False
    for ch in userInput:
        if(ch == '0' or ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or
           ch == '8' or ch == '9'):
            pass
        else:
            charChecker=False
    if(charChecker):
        print(len(userInput))
    else:
        print("Вы ввели что-то не то")
    
    