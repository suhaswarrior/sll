print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")
print("7. View History")
print("8. Exit")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9


def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67


def view_history(history): # history is a list
    print("1. Sort by From Unit") 
    print("2. Sort by To Unit")

    choice = int(input("Enter your choice: ")) 

    if choice == 1:
        history.sort(key=lambda x: x[0]) # sort by first element of each tuple
    elif choice == 2:
        history.sort(key=lambda x: x[1]) # sort by second element of each tuple
    else:
        print("Invalid Choice")
    for i in history: # print each tuple in history
        print(i)


history = []
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        history.append((celsius, fahrenheit))
        print("Temperature in Fahrenheit: ", fahrenheit)
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        history.append((fahrenheit, celsius))
        print("Temperature in Celsius: ", celsius)
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        history.append((celsius, kelvin))
        print("Temperature in Kelvin: ", kelvin)
    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        history.append((kelvin, celsius))
        print("Temperature in Celsius: ", celsius)
    elif choice == 5:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        history.append((fahrenheit, kelvin))
        print("Temperature in Kelvin: ", kelvin)
    elif choice == 6:
        kelvin = float(input("Enter temperature in Kelvin: "))
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        history.append((kelvin, fahrenheit))
        print("Temperature in Fahrenheit: ", fahrenheit)
    elif choice == 7:
        view_history(history)
    elif choice == 8:
        break
    else:
        print("Invalid Choice")
