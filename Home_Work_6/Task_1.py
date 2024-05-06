def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)
#
assert average_num([1,2,3,4]) == 2.5
assert average_num([3.5,6.5,11]) == 7
assert average_num([9,True]) == 5
assert average_num([12,'4']) == 8
assert average_num((1,4,7)) == 4
assert average_num([1,1]) == True
assert average_num({1,2,3,4,5}) == 3
assert average_num({0:1,1:2,2:3}) == 2 
assert average_num(1) == 1
assert average_num([[1,2,3],4,5]) == 3
assert average_num([2,"8*"]) == 5
