userInput = (input("Введите строку:")).lower()
ourDict = {}
for character in userInput:
    if(character==" "):
        continue
    ourDict[character] = userInput.count(character)
print(ourDict)
input()
