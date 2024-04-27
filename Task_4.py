ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
print("Эта программа проверяет совпадения введнных вами координат с заданными")
print("Выход из программы - exit")
print(ship+"\n") # для наглядности
while True:
    charCheker = True
    userInput = input("Введите координаты корабля:")
    if(userInput == "exit"):
        break
    userInput = userInput.upper()
    if(len(userInput)==2):
        if (userInput[0] not in['А','Б','В','Г','Д','Е','Ж','З','И','К']  #буквы на доске в игре "Морской бой"
            or userInput[1] not in['1','2','3','4','5','6','7','8','9','0']): 
            charCheker = False
    else:
         print("Координаты введены некорректно")
         continue
    if(charCheker):
        if(ship.find(userInput) >= 0):
            print("Попал")
        elif(ship.find(userInput) == -1):  # метод возвращает -1, когда не может найти совпадение
            print("Мимо")
    else:
        print("Координаты введены некорректно")