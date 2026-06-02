number = int(input("Enter how long number do you want to take ? : "))

max = -99999999
min =  99999999

array = []
secoendMax =0
for i in range(number) :
    element = int(input("Enter the elements : "))
    array.append(element)

for i in array :
    if i>max :
        max =i
         
    if i<min :
        min =i
    if array[i] == max:
        for i in array[i+1] :
            if array[i+1]>min :
                secoendMax = array[i+1]

print(f"the max number is : {max}")
print(f"the min number is : {min}")
print()
print(f"2nd max number is : {secoendMax}")

