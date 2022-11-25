print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")
print("7. Exit")


def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print("%.2f Celsius is: %.2f Fahrenheit" %(celsius, fahrenheit))


def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print("%.2f Fahrenheit is: %.2f Celsius" %(fahrenheit, celsius))


def celsius_to_kelvin():
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = celsius + 273.15
    print("%.2f Celsius is: %.2f Kelvin" %(celsius, kelvin))


def kelvin_to_celsius():
    kelvin = float(input("Enter temperature in Kelvin: "))
    celsius = kelvin - 273.15
    print("%.2f Kelvin is: %.2f Celsius" %(kelvin, celsius))


def fahrenheit_to_kelvin():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    kelvin = (fahrenheit + 459.67) * 5/9
    print("%.2f Fahrenheit is: %.2f Kelvin" %(fahrenheit, kelvin))


def kelvin_to_fahrenheit():
    kelvin = float(input("Enter temperature in Kelvin: "))
    fahrenheit = kelvin * 9/5 - 459.67
    print("%.2f Kelvin is: %.2f Fahrenheit" %(kelvin, fahrenheit))


while 0==0:
    print("Enter choice: ")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        celsius_to_fahrenheit()
    elif choice == 2:
        fahrenheit_to_celsius()
    elif choice == 3:
        celsius_to_kelvin()
    elif choice == 4:
        kelvin_to_celsius()
    elif choice == 5:
        fahrenheit_to_kelvin()
    elif choice == 6:
        kelvin_to_fahrenheit()
    elif choice == 7:
        exit()
    else:
        print("Invalid choice")
