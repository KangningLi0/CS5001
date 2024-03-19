"""
Kangning Li
CS 5001 Spring 2024
SimpleFraction.py
"""

class SimpleFraction:
    '''
    This class manages rational numbers, following methods
    are implemented according to the hw requirements
    '''
    def __init__(self, numerator=1, denominator=1):
        '''
        Function -- __init__
            The constructor function give the instance of
            class SimpleFraction
        Parameters:
            numerator -- if no user input it default to 1
            denominator -- if no user input it default to 1
        '''
        if (not isinstance(numerator, int) or
                not isinstance(denominator, int)):
            raise ValueError
        
        if denominator == 0:
            raise ZeroDivisionError
        
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        '''
        Function -- get_numerator
        Returns the numerator of the instance
        '''
        return self.numerator
    
    def get_denominator(self):
        '''
        Function -- denominator
        Returns the denominator of the instance
        '''
        return self.denominator
    
    def make_reciprocal(self):
        '''
        Function -- make_reciprocal
        Returns a new SimpleFraction instance that has the
            current instance's denominator as its numerator.
            and the current instance is not modified
        '''
        return SimpleFraction(self.denominator, self.numerator)
    
    def validate(self):
        '''
        Function -- validate
            Check if the numerator and denominator are integers,
            if either not, this method raises a ValueError
        '''
        if (not isinstance(self.numerator, int) or
                not isinstance(self.denominator, int)):
            raise ValueError
    
    def multiply(self, other):
        '''
        Function -- multiply
            this function multiplies the current instance with
            another SimpleFraction or a whole number
        Parameter:
            other -- SimpleFraction instance or whole number
        Return the multiple result instance
        '''
        if isinstance(other, SimpleFraction):
            n_ret = self.numerator * other.numerator
            d_ret = self.denominator * other.denominator
        elif isinstance(other, int):
            n_ret = self.numerator * other
            d_ret = self.denominator
        
        return SimpleFraction(n_ret, d_ret)
    
    def divide(self, other):
        '''
        Function -- divide
            this function divide the current instance with 
            another SimpleFraction or a whole number
        Parameter:
            other -- SimpleFraction instance or whole number
        Returns the divide result instance
        '''
        if isinstance(other, SimpleFraction):
            n_ret = self.numerator * other.denominator
            d_ret = self.denominator * other.numerator
        elif isinstance(other, int):
            n_ret = self.numerator
            d_ret = self.denominator * other
        
        return SimpleFraction(n_ret, d_ret)
    
    def __str__(self):
        '''
        Function -- __str__
        Returns a string representation of SimpleFraction instances
        '''
        return f"{self.numerator}/{self.denominator}"
    
    def __eq__(self, other):
        '''
        Function -- __eq__
            This function compares current SimpleFraction instance to
            another one
        Parameter:
            other -- another SimpleFraction instance
        Return True if there are equal, False otherwise
        '''
        left = self.numerator / self.denominator
        right = other.numerator / other.denominator
        
        return True if left == right else False