def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    while True:
        print("Options:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            converted_temp = celsius_to_fahrenheit(celsius)
            print(str(celsius) + "°C is equal to {:.2f}°F".format(converted_temp))
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            converted_temp = fahrenheit_to_celsius(fahrenheit)
            print(str(fahrenheit) + "°F is equal to {:.2f}°C".format(converted_temp))
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
