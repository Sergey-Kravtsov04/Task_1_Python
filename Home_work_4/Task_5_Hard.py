class CardDeckIter:
    def __init__(self,iter_count:int,list:list):
        self.iters_cont = iter_count-1  #Длина листа напрямую связана с счётчиком, поэтому из нее вычитаем единицу, чтобы не выходить за границу
        self.count = -1  #К счётчику прибавляется единичка в начале итерации(до return). Первый индекс должен быть == 0
        self.list = list
    def __iter__(self):
        return self
    def __next__(self):
        if(self.count<self.iters_cont):
            self.count +=1
            return self.list[self.count]
        else:
            raise StopIteration
#
cardSuit = ["Бубей", "Червей", "Пик","Треф"]
cardAdvantge = ['2','3','4','5','6','7','8','9','10','Валет','Дама','Король','Туз']
cardDeck = []
cardIter = CardDeckIter(len(cardSuit),cardSuit)
# cardIterLower =CardDeckIter(len(CardAdvantge),CardAdvantge)  #При "прокрутке" итератора один раз, останавливается из-за StopIteration. 
for suit in cardIter:  #"Собираем" колоду
    for advantage in CardDeckIter(len(cardAdvantge),cardAdvantge):  
        cardDeck.append(f"{advantage} {suit}")
allCard =CardDeckIter(len(cardDeck),cardDeck)
#
count = 0
for card in allCard:
    print(card)
    count+=1
print(f"Общее кол-во карт:{count}")
input()