FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        print("Temperature below absolute zero is not possible.")
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    if celsius < -273.15:
        print("Temperature below absolute zero is not possible.")
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = input("Enter temperature: ")
unit = input("Is this temperature in celcius or fahrenheit? (C/F): ")
if unit.lower() == 'c' and temperature.isdigit():
    converted_temp = convert_to_fahrenheit(float(temperature))
    print(f"{temperature}°C is {converted_temp:.2f}°F")
elif unit.lower() == 'f' and temperature.isdigit():
    converted_temp = convert_to_celsius(float(temperature))
    print(f"{temperature}°F is {converted_temp:.2f}°C")
else:
    print("Invalid. Please enter a valid temperature and unit.")
