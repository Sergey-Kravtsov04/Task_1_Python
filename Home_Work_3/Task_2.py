def multily_list (lst:list , pow:int = 2):
    tmpLst = []
    for i in lst:
        tmpLst.append(i*pow)
    return tmpLst
lambda_multiply = lambda lst, pow=2: [int(x) * pow for x in lst]

while True:
    ourList = [1, 2, 3, 4, 5]
    print("Наш лист:{0}".format(ourList))
    try:
        ourPow = int(input("Введите число(можете оставить пустым)"))
    except Exception:
        print("Обычная функция:")
        print(multily_list(ourList))
        print("Лямбда функция:")
        print(lambda_multiply(ourList))
        print("Хотите выйти?")
    else: 
        print("Обычная функция:")
        print(multily_list(ourList, ourPow))
        print("Лямбда функция:")
        print(lambda_multiply(ourList, ourPow))
        print("Хотите выйти?")
    breakInput = (input("Y/N:")).lower()
    if(breakInput == 'y'):
        break
    else:
        pass


