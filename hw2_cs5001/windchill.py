'''
CS 5001
Spring 2024
Kangning Li
windchill
'''


FAHRENHEIT_BASE = 32

def convert_fahrenheit_to_celsius( temperature ):
    '''
    Function -- convert_fahrenheit_to_celsius
        Converts temperature from F to C
    Parameters:
        temperature (float) -- the original temperature in Fahrenheit
    Returns a float value representing the original temperature converted
        to Celsius
    '''

    return ( temperature - FAHRENHEIT_BASE ) * 5 / 9

def convert_celsius_to_fahrenheit( temperature ):
    '''
    Function -- convert_celsius_to_farenheit
        Converts temperature from C to F
    Parameters:
        temperature (float) -- the original temperature in Celsius
    Returns a float value representing the original temperature converted
        to Fahrenheit
    '''
    
    # parenthesis not needed but add to readability
    return (( temperature / 5 ) * 9) + FAHRENHEIT_BASE

def calculate_windchill( temperature, speed ):
    '''
    Function: calculate_windchill
        Calculates windchill based on international formula (Metric)
    Parameters:
        temperature in Fahrenheit
        speed in miles per hour
    Returns: windchill index (floating point value) based on applied formula
    Require: temp/speed in metric units
    Ensure: metric -> imperial unit conversions prior to calculation
    '''
    temperature_c = convert_fahrenheit_to_celsius(temperature)
    speed_m = speed * 1.61
    index_c = 13.12 + 0.6215 * temperature_c - 11.37 * (speed_m ** 0.16) \
        + 0.3965 * temperature_c * (speed_m ** 0.16)
    return convert_celsius_to_fahrenheit(index_c)

    
