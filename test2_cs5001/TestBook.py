import unittest
from final import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.dracula = Book("Dracula", "Bram Stoker", "HPE", 20.99)
        self.fahrenheit = Book("Fahrenheit 451", "Ray Bradbury", "PE", 15)
        self.pride = Book("Pride and Prejudice", "Jane Austen", "HP", 50)
        self.body = Book("The Three-Body Problem", "Cixin Liu", "E", 10)

        self.spidey = Book("The Spider-Man Compendium", "Stan Lee", "HPE", 42)

    def test_availability(self):
        self.assertTrue(self.dracula.is_available_as("hardcover"))
        self.assertTrue(self.dracula.is_available_as("H"))
        self.assertFalse(self.body.is_available_as("hardcover"))
        self.assertFalse(self.pride.is_available_as("electronic"))
        self.assertTrue(self.spidey.is_available_as("e"))
        self.assertTrue(self.fahrenheit.is_available_as("paperback"))
        self.assertTrue(self.dracula.is_available_as("p"))


    def test_get_base_cost(self):
        self.assertAlmostEqual(20.99, self.dracula.get_base_cost(), "Wrong Base Cost", 0.001)
        self.assertEqual(50, self.pride.get_base_cost(), "Wrong Base Cost")

    def test_to_string(self):
        self.assertEqual("THE THREE-BODY PROBLEM:CIXIN LIU:10", self.body.__str__())
        self.assertEqual("DRACULA:BRAM STOKER:20.99", self.dracula.__str__())


    def test_equals(self):
        self.assertEqual(self.body, self.body)
        self.assertNotEqual(self.dracula, self.body)
        drac = Book("drAcuLA", "BrAM STOKer", "HPE", 20.99)
        
        self.assertEqual(drac, self.dracula)

    def test_get_prices(self):
        self.assertEqual(7, self.body.get_price_for(1, "E"))
        self.assertEqual(450, self.pride.get_price_for(10, "P"))
        self.assertEqual(600, self.pride.get_price_for(10, "H"))
        self.assertEqual(0, self.body.get_price_for(0, "E"))
        self.assertEqual(0, self.body.get_price_for(1, "H")) # not available
        
    def test_bad_values(self):
        with self.assertRaises(ValueError):
            book = Book("", "Keith", "HPE", 100)

    def test_bad_values_2(self):
        with self.assertRaises(ValueError):
            book = Book("The Opus!", "Keith", "HPE", -1)

    def test_bad_values_3(self):
        with self.assertRaises(ValueError):
            book = Book("The Opus!", "Keith", "HPE", 200.01)

            
    def test_set_bad_price(self):
        with self.assertRaises(ValueError):
            book = Book("The Opus!", "Keith", "HPE", 100)
            book.get_price_for(51, "P")

    def test_set_bad_price_2(self):
        with self.assertRaises(ValueError):
            book = Book("The Opus!", "Keith", "HPE", 100)
            book.get_price_for(-1, "H")


    

if __name__ == "__main__":
    unittest.main(verbosity=3)

