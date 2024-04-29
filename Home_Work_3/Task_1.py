def sum(x:int,y:int):
    return x+y
def min(x:int,y:int):
    return x-y
def umn(x:int,y:int):
    return x*y
def del1(x:int,y:int):
    try:
        return x/y
    except ZeroDivisionError as e:
        print(e)
def step(x:int,y:int):
    return x**y
def exit():
    return False
isOpen = True
while isOpen:
    print("""Выберите операцию:
          1. Сложение
          2. Вычитание
          3. Умножение
          4. Деление
          5. Возведение в степень
          6. Выход""")
    userInput = input("Введите номер операции:")
    if(userInput == '6'):
        isOpen = exit()
    elif(userInput.isdigit() and userInput in ['1','2','3','4','5']):  #проверка ввода операции
        firstNum = (input("Введите первое число:")) 
        secondNum = (input("Введите второе число:"))
        if(firstNum.isdigit() and secondNum.isdigit()):  #Проверка введенных чисел(это дополнительно)
            if(userInput =='1'):
                print(f"{firstNum} + {secondNum} =",sum(int(firstNum),int(secondNum)))
            elif(userInput =='2'):
                print(f"{firstNum} - {secondNum} =",min(int(firstNum),int(secondNum)))
            elif(userInput =='3'):
                print(f"{firstNum} * {secondNum} =",umn(int(firstNum),int(secondNum)))
            elif(userInput =='4'):
                print(f"{firstNum} / {secondNum} =",del1(int(firstNum),int(secondNum)))
            elif(userInput =='5'):
                print(f"{firstNum} ** {secondNum} =",step(int(firstNum),int(secondNum)))
                #Я не совсем понимаю зачем эта проверка, если мы вводим числа как строки, проверяем числа ли они и преобразуем их в int, в случае True
                #Если поставить int на input, то в этом вообще смысла нет, так как оно вылетит при вводе другого типа данных
                #Может try-exception нужен, но по условиям его здесь быть не должно
                #В любом случае, я показал, что могу пользоваться этим инструментом 
        elif not (isinstance(firstNum,int) or isinstance(secondNum, int)):  #ValidationError нет по непонятным причинам
            raise ValueError("Wrong DataType")
    else:
        print("Некорректный номер операции")
input()