"""
Kangning Li
CS 5001 Spring 2024
TestSimpleFraction.py
"""

import unittest
from SimpleFraction import SimpleFraction

class TestMyFunctions(unittest.TestCase):
    '''
    Below are all the test functions for testing
    '''
    def test_constructor(self):
        '''
        Function -- test_constructor
            This function test the constructor of SimpleFraction class
            make sure that without input the numerator and denominator
            should be set to 1 automatically, and if there input a
            non integer number, the __init__ should raise a ValueError
        '''
        fract = SimpleFraction()
        
        # test default value
        self.assertEqual(fract.numerator, 1)
        self.assertEqual(fract.denominator, 1)

        # test ValueError raised
        with self.assertRaises(ValueError):
            fract = SimpleFraction(1.1)
    
    def test_get_numerator_denominator(self):
        '''
        Function -- test_get_numerator_denominator
            This function test the get_numerator() and get_denominator()
            make sure there return the right value in instance domain
        '''
        fract = SimpleFraction(2, 3)

        # test get functions
        self.assertEqual(fract.get_numerator(), 2)
        self.assertEqual(fract.get_denominator(), 3)
    
    def test_make_reciprocal(self):
        '''
        Function -- test_make_reciprocal
            This function test the value of make_reciprocal()
            make sure the right instance that return
            and the original instance not be changed
        '''
        fract = SimpleFraction(2, 3)
        rec_fract = fract.make_reciprocal()

        # test whether original instance doesn't change
        self.assertEqual(fract.get_numerator(), 2)
        self.assertEqual(fract.get_denominator(), 3)

        # test new SimpleFraction instance
        self.assertEqual(rec_fract.get_numerator(), 3)
        self.assertEqual(rec_fract.get_denominator(), 2)

    def test_validate(self):
        '''
        Function -- test_validate
            This function test the validate function work
            if changed the numerator of instance to 1.1
            validate function should raised ValueError
        '''
        fract = SimpleFraction(2, 3)
        fract.numerator = 1.1

        # test validate Error raised
        with self.assertRaises(ValueError):
            fract.validate()
    
    def test_multiply(self):
        '''
        Function -- test_multiply
            This function test the test_multiply function
            make sure whether it multiply with another
            instance or whole number it should return the 
            correct instance and leave the origin unchanged
        '''
        left = SimpleFraction(2, 3)
        right = SimpleFraction(5, 7)
        num = 5

        # test cases
        test1 = left.multiply(right)
        test2 = left.multiply(num)

        # make sure original instance doesn't change
        self.assertEqual(left.get_numerator(), 2)
        self.assertEqual(left.get_denominator(), 3)

        # test result
        self.assertEqual(test1.get_numerator(), 10)
        self.assertEqual(test1.get_denominator(), 21)
        self.assertEqual(test2.get_numerator(), 10)
        self.assertEqual(test2.get_denominator(), 3)

    def test_divide(self):
        '''
        Function -- test_divide
            This function test the test_divide function
            make sure whether it divide with another
            instance or whole number it should return the 
            correct instance and leave the origin unchanged
        '''
        left = SimpleFraction(2, 3)
        right = SimpleFraction(5, 7)
        num = 5

        # test cases
        test1 = left.divide(right)
        test2 = left.divide(num)

        # make sure original instance doesn't change
        self.assertEqual(left.get_numerator(), 2)
        self.assertEqual(left.get_denominator(), 3)

        # test result
        self.assertEqual(test1.get_numerator(), 14)
        self.assertEqual(test1.get_denominator(), 15)
        self.assertEqual(test2.get_numerator(), 2)
        self.assertEqual(test2.get_denominator(), 15)
    
    def test_str(self):
        '''
        Function -- test_str
            This function make sure __str__ function
            return a value type in string
        '''
        fract = SimpleFraction(2, 3)
        self.assertEqual(isinstance(fract.__str__(), str), True)
    
    def test_eq(self):
        '''
        Function -- test_eq
            This function make sure __eq__ function work accordingly
            if input a instance with same value return True
            if input a instance with different value return False
        '''
        fract = SimpleFraction(2, 3)
        target1 = SimpleFraction(4, 6)
        target2 = SimpleFraction(4, 5)

        # test result
        self.assertEqual(fract.__eq__(target1), True)
        self.assertEqual(fract.__eq__(target2), False)

if __name__ == "__main__":
    unittest.main()