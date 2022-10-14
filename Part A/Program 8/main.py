from functools import reduce # for reduce function
list = [] # list to store the numbers
for i in range(0,6): # for loop to take input
    item=int(input("Enter the number "))
    list.append(item)

print("\nThe elements are\n") # printing the elements
print(list)
print("Elements after multiplying are:\n")
newlist = [x*3 for x in list] # list comprehension
print(newlist)
listSum = reduce(lambda a,b:a+b,list) # using reduce function
print("The sum of the original list  is ",listSum) # printing the sum

listSum = reduce(lambda a,b:a+b,newlist) # using reduce function
print("The sum of the original list  is ",listSum) # printing the sum


