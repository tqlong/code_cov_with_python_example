import unittest
from dice_package.dice import Die, DiceBag

class TestDie(unittest.TestCase):

    def setUp(self):
        self.die = Die()
        self.die_bag = DiceBag([2,4,6])

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_roll(self):
        self.assertTrue(self.die.roll() in range(1,7))

    def test_create_dice_from_sides(self):
        for dice in self.die_bag.dice:
            self.assertTrue(isinstance(dice, Die))
            self.assertTrue(dice.sides in [2,4,6])

    def test_roll_bag(self):
        for sides, roll in zip([2,4,6], self.die_bag.roll_bag()):
            self.assertTrue(roll in range(1,sides+1))