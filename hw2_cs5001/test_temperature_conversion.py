'''
   CS5001
   Spring 2024
   Kangning Li
   Homework 2: Temperature Converter Starter Code
'''
def main():
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

        return (temperature - FAHRENHEIT_BASE) * 5/9

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
        return ((temperature / 5) * 9) + FAHRENHEIT_BASE

    def test_function_f2c(f_tem, expected):
        # convert the fahreheit temp to celsius
        print(f"Converting {f_tem:.1f} F to Celsuius --")
        result = convert_fahrenheit_to_celsius(f_tem)
        print(f">> result = {result:.1f} expected = {expected:.1f}")

    def test_function_c2f(c_tem, expected):
        # convert the celcius temp to fahreheit
        print(f"Converting {c_tem:.1f} C to Fahrenheit --")
        result = convert_celsius_to_fahrenheit(c_tem)
        print(f">> result = {result:.1f} expected = {expected:.1f}")

    test_function_f2c(32.0, 0)
    test_function_f2c(100.0, 37.8)
    test_function_f2c(212.0, 100.0)
    test_function_f2c(85.1, 29.5)
    test_function_c2f(0.0, 32.0)
    test_function_c2f(37.8, 100.0)
    test_function_c2f(100.0, 212.0)

if __name__ == "__main__":
    main()
    
    
