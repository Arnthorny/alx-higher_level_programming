#!/usr/bin/python3
"""
Unittest for models.rectangle([..])

This module contains the required tests
for the specified module
"""

import unittest
from unittest.mock import patch
from io import StringIO
import models.rectangle
from models.rectangle import Rectangle
from models.base import Base


class TestAllRectangleDocstrings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def setUp(self):
        self.r0 = Rectangle(2, 5)

    def testModuleDocstring(self):
        self.assertGreater(len(models.rectangle.__doc__), 1)

    def testClassDocstring(self):
        self.assertTrue(hasattr(models.rectangle, "Rectangle"))
        self.assertGreater(len(Rectangle.__doc__), 1)

    def testAreaFnDocstring(self):
        self.assertTrue(hasattr(self.r0, "area"))
        self.assertGreater(len(self.r0.area.__doc__), 1)

    def testDisplayFnDocstring(self):
        self.assertTrue(hasattr(self.r0, "display"))
        self.assertGreater(len(self.r0.display.__doc__), 1)

    def testStrFnDocstring(self):
        self.assertTrue(hasattr(self.r0, "__str__"))
        self.assertGreater(len(self.r0.__str__.__doc__), 1)

    def testUpdateFnDocstring(self):
        self.assertTrue(hasattr(self.r0, "update"))
        self.assertGreater(len(self.r0.update.__doc__), 1)

    def testToDictionaryFnDocstring(self):
        self.assertTrue(hasattr(self.r0, "to_dictionary"))
        self.assertGreater(len(self.r0.to_dictionary.__doc__), 1)


class TestRectangleInit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls._Idcheck = 0

    def setUp(self):
        self.r0 = Rectangle(2, 5)
        type(self)._Idcheck += 1

    def test_WidthAndHeight(self):
        self.assertEqual(self.r0.width, 2)
        self.assertEqual(self.r0.height, 5)

    def test_AllDefaultValues(self):
        self.assertEqual(self.r0.x, 0)
        self.assertEqual(self.r0.y, 0)
        self.assertEqual(self.r0.id, type(self)._Idcheck)

    def test_AllArgs(self):
        self.r0 = Rectangle(4, 2, 5, 8, 14)
        self.assertEqual(self.r0.width, 4)
        self.assertEqual(self.r0.height, 2)
        self.assertEqual(self.r0.x, 5)
        self.assertEqual(self.r0.y, 8)
        self.assertEqual(self.r0.id, 14)

    def test_ThreeArgs(self):
        type(self)._Idcheck += 1
        self.r0 = Rectangle(6, 11, 4)
        self.assertEqual(self.r0.width, 6)
        self.assertEqual(self.r0.height, 11)
        self.assertEqual(self.r0.x, 4)
        self.assertEqual(self.r0.y, 0)
        self.assertEqual(self.r0.id, type(self)._Idcheck)

    def test_FourArgs(self):
        type(self)._Idcheck += 1
        self.r0 = Rectangle(5, 12, 7, 33)
        self.assertEqual(self.r0.width, 5)
        self.assertEqual(self.r0.height, 12)
        self.assertEqual(self.r0.x, 7)
        self.assertEqual(self.r0.y, 33)
        self.assertEqual(self.r0.id, type(self)._Idcheck)

    def test_InvalidArgs(self):
        with self.assertRaises(TypeError):
            self.r0 = Rectangle()
        with self.assertRaises(TypeError):
            self.r0 = Rectangle(8)


class TestRectangleValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test_InvalidTypes(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle("width", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(5, 2.57)
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(5, 2, "x", 7)
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(9, 1, 12, "2y")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_InvalidDimension(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(-5, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(6, -15)
        self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(6, 15, -61, 2)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(6, 15, 8, -41)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_ZeroDimension(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(15, 0)
        self.assertEqual(str(e.exception), "height must be > 0")


class TestRectangleArea(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testArea(self):
        r1 = Rectangle(5, 3, 4, 5, 11)
        self.assertEqual(r1.area(), 15)

        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)

        r1 = Rectangle(2, 3, 6, 1)
        self.assertEqual(r1.area(), 6)

    def testInvalidArea(self):
        r1 = Rectangle(5, 1)
        with self.assertRaises(TypeError):
            r1.area(5)


class TestDisplayFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testDisplay(self):
        r1 = Rectangle(3, 4)
        with patch("sys.stdout", new=StringIO()) as mock_print:
            r1.display()
            self.assertEqual(mock_print.getvalue(),
                             "###\n###\n###\n###\n")

    def testDisplay2(self):
        r1 = Rectangle(1, 1, y=3)
        with patch("sys.stdout", new=StringIO()) as mock_print:
            r1.display()
            self.assertEqual(mock_print.getvalue(),
                             "\n\n\n#\n")

    def testDisplay3(self):
        r1 = Rectangle(3, 2, 1, 0)
        with patch("sys.stdout", new=StringIO()) as mock_print:
            r1.display()
            self.assertEqual(mock_print.getvalue(),
                             " ###\n ###\n")

    def testDisplay4(self):
        r1 = Rectangle(2, 3, 5, 2)
        with patch("sys.stdout", new=StringIO()) as mock_print:
            r1.display()
            self.assertEqual(mock_print.getvalue(),
                             "\n\n     ##\n     ##\n     ##\n")

    def testInvalidArg(self):
        r1 = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r1.display(4)


class TestStrMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testStr(self):
        r1 = Rectangle(4, 7, 3, 9, 34)
        self.assertEqual(str(r1), "[Rectangle] (34) 3/9 - 4/7")

    def testPrint(self):
        r1 = Rectangle(1, 4, 6, 8, 21)
        with patch("sys.stdout", new=StringIO()) as mock_print:
            print(r1)
            self.assertEqual(mock_print.getvalue(),
                             "[Rectangle] (21) 6/8 - 1/4\n")


class TestUpdateMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testUpdate0Args(self):
        r1 = Rectangle(6, 9, 3, 11, 43)
        r1.update()

    def testUpdate1Arg(self):
        r1 = Rectangle(4, 7, 3, 9, 34)
        self.assertEqual(r1.y, 9)
        r1.update(12)
        self.assertEqual(r1.id, 12)

    def testUpdate2Args(self):
        r1 = Rectangle(4, 7, 3)
        self.assertEqual(r1.id, Base._Base__nb_objects)
        r1.update(2, 5)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 5)

    def testUpdate3Args(self):
        r1 = Rectangle(11, 5)
        r1.update(7, 6, 12)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 12)

    def testUpdate4Args(self):
        r1 = Rectangle(11, 5, 7)
        self.assertEqual(r1.x, 7)
        r1.update(4, 9, 8, 2)
        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 9)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 2)

    def testUpdate5Args(self):
        r1 = Rectangle(11, 5)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 5)

        r1.update(6, 5, 2, 3, 11)
        self.assertEqual(r1.id, 6)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 11)


class TestInvalidUpdate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testInvalidUpdateArg2(self):
        r1 = Rectangle(7, 5, 12)
        with self.assertRaises(TypeError) as e:
            r1.update(12, "width", 5, 11)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            r1.update(32, 0, 5, 11)
        self.assertEqual(str(e.exception), "width must be > 0")

    def testInvalidUpdateArg3(self):
        r1 = Rectangle(2, 6, 11)
        with self.assertRaises(TypeError) as e:
            r1.update(21, 5, "5", 11)
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(ValueError) as e:
            r1.update(27, 12, -5, 11)
        self.assertEqual(str(e.exception), "height must be > 0")

    def testInvalidUpdateArg4(self):
        r1 = Rectangle(11, 14, 3, 5, 16)
        with self.assertRaises(TypeError) as e:
            r1.update(31, 5, 5, None, 6)
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(ValueError) as e:
            r1.update(19, 12, 5, -17, 5)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def testInvalidUpdateArg5(self):
        r1 = Rectangle(7, 4, 1, 8, 2)
        with self.assertRaises(TypeError) as e:
            r1.update(11, 5, 5, 3, 3.56)
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            r1.update(19, 12, 5, 17, -5)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def testInvalidUpdateArg6(self):
        r1 = Rectangle(7, 4, 1, 8, 2)
        r1.update(11, 5, 4, 3, 7, 9)
        self.assertEqual(r1.id, 11)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 7)


class TestAdvancedUpdateMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testUpdate1Kwrg(self):
        r1 = Rectangle(4, 7, 3, 9, 34)
        self.assertEqual(r1.width, 4)
        r1.update(width=12)
        self.assertEqual(r1.width, 12)

    def testUpdate2Kwrgs(self):
        r1 = Rectangle(4, 7, 3)
        self.assertEqual(r1.id, Base._Base__nb_objects)
        r1.update(x=2, id=5)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.x, 2)

    def testUpdate3Kwrgs(self):
        r1 = Rectangle(11, 5)
        r1.update(y=7, id=6, height=12)
        self.assertEqual(r1.id, 6)
        self.assertEqual(r1.y, 7)
        self.assertEqual(r1.height, 12)

    def testUpdate4Kwrgs(self):
        r1 = Rectangle(11, 5, 7)
        self.assertEqual(r1.x, 7)
        r1.update(x=4, y=9, id=8, height=2)
        self.assertEqual(r1.id, 8)
        self.assertEqual(r1.y, 9)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)

    def testUpdate5Kwrgs(self):
        r1 = Rectangle(11, 5)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 5)

        r1.update(width=6, x=5, height=2, id=3, y=11)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.y, 11)


class TestAdvancedUpdateMethod2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test1UpdateKwrgAndArg(self):
        r1 = Rectangle(7, 13)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 13)

        r1.update(12, 34, 33, height=15, id=21)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.height, 33)
        self.assertEqual(r1.y, 0)

    def test2UpdateKwrgAndArg(self):
        r1 = Rectangle(14, 9)
        self.assertEqual(r1.width, 14)
        self.assertEqual(r1.height, 9)

        r1.update(17, 25, 19, 9, x=5, y=11, id=11, height=23)
        self.assertEqual(r1.height, 19)
        self.assertEqual(r1.width, 25)
        self.assertEqual(r1.id, 17)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 0)

    def test3UpdateKwrgAndArg(self):
        r1 = Rectangle(13, 19)
        self.assertEqual(r1.width, 13)
        self.assertEqual(r1.height, 19)

        r1.update(29, x=5, y=11, id=11, height=23)
        self.assertEqual(r1.height, 19)
        self.assertEqual(r1.width, 13)
        self.assertEqual(r1.id, 29)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test4UpdateKwrgAndArg(self):
        r1 = Rectangle(4, 7, 9, 12)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 7)

        r1.update(29, 32, x=5, y=11, id=11, height=23)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.width, 32)
        self.assertEqual(r1.id, 29)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 12)

    def test5UpdateKwrgAndArg(self):
        r1 = Rectangle(4, 7, 9)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 7)

        r1.update(29, 32, x=5, y="11", id=11, height=23)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.width, 32)
        self.assertEqual(r1.id, 29)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 0)


class TestInvalidKwargUpdate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testInvalidUpdateKwrg2(self):
        r1 = Rectangle(7, 5, 12)
        with self.assertRaises(TypeError) as e:
            r1.update(height=12, width="width", y=5, x=11)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            r1.update(x=32, width=-2, y=5, height=11)
        self.assertEqual(str(e.exception), "width must be > 0")

    def testInvalidUpdateKwrg3(self):
        r1 = Rectangle(2, 6, 11)
        with self.assertRaises(TypeError) as e:
            r1.update(id=21, y=5, height="5", x=11)
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(ValueError) as e:
            r1.update(width=27, id=12, height=0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def testInvalidUpdateKwrg4(self):
        r1 = Rectangle(11, 14, 3, 5, 16)
        with self.assertRaises(TypeError) as e:
            r1.update(width=31, height=5, y=6, x=None)
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(ValueError) as e:
            r1.update(width=19, x=-12, id=5, y=17)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def testInvalidUpdateKwrg5(self):
        r1 = Rectangle(7, 4, 1, 8, 2)
        with self.assertRaises(TypeError) as e:
            r1.update(x=11, id=5, y=5.23, width=3, height=3)
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            r1.update(width=19, x=12, y=-5, id=17, height=5)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def testInvalidUpdateKwrg6(self):
        r1 = Rectangle(7, 4, 1, 8, 2)
        r1.update(x=11, id=5, diag=5, width=3, height=3)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.x, 11)
        self.assertEqual(r1.y, 8)


class TestToDictionaryRep(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testToDictionary(self):
        r1 = Rectangle(5, 7, 3, 11, 23)
        self.assertEqual(r1.to_dictionary(),
                         {'width': 5, 'height': 7,
                         'x': 3, 'y': 11, 'id': 23})

    def testToDictionary2(self):
        r1 = Rectangle(4, 3, 9, 13, 27)
        self.assertCountEqual(list(r1.to_dictionary().items()),
                              list({'width': 4, 'height': 3,
                                    'x': 9, 'y': 13, 'id': 27}.items()))

    def testToDictionaryInvalidArg(self):
        r1 = Rectangle(4, 3, 9, 13, 27)
        with self.assertRaises(TypeError):
            r1.to_dictionary(5)
