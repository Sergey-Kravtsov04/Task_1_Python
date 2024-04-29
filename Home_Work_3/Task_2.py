def umn_func(x:list , y:int=2 ):
    for i in x:
        i=i*y
        print(i)
        return x
l:list=[1,23,455]
num: int = 2
print(umn_func(l,num))