def sum(x:int,y:int):
    return x+y
def subtract(x:int,y:int):
    return x-y
def multiply(x:int,y:int):
    return x*y
def divide(x:int,y:int):
    try:
        return x/y
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
def pow(x:int,y:int):
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
        try:
            firstNum = int(input("Введите первое число:")) 
            secondNum = int(input("Введите второе число:"))
            if(userInput =='1'):
                print(f"{firstNum} + {secondNum} =",sum(firstNum,secondNum))
            elif(userInput =='2'):
                print(f"{firstNum} - {secondNum} =",subtract(firstNum, secondNum))
            elif(userInput =='3'):
                print(f"{firstNum} * {secondNum} =",subtract(firstNum,secondNum))
            elif(userInput =='4'):
                print(f"{firstNum} / {secondNum} =",divide(firstNum,secondNum))
            elif(userInput =='5'):
                print(f"{firstNum} ** {secondNum} =",pow(firstNum,secondNum))
        except Exception:
            print("Invalid Data type")
input()
