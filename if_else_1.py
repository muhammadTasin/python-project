print ("dear student enter ur roll : ")
roll = input()
print()

print(f"dear user {roll} please input your numbers : ")
num = int(input())

print()

if num>=90 and num<=100 :
    print('you got A+ ')
elif num <90 and  num>=80:
    print("you got A")
elif num< 80 and num >=70 :
    print("you got A-")
elif num<70 and num>=60 :
    print("You got B+")
elif num<60 and num>=50 :
    print("you got B-")
elif 50 > num > 0:
    print("Sorry u are fail ")
else :
    print("invalid input olease enter a posetive number insted of negative number ")

print()

avg = ((num*5)/500)*5
#print (f"your cgpa is {avg}")
print (f"your cgpa is {avg}")


