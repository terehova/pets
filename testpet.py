import unittest

from pets import *

class TestPets(unittest.TestCase):

    def test_cats(self):
        cat = Cat(name='Kitty', hates_dogs=True)

        self.assertEqual("Kitty", cat.name)

    def test_dogs(self):
        dog = Dog(name='Bars',chases_cats=True)
        self.assertEqual(True, dog.chases_cats)

     def test_cats(self):
        cat = Cat (name='Kitty', hates_dogs=True)
        self.assertEqual(True, cat.hates_dogs)

    def test_cats(self):
        cat = Cat (name='Kitty', say_smth=True)
        self.assertEqual(True, cat.say_smth)
          

if __name__=='__main__':
    unittest.main()
