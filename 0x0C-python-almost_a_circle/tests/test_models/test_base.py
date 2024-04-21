#!/usr/bin/python3

"""Base class unit tests module"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test the base class"""
    def setUp(self):
        """Reset the __nb_object attribute to zero before every tests"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass

    def test_attribute(self):
        """test if attribute exists"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_init(self):
        """Test the the the nb_objects attributes is zero
        if no new object has been created"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_init2(self):
        """Test the the the nb_objects attributes remains zero
        if no void object has been created"""

        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)


    def test_id_increment(self):
        """Test that every time a new object is created
        the instance id attribute increases by 1"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b2.id + 1, b3.id)

    def test_id_increament_2(self):
        """Test that the Base object id only increases
        when no value/object is passed"""
        b1 = Base()
        b2 = Base("Hey!")
        b3 = Base(33)
        b4 = Base(True)
        b5 = Base([1, 2, 3])
        b6 = Base()
        self.assertEqual(b6.id, 2)

    def test_id_explicit_values(self):
        """Test that the id attribute of an instance created
        is literally what is passed into it"""
        b0 = Base(0)
        bp_33 = Base(33)
        bn_27 = Base(-27)
        self.assertEqual(b0.id, 0)
        self.assertEqual(bp_33.id, 33)
        self.assertEqual(bn_27.id, -27)

if __name__ == "__main__":
    unittest.main()
