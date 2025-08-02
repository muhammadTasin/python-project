import random

from coinToss import answer

user = ["sayem","sobhan","sakib","tasin"]

randomnum = random.randint(0, 3)
if randomnum == 0 :
    print("bill will pay by Sayem")
elif randomnum == 1 :
    print("bill will pay by Sobhan")
elif randomnum ==2 :
    print("bill will pay by Sakib")
else :
    print("bill will pay by Tasin")

print("=========")  #print side rakhar jonno bug dekha diyechilo that's why sometimes print hoto na ei line ta


   ## method 2
length = len(user) - 1
random2 = random.randint(0, length)
biller = user[random2]
print(f"Bill will pay by {biller}")

#method 3

payer = {'titi','dodo','titi pakhi', 'dodo pakhi'}
payer_list = list (payer)

answer = random.choice(payer_list)
print(answer)