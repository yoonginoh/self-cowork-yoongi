import random

print("로또번호다섯개추첨합시다!!!^^")

for i in range(5) :
    lotto = random.randint((1,46),6)
    print(lotto)    
