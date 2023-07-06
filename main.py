import random

print("로또번호다섯개추첨해!!^^")

for i in range(5) :
    lotto = random.randint((1,46),6)
    print(lotto)    

y = input("다시 추첨하기 원하면 y를 누르세요 :")

if y == "y" :
    lotto = random.sample(range(1,46), 6)
    print(lotto)

