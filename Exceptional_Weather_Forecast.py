# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.
def get_temperature():
    try:
        temperature = input("Please enter the temperature in Fahrenheit: ")
        temperature = float(temperature)
        print(f"The temperatue you entered is: {temperature}°F")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the temperature.")


get_temperature()

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.
# Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

def convert_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except TypeError:
        print("Error: The input must be a number.")
        return None
    

def get_temperature_and_convert():
    try:
        temperature = input("Please enter the temperature in Farenheit: ")
        temperature = float(temperature)
        celcius = convert_to_celsius(temperature)
        if celcius is not None:
            print(f"The temperature in Celsius is: {celcius:.2f}°C")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the temperature.")
# Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
    else:
        celcius = convert_to_celsius(temperature)
        if celcius is not None:
            print(f"{temperature} degrees Fahrenheit is {celcius:.2f} degrees Celcius.")
#Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
    finally:
        print("Thank you for using the weather forecast application!")


get_temperature_and_convert()

