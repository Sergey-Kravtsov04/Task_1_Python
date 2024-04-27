dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
# dctKeys = set(dct.keys())
# dctValues = set(dct.values()) #Можно так сделать
dctKeys = set()
dctValues = set()
for key, value in dct.items():
    dctKeys.add(key)
    dctValues.add(value)
print("Изначальный словарь:{0}".format(dct))
print("Множество с ключами:{0}".format(dctKeys))
print("Множество со значениями:{0}".format(dctValues))
coolSet = dctKeys|dctValues #По итогам у нас не будет повторяющихся значений, так как это множество
print("Итог объединения двух множеств:{0}".format(coolSet))
input()