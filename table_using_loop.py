import time
start = time.time()

print("Enter a number :")
n = int(input())

i =1
i2 =10
result =1
print(f"Table of {n} is :")
while i<=i2:
    result=n*i
    print(f"{n}*{i} = {result}")
    i+=1


print("\n")

list_of_number = [32,36,666,32,96,.03,-95,-652,.96685,98,-.032,-552,338,0.0351500000000442]
result2 =0

for sum in list_of_number :
    result2+=sum
print("The sum of the listed number is :")
print(result2)


print("Enter 'start' to start the program either type 'stop' to Stop the program")
trigger = input().lower()

while True:
    if trigger == "stop" :
        print("program stopped")
        break
    elif trigger != "start":
        print("Invalid input, please type 'start' or 'stop' ")
        continue

    print("Enter a year to check :")
    year = int(input())

    if year % 4 == 0 and year%100!=0 or year%400==0 :
        print(f"{year} is a leap year")
    else :
        print(f"{year} is not a leap year")

print("The process is finished ")

end = time.time()
print(f"\nExecution time: {end - start:.4f} seconds")