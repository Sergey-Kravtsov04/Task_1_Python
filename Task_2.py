while True:
    ourList=[]
    negativeSum = 0
    positiveSum = 0
    charChecker=True
    userInput = (input("Введите положительное натуральное число:"))
    for ch in userInput:
        if(ch == '0' or ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or
           ch == '8' or ch == '9'):
            None
        else:
            charChecker=False
    if( charChecker==False):
        print("Что-то не так, попробуйте заново")
        continue
    userInput= int(userInput)
    for i in range(-userInput,userInput+1):
        ourList.append(i)
    print(ourList)
    for number in ourList:
        if(number>0):
            positiveSum+= number
        elif(number<0):
            negativeSum+=number
        else:
            None
    print(f"Сумма отрицательных чисел:{negativeSum}")
    print(f"Сумма положительных чисел:{positiveSum}")