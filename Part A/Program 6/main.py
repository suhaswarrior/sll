atomic_dict = {"H":"Hydrogen", "C":"Carbon", "O":"Oxygen", "N":"Nitrogen"}
while 0==0:
    print("1.Add element")
    print("2.Number of elements present")
    print("3. Search for element")
    print("4. Print the dictionary")
    print("0. Exit")
    n = int(input("Enter your choice: "))
    if n==1:
        atomic_dict[input("Enter the symbol: ")] = input("Enter the name: ")
    elif n==2:
        print("Number of elements present: ",len(atomic_dict))
    elif n==3:
        print(atomic_dict[input("Enter the symbol: ")])
    elif n==4:
        print(atomic_dict)
    elif n==0:
        break
    else:
        print("Invalid choice")

