n = int(input("Enter the size in the list:"))
List = [0]*n
for i in range(0, n):
    List[i] = int(input("Enter the element:"))
print("The list is:", List)
print("Enter the number to be appended:")
List.append(int(input()))
print("The list after appending is:", List)
print("The max element in the list is ", max(List))
print("The min element in the list is ", min(List))
print("Enter the element to be searched:")
if int(input()) in List:
    print("Element found")
else:
    print("Element not found")
print("Enter the index number to be deleted ")
del List[int(input())]
