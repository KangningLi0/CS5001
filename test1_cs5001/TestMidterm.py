"""
    CS 5001 Midterm Test Suite SPRING 2024

"""

import unittest
import io, contextlib
import os
from os.path import exists

import midterm


class TestMidterm(unittest.TestCase): 
    def test_every_other(self):
        a = [1,2,3,4,5]
        midterm.every_other(a)
        self.assertEqual(a, [1,4,3,8,5], msg="Failed Every other 1,2,3,4,5")

        a = ["hi", "oo", "ah"]
        midterm.every_other(a)
        self.assertEqual(a, ["hi","oooo", "ah"], msg="Failed every other strings")

        a = [1,[2,3],1]
        midterm.every_other(a)
        self.assertEqual(a, [1,[2,3,2,3],1], msg="Failed Every other [1,[2,3],1")

        a = []
        midterm.every_other(a)
        self.assertEqual(a, [], msg="Failed Every other []")

        a = [1]
        midterm.every_other(a)
        self.assertEqual(a, [1], msg="Failed Every other [1]")


    def test_word_play(self):          

        a = ["hello world", "jelly belly", "hit the high hat", "zero zip zonk"]
        expected = ['jello world', 'helly belly', 'jit tje jigj jat', 'zero zip zonk']
        midterm.word_play(a, "h", "j")
        self.assertEqual(expected, a )

        a = ["hello world", "jelly belly", "hit the high hat", "zero zip zonk"]
        midterm.word_play(a, "h", "z")
        expected = ['zello world', 'jelly belly', 'zit tze zigz zat', 'hero hip honk']
        self.assertEqual(expected, a )
        
    def test_resequencing(self):
        a = []
        self.assertEqual(midterm.resequencing(a), "")
        self.assertEqual(a, []) # a not mutated

        a = [1]
        self.assertEqual(midterm.resequencing(a), "1")
        self.assertEqual(a, [1]) # confirm a not mutated

        a = [5, 3, 4, 10, 1]
        self.assertEqual(midterm.resequencing(a), "1 3 4 5 10")
        self.assertEqual(a, [5,3,4,10,1])

        a = ["every", "good", "boy", "does", "fine"]
        self.assertEqual(midterm.resequencing(a), "boy does every fine good")
        self.assertEqual(a, ["every", "good", "boy", "does", "fine"])

    def test_identify(self):
        self.assertEqual((midterm.identify(4111111111111111)).lower(), "visa")
        self.assertEqual(
            (midterm.identify(5431111111111111)).lower(), "mastercard")
        self.assertEqual(
            (midterm.identify(371111111111114)).lower(), "american express")
        self.assertEqual(
            (midterm.identify(36000000000008)).lower(), "diners club")
        self.assertEqual((midterm.identify(6011111111111117)).lower(), "discover")
        self.assertEqual((midterm.identify(3562350000000003)).lower(), "jcb")
        self.assertEqual((midterm.identify(4111111111111)).lower(), "visa")
        self.assertEqual((midterm.identify(8711111111111111)).lower(), "unknown")
        self.assertEqual((midterm.identify(41111111111)).lower(), "unknown")


    def test_flipper(self):
        a = []
        b = midterm.flipper(a)
        self.assertEqual(a, []) # a is not mutated
        self.assertEqual(a, [])

        a = [True]
        b = midterm.flipper(a)
        self.assertEqual(b, [False])
        self.assertEqual(a, [True]) # a is not mutated

        a = [False]
        b = midterm.flipper(a)
        self.assertEqual(b, [True])
        self.assertEqual(a, [False])

        a = [True, False, True]
        b = midterm.flipper(a)
        self.assertEqual(b, [False, True, False])
        self.assertEqual(a, [True, False, True])

        
if __name__ == "__main__":
    unittest.main()
