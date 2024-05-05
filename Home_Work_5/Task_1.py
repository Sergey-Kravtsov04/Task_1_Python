import random as rnd
#
def random_el(l:list):
    new_list = []
    for i in range(2):
        new_list.append(rnd.choice(l))
    return new_list
#
list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]
print(random_el(list_el))