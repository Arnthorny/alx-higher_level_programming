#!/usr/bin/python3
"""
Unittest for models.base([..])

This module contains the required tests for the specified module
"""
import unittest
import models.base
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from unittest.mock import patch, mock_open
import json
import csv


class TestAllBaseDocstrings(unittest.TestCase):
    def testModuleDocstring(self):
        self.assertGreater(len(models.base.__doc__), 1)

    def testClassDocstring(self):
        self.assertTrue(hasattr(models.base, "Base"))
        self.assertGreater(len(Base.__doc__), 1)

    def testToJSONStringFnDocstring(self):
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertGreater(len(Base.to_json_string.__doc__), 1)

    def testSaveToFileFnDocstring(self):
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertGreater(len(Base.save_to_file.__doc__), 1)

    def testFromJSONStringFnDocstring(self):
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertGreater(len(Base.from_json_string.__doc__), 1)

    def testCreateFnDocstring(self):
        self.assertTrue(hasattr(Base, "create"))
        self.assertGreater(len(Base.create.__doc__), 1)

    def testLoadFromFileFnDocstring(self):
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertGreater(len(Base.load_from_file.__doc__), 1)

    def testSaveToFileCSVFnDocstring(self):
        self.assertTrue(hasattr(Base, "save_to_file_csv"))
        self.assertGreater(len(Base.save_to_file_csv.__doc__), 1)

    def testLoadFromFileCSVFnDocstring(self):
        self.assertTrue(hasattr(Base, "load_from_file_csv"))
        self.assertGreater(len(Base.load_from_file_csv.__doc__), 1)


class TestBaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls._Idcheck = 0

    def setUp(self):
        self.b0 = Base()
        type(self)._Idcheck += 1

    def test_Docstrings(self):
        self.assertGreater(len(models.base.__doc__), 1)
        self.assertGreater(len(Base.__doc__), 1)

    def test_IdNone(self):
        # Test when no id is given as arg
        self.assertEqual(self.b0.id, type(self)._Idcheck)

    def test_IdInstanceVariable(self):
        with self.assertRaises(AttributeError):
            print(Base.id)

    def test_PrivateAttribute(self):
        with self.assertRaises(AttributeError):
            print(self.b0.__nb_objects)

    def test_ValidId(self):
        self.assertEqual(self.b0.id, type(self)._Idcheck)

    def test_WithArg(self):
        self.b0 = Base(35)
        type(self)._Idcheck -= 1
        self.assertEqual(self.b0.id, 35)


class TestToJsonStringMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test_ListOfDictionaries1(self):
        r1 = Rectangle(11, 6, 2, 5, 8)
        rect_dict = r1.to_dictionary()
        json_str = Base.to_json_string([rect_dict])

        self.assertEqual(json_str, json.dumps([rect_dict]))

    def test_ListOfDictonaries2(self):
        r1 = Rectangle(11, 6, 2)
        s1 = Square(6)
        dict_list = [r1.to_dictionary(), s1.to_dictionary()]
        json_str = Base.to_json_string(dict_list)

        self.assertEqual(json_str, json.dumps(dict_list))

    def test_ListOfDictionaryNone(self):
        json_str = Base.to_json_string()
        self.assertEqual(json_str, "[]")
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_ListOfDictionaryEmpty(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_ListInvalid1(self):
        with self.assertRaises(TypeError) as e:
            json_str = Base.to_json_string([{'x': 5},
                                            {'y': 8}, "4", 5.35])
        self.assertEqual(str(e.exception), "list_dictionaries must be "
                         "a list of dictionaries")

    def test_ListInvalid2(self):
        with self.assertRaises(TypeError) as e:
            json_str = Base.to_json_string(2.54)
        self.assertEqual(str(e.exception), "list_dictionaries must be "
                         "a list of dictionaries")

    def test_ListInvalid3(self):
        with self.assertRaises(TypeError) as e:
            json_str = Base.to_json_string({'x': 12, 'y': 5, 'id': 4})
        self.assertEqual(str(e.exception), "list_dictionaries must be "
                         "a list of dictionaries")


class TestSaveToJSONFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        # Create temporary JSON File for use in testing
        # permission errors
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def testListOfRectangleObjects(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(7, 8, 9, 8)

        filename = "Rectangle.json"
        filecontent = json.dumps([r1.to_dictionary(),
                                  r2.to_dictionary(),
                                  r3.to_dictionary()])

        with patch('models.base.open', mock_open()) as mocked_file:
            Rectangle.save_to_file([r1, r2, r3])

            # assert if file was opened with write mode 'w'
            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8")

            # assert if write(content) was called from the file opend
            mocked_file().write.assert_called_once_with(filecontent)

    def testListOfSquareObjects(self):
        s1 = Square(9, 13, 6, 11)
        s2 = Square(3, 9, 7)
        s3 = Square(11, 15)

        filename = "Square.json"
        filecontent = json.dumps([s1.to_dictionary(),
                                  s2.to_dictionary(),
                                  s3.to_dictionary()])

        with patch('models.base.open', mock_open()) as mocked_file:
            Square.save_to_file([s1, s2, s3])

            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8")
            mocked_file().write.assert_called_once_with(filecontent)

    def testListOfSquareAndRectangleObjects(self):
        s1 = Square(9, 13, 6, 11)
        r2 = Rectangle(5, 2, 8)
        s3 = Square(2, 13)

        filename = "Square.json"
        filecontent = json.dumps([])

        with patch('models.base.open', mock_open()) as mocked_file:
            with self.assertRaises(TypeError) as e:
                Square.save_to_file([s1, r2, s3])
            self.assertEqual(str(e.exception), "list_objs objects "
                             "must be homogeneous")

            mocked_file.assert_not_called()
            mocked_file().write.assert_not_called()

    def testEmptyListOfRectObjects(self):
        filename = "Rectangle.json"
        filecontent = json.dumps([])

        with patch('models.base.open', mock_open()) as mocked_file:
            Rectangle.save_to_file([])

            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8")
            mocked_file().write.assert_called_once_with(filecontent)

    def testEmptyListOfSquareObjects(self):
        filename = "Square.json"
        filecontent = json.dumps([])

        with patch('models.base.open', mock_open()) as mocked_file:
            Square.save_to_file([])

            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8")
            mocked_file().write.assert_called_once_with(filecontent)

    def testNoneListOfObjects(self):
        filename = "Square.json"
        filecontent = json.dumps([])

        with patch('models.base.open', mock_open()) as mocked_file:
            Square.save_to_file(None)

            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8")
            mocked_file().write.assert_called_once_with(filecontent)

    def testInvalidListOfObjects(self):
        s1 = Square(9, 13, 6, 11)
        filename = "Square.json"
        filecontent = json.dumps([])

        with patch('models.base.open', mock_open()) as mocked_file:
            with self.assertRaises(TypeError) as e:
                Square.save_to_file([s1.to_dictionary, 4, 5, 6])
            self.assertEqual(str(e.exception), "list_objs objects "
                             "must be homogeneous")

            mocked_file.assert_not_called()
            mocked_file().write.assert_not_called()

    @staticmethod
    def fake_path_exists(path):
        return (True)

    @staticmethod
    def fake_path_isfile(path):
        return (False)

    def testInvalidFileType(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        filecontent = json.dumps([r1.to_dictionary(),
                                  r2.to_dictionary()])

        with patch("os.path.exists", self.fake_path_exists):
            with patch("os.path.isfile", self.fake_path_isfile):
                with self.assertRaises(TypeError) as e:
                    Rectangle.save_to_file([r1, r2])
                self.assertEqual(str(e.exception), "Rectangle.json must "
                                 "be a regular file")


class TestFromJsonStringMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test_JSONString(self):
        r1 = Rectangle(11, 6, 2, 5, 8)
        json_str = Square.to_json_string([r1.to_dictionary()])
        list_from_json = Rectangle.from_json_string(json_str)

        self.assertEqual(json.loads(json_str), list_from_json)

    def test_JSONString2(self):
        r1 = Rectangle(11, 6, 2)
        s1 = Square(6, 8)
        json_str = Rectangle.to_json_string([r1.to_dictionary(),
                                            s1.to_dictionary()])

        list_from_json = Square.from_json_string(json_str)
        self.assertEqual(json.loads(json_str), list_from_json)

    def test_JSONEmptyString(self):
        json_str = ""
        list_from_json = Square.from_json_string(json_str)
        self.assertEqual([], list_from_json)

    def test_JSONNoneString(self):
        json_str = None
        list_from_json = Square.from_json_string(json_str)
        self.assertEqual([], list_from_json)

    def test_JSONInvalidString1(self):
        json_str = 2.45

        with self.assertRaises(TypeError):
            list_from_json = Rectangle.from_json_string(json_str)

    def test_JSONInvalidString2(self):
        json_str = Square(5)
        with self.assertRaises(TypeError):
            list_from_json = Square.from_json_string(json_str)

    def test_JSONInvalidString(self):
        json_str = "\n\b Invalid Square.json file content"
        with self.assertRaises(json.decoder.JSONDecodeError):
            list_from_json = Rectangle.from_json_string(json_str)

    def test_InvalidListFromString(self):
        json_str = "[2, 4, 5, 7, 9]"
        with self.assertRaises(TypeError) as e:
            list_from_json = Square.from_json_string(json_str)
        self.assertEqual(str(e.exception), "Deserialized object "
                         "not list of dictionaries")


class TestCreateMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def testCreateRectFromInstance(self):
        r1 = Rectangle(2, 4, 5)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)

        self.assertEqual(r2.to_dictionary(), r1.to_dictionary())

    def testCreateRectFromDict(self):
        dict_base = {'x': 5, 'y': 11, 'width': 4, 'height': 5, 'id': 9}
        r1 = Rectangle.create(**dict_base)

        self.assertEqual(r1.to_dictionary(), dict_base)
        self.assertEqual(type(r1).__name__, "Rectangle")

    def testCreateSquareFromInstance(self):
        s1 = Square(5, 7, 9)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)

        self.assertEqual(s1_dict, s2.to_dictionary())
        self.assertEqual(type(s2).__name__, "Square")

    def testCreateSquareFromDict(self):
        dict_square = {'size': 5, 'x': 4, 'y': 3, 'id': 11}
        s1 = Square.create(**dict_square)

        self.assertEqual(dict_square, s1.to_dictionary())

    def testCreateRectWithInvalidKey(self):
        r1 = Rectangle(3, 4, 5, 11)
        r1_dict = r1.to_dictionary()
        r1_dict['z'] = 9
        r1_dict['area'] = 12
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def testCreateSquareWithInvalidKey(self):
        s1 = Square(3, 4, 5, 11)
        s1_dict = s1.to_dictionary()
        s1_dict['diagonal'] = 18
        s1_dict['angle'] = 90
        s2 = Square.create(**s1_dict)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())

    def testCreateWithEmptyDict(self):
        r1_dict = {}
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual({'width': 1, 'height': 1,
                          'x': 0, 'y': 0,
                          'id': Base._Base__nb_objects},
                         r2.to_dictionary())

        s1_dict = {}
        s2 = Square.create(**r1_dict)
        self.assertEqual({'size': 1, 'x': 0,
                          'y': 0,
                          'id': Base._Base__nb_objects},
                         s2.to_dictionary())

    def testCreateWithInvalidDict(self):
        r1_dict = {'i': 1, 'z': 2, 'diag': 3}
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual({'width': 1, 'height': 1,
                          'x': 0, 'y': 0,
                          'id': Base._Base__nb_objects},
                         r2.to_dictionary())

        s1_dict = {'i': 1, 'z': 2, 'diag': 3}
        s2 = Square.create(**s1_dict)
        self.assertEqual({'size': 1,
                          'x': 0, 'y': 0,
                          'id': Base._Base__nb_objects},
                         s2.to_dictionary())


class TestLoadFromJSONFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        # Create temporary JSON File for use in testing
        # permission errors
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

    @staticmethod
    def fake_path_exists_false(path):
        return (False)

    @staticmethod
    def fake_path_exists_true(path):
        return (True)

    def testAbsentRectangleFile(self):
        with patch('os.path.exists', self.fake_path_exists_false):
            rect_list = Rectangle.load_from_file()
            self.assertEqual([], rect_list)

    def testAbsentSquareFile(self):
        with patch('os.path.exists', self.fake_path_exists_false):
            square_list = Square.load_from_file()
            self.assertEqual([], square_list)

    def testEmptyListOfRectFile(self):
        filecontent = json.dumps([])
        filename = "Rectangle.json"
        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:
            rect_list = Rectangle.load_from_file()

            # assert if file was opened with read mode 'r'
            mocked_file.assert_called_once_with(filename, 'r',
                                                encoding="utf-8")

            self.assertEqual(rect_list, [])

    def testEmptyListOfSquareFile(self):
        filecontent = json.dumps([])
        filename = "Square.json"
        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:
            square_list = Square.load_from_file()

            # assert if file was opened with read mode 'r'
            mocked_file.assert_called_once_with(filename, 'r',
                                                encoding="utf-8")

            self.assertEqual(square_list, [])

    def testListOfRectangleInstancesFile(self):
        r1 = Rectangle(10, 4, 8)
        r2 = Rectangle(2, 4, 9)
        rect_list_ip = [r.to_dictionary() for r in (r1, r2)]
        filecontent = json.dumps(rect_list_ip)
        filename = "Rectangle.json"

        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:
            rect_list_op = Rectangle.load_from_file()

            # assert if file was opened with read mode 'r'
            mocked_file.assert_called_once_with(filename, 'r',
                                                encoding="utf-8")

            self.assertEqual(list(map(lambda x: x.to_dictionary(),
                                      rect_list_op)),
                             rect_list_ip)

    def testListOfSquareInstancesFile(self):
        s1 = Square(10, 5, 7)
        s2 = Square(2, 9)
        s3 = Square(11, 25)
        sqr_list_ip = [s.to_dictionary() for s in (s1, s2, s3)]
        filecontent = json.dumps(sqr_list_ip)
        filename = "Square.json"

        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:
            sqr_list_op = Square.load_from_file()

            # assert if file was opened with read mode 'r'
            mocked_file.assert_called_once_with(filename, 'r',
                                                encoding="utf-8")

            self.assertEqual(list(map(lambda x: x.to_dictionary(),
                                      sqr_list_op)),
                             sqr_list_ip)

    def testCorruptSquareJSONFile(self):
        filecontent = "\n\b Invalid Square.json file content"
        filename = "Square.json"

        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:
            with self.assertRaises(json.decoder.JSONDecodeError):
                sqr_list_op = Square.load_from_file()

            # assert if file was opened with read mode 'r'
            mocked_file.assert_called_once_with(filename, 'r',
                                                encoding="utf-8")

    def testCorruptRectangleJSONFile(self):
        filecontent = "\t\t Invalid JSON file content"
        filename = "Rectangle.json"

        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:
            with self.assertRaises(json.decoder.JSONDecodeError):
                rect_list_op = Rectangle.load_from_file()

            # assert if file was opened with read mode 'r'
            mocked_file.assert_called_once_with(filename, 'r',
                                                encoding="utf-8")

    @staticmethod
    def fake_path_exists_true(path):
        return (True)

    @staticmethod
    def fake_path_isfile(path):
        return (False)

    def testInvalidRectangleJSONFileType(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        filecontent = json.dumps([r1.to_dictionary(),
                                  r2.to_dictionary()])

        with patch("os.path.exists", self.fake_path_exists_true):
            with patch("os.path.isfile", self.fake_path_isfile):
                with self.assertRaises(TypeError) as e:
                    Rectangle.load_from_file()
                self.assertEqual(str(e.exception), "Rectangle.json must "
                                 "be a regular file")

    def testInvalidSquareJSONFileType(self):

        with patch("os.path.exists", self.fake_path_exists_true):
            with patch("os.path.isfile", self.fake_path_isfile):
                with self.assertRaises(TypeError) as e:
                    Square.load_from_file()
                self.assertEqual(str(e.exception), "Square.json must "
                                 "be a regular file")


class TestSaveToCSVFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        # Create temporary JSON File for use in testing
        # permission errors
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def testListOfRectangleObjects(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(7, 8, 9, 8)

        filename = "Rectangle.csv"
        calls = ['3,10,7,2,8\r\n',
                 '4,2,4,0,0\r\n',
                 '5,7,8,9,8\r\n']

        with patch('models.base.open', mock_open()) as mocked_file:
            Rectangle.save_to_file_csv([r1, r2, r3])

            # assert if file was opened with write mode 'w'
            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8", newline='')

            # assert if write(content) was called from the file opend
            mocked_file().write.has_calls(calls)

    def testListOfSquareObjects(self):
        s1 = Square(9, 13, 6, 11)
        s2 = Square(3, 9, 7)
        s3 = Square(11, 15)

        filename = "Square.csv"
        calls = ['11,9,13,6\r\n',
                 '8,3,9,7\r\n',
                 '9,11,15,0\r\n']

        with patch('models.base.open', mock_open()) as mocked_file:
            Square.save_to_file_csv([s1, s2, s3])

            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8", newline='')
            mocked_file().write.has_calls(calls)

    def testListOfSquareAndRectangleObjects(self):
        s1 = Square(9, 13, 6, 11)
        r2 = Rectangle(5, 2, 8)
        s3 = Square(2, 13)

        filename = "Square.csv"

        with patch('models.base.open', mock_open()) as mocked_file:
            with self.assertRaises(TypeError) as e:
                Square.save_to_file_csv([s1, r2, s3])
            self.assertEqual(str(e.exception), "list_objs must be homogeneous "
                             "list of `Base` objects")

            mocked_file.assert_not_called()
            mocked_file().write.assert_not_called()

    def testEmptyListOfObjects(self):
        filename = "Rectangle.csv"
        filecontent = ""

        with patch('models.base.open', mock_open()) as mocked_file:
            Rectangle.save_to_file_csv([])

            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8", newline='')
            mocked_file().write.assert_not_called()

    def testNoneListOfObjects(self):
        filename = "Square.csv"
        filecontent = ""

        with patch('models.base.open', mock_open()) as mocked_file:
            Square.save_to_file_csv(None)

            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8", newline='')
            mocked_file().write.assert_not_called()

    def testInvalidListOfObjects(self):
        s1 = Square(9, 13, 6, 11)

        with patch('models.base.open', mock_open()) as mocked_file:
            with self.assertRaises(TypeError) as e:
                Square.save_to_file_csv([s1, 4, 5, 6])
            self.assertEqual(str(e.exception), "list_objs must be homogeneous "
                             "list of `Base` objects")

            mocked_file.assert_not_called()
            mocked_file().write.assert_not_called()

    @staticmethod
    def fake_path_exists(path):
        return (True)

    @staticmethod
    def fake_path_isfile(path):
        return (False)

    def testInvalidFileType(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        filecontent = f"{Base._Base__nb_objects},10,7,2,8\n\
                        {Base._Base__nb_objects},2,4,0,0\n"

        with patch("os.path.exists", self.fake_path_exists):
            with patch("os.path.isfile", self.fake_path_isfile):
                with self.assertRaises(TypeError) as e:
                    Rectangle.save_to_file_csv([r1, r2])
                self.assertEqual(str(e.exception), "Rectangle.csv must "
                                 "be a regular file")

    def test_ListOfDictionaryNone(self):
        filename = "Rectangle.csv"
        filecontent = ""

        with patch('models.base.open', mock_open()) as mocked_file:
            Rectangle.save_to_file_csv(None)

            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8", newline='')
            mocked_file().write.assert_not_called()

    def test_ListOfDictionaryEmpty(self):
        filename = "Square.csv"
        filecontent = ""

        with patch('models.base.open', mock_open()) as mocked_file:
            Square.save_to_file_csv()

            mocked_file.assert_called_once_with(filename, 'w',
                                                encoding="utf-8", newline='')
            mocked_file().write.assert_not_called()

    def test_ListInvalid1(self):
        obj_list = [{'x': 5}, {'y': 8}, "4", 5.35]

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file_csv(obj_list)

        self.assertEqual(str(e.exception), "list_objs must be homogeneous "
                         "list of `Base` objects")

    def test_ListInvalid2(self):
        obj_list = 3.87

        with self.assertRaises(TypeError) as e:
            Square.save_to_file_csv(obj_list)

        self.assertEqual(str(e.exception), "list_objs must be homogeneous "
                         "list of `Base` objects")

    def test_ListInvalid3(self):
        obj_list = {'x': 12, 'y': 5, 'id': 4}

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file_csv(obj_list)

        self.assertEqual(str(e.exception), "list_objs must be homogeneous "
                         "list of `Base` objects")


class TestLoadFromCSVFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        # Create temporary JSON File for use in testing
        # permission errors
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")


    @staticmethod
    def fake_path_exists_false(path):
        return (False)

    def testAbsentRectangleFile(self):
        with patch('os.path.exists', self.fake_path_exists_false):
            rect_list = Rectangle.load_from_file_csv()
            self.assertEqual([], rect_list)

    def testAbsentSquareFile(self):
        with patch('os.path.exists', self.fake_path_exists_false):
            square_list = Square.load_from_file_csv()
            self.assertEqual([], square_list)

    def testEmptyRectangleListFile(self):
        filecontent = ""
        filename = "Rectangle.csv"
        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:
            rect_list = Rectangle.load_from_file_csv()

            # assert if file was opened with read mode 'r'
            mocked_file.assert_called_once_with(filename, 'r',
                                                encoding="utf-8", newline='')

            self.assertEqual(rect_list, [])

    def testEmptySquareListFile(self):
        filecontent = "\n"
        filename = "Square.csv"
        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:

            with self.assertRaises(TypeError) as e:
                square_list = Square.load_from_file_csv()
            self.assertEqual(str(e.exception), "Invalid CSV file")

        # assert if file was opened with read mode 'r'
        mocked_file.assert_called_once_with(filename, 'r',
                                            encoding="utf-8", newline='')

    def testListOfRectangleInstancesFile(self):
        r1 = Rectangle(10, 4, 8)
        id1 = Base._Base__nb_objects
        r2 = Rectangle(2, 4, 9)
        id2 = Base._Base__nb_objects
        rect_list_ip = [r.to_dictionary() for r in (r1, r2)]
        filecontent = f"{id1},10,4,8,0\n\
                        {id2},2,4,9,0\n"
        filename = "Rectangle.csv"

        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:
            rect_list_op = Rectangle.load_from_file_csv()

            # assert if file was opened with read mode 'r'
            mocked_file.assert_called_once_with(filename, 'r',
                                                encoding="utf-8", newline='')

            self.assertEqual(list(map(lambda x: x.to_dictionary(),
                                      rect_list_op)),
                             rect_list_ip)

    def testListOfSquareInstancesFile(self):
        s1 = Square(10, 5, 7)
        id1 = Base._Base__nb_objects
        s2 = Square(2, 9)
        id2 = Base._Base__nb_objects
        s3 = Square(11, 25)
        id3 = Base._Base__nb_objects
        sqr_list_ip = [s.to_dictionary() for s in (s1, s2, s3)]
        filecontent = f"{id1},10,5,7\n\
                        {id2},2,9,0\n\
                        {id3},11,25,0\n"

        filename = "Square.csv"

        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:
            sqr_list_op = Square.load_from_file_csv()

            # assert if file was opened with read mode 'r'
            mocked_file.assert_called_once_with(filename, 'r',
                                                encoding="utf-8", newline='')

            self.assertEqual(list(map(lambda x: x.to_dictionary(),
                                      sqr_list_op)),
                             sqr_list_ip)

    def testCorruptSquareCSVFile(self):
        filecontent = "\n\b Invalid Square.csv file content"
        filename = "Square.csv"

        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:

            with self.assertRaises(TypeError) as e:
                sqr_list_op = Square.load_from_file_csv()
            self.assertEqual(str(e.exception), "Invalid CSV file")

        # assert if file was opened with read mode 'r'
        mocked_file.assert_called_once_with(filename, 'r',
                                            encoding="utf-8", newline='')

    def testCorruptRectangleCSVFile(self):
        filecontent = "\t\t Invalid CSV file content\n"
        filename = "Rectangle.csv"

        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:

            with self.assertRaises(TypeError) as e:
                rect_list_op = Rectangle.load_from_file_csv()
            self.assertEqual(str(e.exception), "Invalid CSV file")
        # assert if file was opened with read mode 'r'
        mocked_file.assert_called_once_with(filename, 'r',
                                            encoding="utf-8", newline='')

    def testCorruptRectangleCSVFile2(self):
        filecontent = "1,2,4,5,6,7\n"
        filename = "Rectangle.csv"

        with patch("models.base.open",
                   mock_open(read_data=filecontent)) as mocked_file:
            with self.assertRaises(TypeError) as e:
                rect_list_op = Rectangle.load_from_file_csv()
            self.assertEqual(str(e.exception), "Invalid CSV file")

        # assert if file was opened with read mode 'r'
        mocked_file.assert_called_once_with(filename, 'r',
                                            encoding="utf-8", newline='')

    @staticmethod
    def fake_path_exists_true(path):
        return (True)

    @staticmethod
    def fake_path_isfile(path):
        return (False)

    def testInvalidRectangleCSVFileType(self):
        r1 = Rectangle(10, 4, 8)
        r2 = Rectangle(2, 4, 9)
        filecontent = f"{Base._Base__nb_objects},10,4,8,0\n\
                        {Base._Base__nb_objects},2,4,9\n"

        with patch("os.path.exists", self.fake_path_exists_true):
            with patch("os.path.isfile", self.fake_path_isfile):
                with self.assertRaises(TypeError) as e:
                    Rectangle.save_to_file_csv(filecontent)
                self.assertEqual(str(e.exception), "Rectangle.csv must "
                                 "be a regular file")

    def testInvalidSquareCSVFileType(self):
        s1 = Square(10, 5, 7)
        s3 = Square(11, 25)
        filecontent = f"{Base._Base__nb_objects},10,5,7\n\
                        {Base._Base__nb_objects},11,25,0\n"

        with patch("os.path.exists", self.fake_path_exists_true):
            with patch("os.path.isfile", self.fake_path_isfile):
                with self.assertRaises(TypeError) as e:
                    Rectangle.save_to_file_csv(filecontent)
                self.assertEqual(str(e.exception), "Rectangle.csv must "
                                 "be a regular file")
