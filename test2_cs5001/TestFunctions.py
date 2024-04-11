"""
    Unit Tests for the Function Questions for CS5001 Final Exam SPRING 2024
"""

import unittest
import os.path
from final import square_series, write_scores, make_upper, make_lower
from final import is_missing, equal_stacks, capitalize, apply_to_all
from Stack import Stack

class TestFunctions(unittest.TestCase):
  
    def test_square_series(self):
        a = []
        square_series(2, a)
        self.assertEqual([1, 4], a)
        
        a = []
        square_series(5, a)
        self.assertEqual([1, 4, 9, 16, 25], a)

        a = [1,1,1]
        square_series(5,a)
        self.assertEqual([1, 4, 9, 16, 25, 1, 1, 1], a)

        a = []
        square_series(1, a)
        self.assertEqual([1], a)

        a = []
        square_series(0, a)
        self.assertEqual([], a)

        a = []
        square_series(-1, a)
        self.assertEqual([], a)

    def test_function_object(self):
        a = ["hEllo", "Goodbye", "what?"]
        apply_to_all(make_upper, a)
        self.assertEqual(['HELLO', 'GOODBYE', 'WHAT?'], a)
        
        a = ["hEllo", "Goodbye", "what?"]
        apply_to_all(make_lower, a)
        self.assertEqual(['hello', 'goodbye', 'what?'], a)
        
        a = ["hEllo", "Goodbye", "what?"]
        apply_to_all(capitalize, a)
        self.assertEqual(['Hello', 'Goodbye', 'What?'], a)

    def test_write_scores(self):
        if os.path.exists("grades.txt"): # prepare for new test. Delete existing
            os.remove("grades.txt")
        write_scores("grades.txt", [88, 99, 100], ["Carrie", "Charity", "Chloe"])
        if not os.path.exists("grades.txt"):
            self.fail("Did not create file properly!")
        result = []
        with open("grades.txt", mode="r", encoding = "utf-8") as file:
            for each in file:
                result.append(each)
        self.assertEqual(result, ["Carrie 88\n", "Charity 99\n", "Chloe 100\n"])

        if os.path.exists("empty.txt"): # prepare for new test. Delete existing
            os.remove("empty.txt")
        write_scores("empty.txt", [], [])
        if not os.path.exists("empty.txt"):
            self.fail("Did not create file properly!")
        result = []
        with open("empty.txt", mode="r", encoding = "utf-8") as file:
            for each in file:
                result.append(each)
        self.assertEqual(result, [])


    def test_is_missing(self):
        self.assertEqual(is_missing([2,3,4]), 1)
        self.assertEqual(is_missing([4,1,3,6,7,2]), 5)
        self.assertEqual(is_missing([4,1,3]), 2)
        self.assertEqual(is_missing([1]), 2)

    def test_equal_stacks(self):
        s1 = Stack()
        s1.push(1)
        s1.push(2)

        s2 = Stack()
        s2.push(1)
        s2.push(2)
        self.assertEqual(equal_stacks(s1, s2), True)

        s1 = Stack()
        s1.push(1)
        s1.push(2)

        s2 = Stack()
        s2.push(1)
        s2.push(2)
        s2.push(3)
        s2.pop()
        self.assertEqual(equal_stacks(s1, s2), True)
        
        s1 = Stack()
        s1.push("Hello")
        s1.push("World")

        s2 = Stack()
        s2.push("World")
        s2.push("Hello")

        self.assertEqual(equal_stacks(s1, s2), False)

        s1 = Stack()
        s2 = Stack()
        self.assertEqual(equal_stacks(s1, s2), True)


if __name__ == "__main__":
    unittest.main(verbosity=3)

