#Task 1: Create a program wthat converts temperature between Celsius, fahrenheit and Kelvin scales
# Functions to convert temperatures between different scales

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature(value, from_scale, to_scale):
    if from_scale == 'C':
        if to_scale == 'F':
            return celsius_to_fahrenheit(value)
        elif to_scale == 'K':
            return celsius_to_kelvin(value)
    elif from_scale == 'F':
        if to_scale == 'C':
            return fahrenheit_to_celsius(value)
        elif to_scale == 'K':
            return fahrenheit_to_kelvin(value)
    elif from_scale == 'K':
        if to_scale == 'C':
            return kelvin_to_celsius(value)
        elif to_scale == 'F':
            return kelvin_to_fahrenheit(value)
    else:
        return "Invalid scale input. Please use 'C', 'F', or 'K'."

value = float(input("Enter the temperature value: "))
from_scale = input("Enter the scale to convert from (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
to_scale = input("Enter the scale to convert to (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

converted_value = convert_temperature(value, from_scale, to_scale)

if isinstance(converted_value, str):
    print(converted_value)
else:
    print(f"{value}°{from_scale} is equal to {converted_value:.2f}°{to_scale}")
