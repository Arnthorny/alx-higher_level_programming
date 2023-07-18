#!/usr/bin/python3
"""
Unittest for models.rectangle([..])

This module contains the required tests
for the specified module
"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
import models.square
from models.square import Square


class TestAllSquareDocstrings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def setUp(self):
        self.s0 = Square(5)

    def testModuleDocstring(self):
        self.assertGreater(len(models.square.__doc__), 1)

    def testClassDocstring(self):
        self.assertGreater(len(Square.__doc__), 1)

    def testStrFnDocstring(self):
        self.assertGreater(len(self.s0.__str__.__doc__), 1)

    def testUpdateFnDocstring(self):
        self.assertGreater(len(self.s0.update.__doc__), 1)

    def testToDictionaryFnDocstring(self):
        self.assertGreater(len(self.s0.to_dictionary.__doc__), 1)


class TestSquareInit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls._Idcheck = 0

    def setUp(self):
        self.s0 = Square(7)
        type(self)._Idcheck += 1

    def test_Size(self):
        self.assertEqual(self.s0.size, 7)

    def test_AllDefaultValues(self):
        self.assertEqual(self.s0.x, 0)
        self.assertEqual(self.s0.y, 0)
        self.assertEqual(self.s0.id, type(self)._Idcheck)

    def test_AllArgs(self):
        self.s0 = Square(4, 5, 8, 14)
        self.assertEqual(self.s0.size, 4)
        self.assertEqual(self.s0.x, 5)
        self.assertEqual(self.s0.y, 8)
        self.assertEqual(self.s0.id, 14)

    def test_ThreeArgs(self):
        type(self)._Idcheck += 1
        self.s0 = Square(6, 11, 4)
        self.assertEqual(self.s0.size, 6)
        self.assertEqual(self.s0.x, 11)
        self.assertEqual(self.s0.y, 4)
        self.assertEqual(self.s0.id, type(self)._Idcheck)

    def test_InvalidArgs(self):
        with self.assertRaises(TypeError):
            self.s0 = Square()
        with self.assertRaises(TypeError):
            self.s0 = Square(8, 4, 5, 6, 7)


class TestSquareValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test_InvalidTypes(self):
        with self.assertRaises(TypeError) as e:
            s1 = Square("5", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            s1 = Square(2.57, 8)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            s1 = Square(5, "x", 7)
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            s1 = Square(9, 12, "2y")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_InvalidDimension(self):
        with self.assertRaises(ValueError) as e:
            s1 = Square(-5, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            s1 = Square(15, -61, 2)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            s1 = Square(6, 15, -8, 11)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_ZeroDimension(self):
        with self.assertRaises(ValueError) as e:
            s1 = Square(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")


class TestSquareArea(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testArea(self):
        s1 = Square(5, 3, 4, 5)
        self.assertEqual(s1.area(), 25)

        s1 = Square(2, 4)
        self.assertEqual(s1.area(), 4)

        s1 = Square(6, 3, 5)
        self.assertEqual(s1.area(), 36)

    def testInvalidArea(self):
        s1 = Square(5, 1)
        with self.assertRaises(TypeError):
            s1.area(5)


class TestSquareDisplayFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testDisplay(self):
        s1 = Square(3, 4)
        with patch("sys.stdout", new=StringIO()) as mock_print:
            s1.display()
            self.assertEqual(mock_print.getvalue(),
                             "    ###\n    ###\n    ###\n")

    def testDisplay2(self):
        s1 = Square(2, y=3)
        with patch("sys.stdout", new=StringIO()) as mock_print:
            s1.display()
            self.assertEqual(mock_print.getvalue(),
                             "\n\n\n##\n##\n")

    def testDisplay3(self):
        s1 = Square(3, 2, 1, 21)
        with patch("sys.stdout", new=StringIO()) as mock_print:
            s1.display()
            self.assertEqual(mock_print.getvalue(),
                             "\n  ###\n  ###\n  ###\n")

    def testDisplay4(self):
        s1 = Square(2, 3, 5, 2)
        with patch("sys.stdout", new=StringIO()) as mock_print:
            s1.display()
            self.assertEqual(mock_print.getvalue(),
                             "\n\n\n\n\n   ##\n   ##\n")

    def testInvalidArg(self):
        s1 = Square(5, 8)
        with self.assertRaises(TypeError):
            s1.display(4)


class TestSquareStrMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testStr(self):
        s1 = Square(4, 7, 3, 9)
        self.assertEqual(str(s1), "[Square] (9) 7/3 - 4")

    def testPrint(self):
        s1 = Square(1, 4, 6, 8)
        with patch("sys.stdout", new=StringIO()) as mock_print:
            print(s1)
            self.assertEqual(mock_print.getvalue(), "[Square] (8) 4/6 - 1\n")


class TestSquareUpdateMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testUpdate0Args(self):
        s1 = Square(6, 9, 3, 11)
        s1.update()

    def testUpdate1Arg(self):
        s1 = Square(4, 7, 3, 34)
        self.assertEqual(s1.y, 3)
        s1.update(12)
        self.assertEqual(s1.id, 12)

    def testUpdate2Args(self):
        s1 = Square(4, 7, 3)
        self.assertEqual(s1.id, Base._Base__nb_objects)
        s1.update(2, 5)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 5)

    def testUpdate3Args(self):
        s1 = Square(11, 5)
        s1.update(7, 6, 12)
        self.assertEqual(s1.id, 7)
        self.assertEqual(s1.size, 6)
        self.assertEqual(s1.x, 12)

    def testUpdate4Args(self):
        s1 = Square(11, 5, 7)
        self.assertEqual(s1.y, 7)
        s1.update(4, 9, 2, 8)
        self.assertEqual(s1.id, 4)
        self.assertEqual(s1.size, 9)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 8)


class TestInvalidUpdate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testInvalidUpdateArg2(self):
        s1 = Square(7, 5, 12)
        with self.assertRaises(TypeError) as e:
            s1.update(12, "5", 5, 11)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.update(14, 0, 5, 11)
        self.assertEqual(str(e.exception), "width must be > 0")

    def testInvalidUpdateArg4(self):
        s1 = Square(11, 14, 3, 5)
        with self.assertRaises(TypeError) as e:
            s1.update(31, 5, None, 6)
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.update(19, 12, -17, 5)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def testInvalidUpdateArg5(self):
        s1 = Square(7, 4, 1, 8)
        with self.assertRaises(TypeError) as e:
            s1.update(11, 5, 5, 3.56)
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.update(19, 12, 5, -5)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def testInvalidUpdateArg6(self):
        s1 = Square(7, 4, 1, 8)
        s1.update(11, 5, 4, 3, 7, 9)
        self.assertEqual(s1.id, 11)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 3)


class TestAdvancedSquareUpdateMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testUpdate1Kwrg(self):
        s1 = Square(4, 7, 3, 9)
        self.assertEqual(s1.size, 4)
        s1.update(size=12)
        self.assertEqual(s1.size, 12)

    def testUpdate2Kwrgs(self):
        s1 = Square(4, 7, 3)
        self.assertEqual(s1.id, Base._Base__nb_objects)
        s1.update(x=2, id=5)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.x, 2)

    def testUpdate3Kwrgs(self):
        s1 = Square(11, 5)
        s1.update(y=7, id=6, size=12)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.y, 7)
        self.assertEqual(s1.size, 12)

    def testUpdate4Kwrgs(self):
        s1 = Square(11, 5, 7)
        self.assertEqual(s1.x, 5)
        s1.update(x=4, y=9, id=8, size=2)
        self.assertEqual(s1.id, 8)
        self.assertEqual(s1.y, 9)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 4)

    def testUpdate5Kwrgs(self):
        s1 = Square(5, 11)
        self.assertEqual(s1.size, 5)

        s1.update(size=6, x=5, id=3, y=11)
        self.assertEqual(s1.size, 6)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.id, 3)
        self.assertEqual(s1.y, 11)


class TestAdvancedUpdateMethod2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test1UpdateKwrgAndArg(self):
        s1 = Square(7, 13)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 13)

        s1.update(12, 34, size=15, id=21)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s1.size, 34)
        self.assertEqual(s1.y, 0)

    def test2UpdateKwrgAndArg(self):
        s1 = Square(14, 9)
        self.assertEqual(s1.size, 14)
        self.assertEqual(s1.x, 9)

        s1.update(17, 25, 19, 9, x=5, y=11, id=11, size=23)
        self.assertEqual(s1.size, 25)
        self.assertEqual(s1.id, 17)
        self.assertEqual(s1.x, 19)
        self.assertEqual(s1.y, 9)

    def test3UpdateKwrgAndArg(self):
        s1 = Square(13, 19)
        self.assertEqual(s1.size, 13)
        self.assertEqual(s1.x, 19)

        s1.update(29, x=5, y=11, id=11, size=23)
        self.assertEqual(s1.size, 13)
        self.assertEqual(s1.id, 29)
        self.assertEqual(s1.x, 19)
        self.assertEqual(s1.y, 0)

    def test4UpdateKwrgAndArg(self):
        s1 = Square(4, 7, 9, 12)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.id, 12)

        s1.update(29, 32, x=5, y=11, id=11, size=23)
        self.assertEqual(s1.size, 32)
        self.assertEqual(s1.id, 29)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 9)

    def test5UpdateKwrgAndArg(self):
        s1 = Square(4, 7, 9)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.y, 9)

        s1.update(23, 3, x=5, y="11", id=11, size=23)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.id, 23)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 9)


class TestInvalidSquareKwargUpdate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testInvalidUpdateKwrg2(self):
        s1 = Square(7, 5, 12)
        with self.assertRaises(TypeError) as e:
            s1.update(size="2", y=5, x=11)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.update(x=32, size=-2, y=5)
        self.assertEqual(str(e.exception), "width must be > 0")

    def testInvalidUpdateKwrg3(self):
        s1 = Square(14, 3, 5, 16)
        with self.assertRaises(TypeError) as e:
            s1.update(size=31, y=6, x=None)
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.update(size=19, x=-12, id=5, y=17)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def testInvalidUpdateKwrg4(self):
        s1 = Square(7, 4, 1, 8)
        with self.assertRaises(TypeError) as e:
            s1.update(x=11, id=5, y=5.23, size=3)
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.update(x=12, y=-5, id=17, size=5)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def testInvalidUpdateKwrg6(self):
        s1 = Square(7, 1, 8, 2)
        s1.update(x=11, id=5, diag=5, size=3)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.x, 11)
        self.assertEqual(s1.y, 8)


class TestSquareToDictionaryRep(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testToDictionary(self):
        s1 = Square(5, 3)
        self.assertEqual(s1.to_dictionary(),
                         {'size': 5, 'x': 3, 'y': 0,
                         'id': Base._Base__nb_objects})

    def testToDictionary2(self):
        s1 = Square(3, 9, 13, 27)
        self.assertCountEqual(list(s1.to_dictionary().items()),
                              list({'size': 3, 'x': 9,
                                    'y': 13, 'id': 27}.items()))

    def testToDictionaryInvalidArg(self):
        s1 = Square(4, 3, 9, 27)
        with self.assertRaises(TypeError):
            s1.to_dictionary(5)
