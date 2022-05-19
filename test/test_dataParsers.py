import unittest
from datetime import datetime
from data.dataParsers import DataParsers

Input = DataParsers()
dateList = ["2019-03-04",""]
class TestDataParsers(unittest.TestCase):
    def test_date_format(self):
        self.assertTrue(Input.validateDate("2019-03-04"))
        self.assertTrue(Input.validateDate("2019-12-31"))
        self.assertFalse(Input.validateDate("2019-02-31"))
        self.assertFalse(Input.validateDate("2019-05-32"))
        self.assertFalse(Input.validateDate("20-01-19"))
        self.assertFalse(Input.validateDate("2019/01/31"))
        self.assertFalse(Input.validateDate(""))

    def test_validateFrequency(self):
        self.assertTrue(Input.validateFrequency("q"))
        self.assertTrue(Input.validateFrequency("W"))
        self.assertTrue(Input.validateFrequency("m"))
        self.assertFalse(Input.validateFrequency(""))
        self.assertFalse(Input.validateFrequency("."))

    def test_validatePeriod(self):
        self.assertTrue(Input.validatePeriod(["2022-07-12","2022-07-25"]))
        self.assertFalse(Input.validatePeriod(["2022-02-22","2022-06-25"]))
        self.assertFalse(Input.validatePeriod("asdsad"))

if __name__ == '__main__':
    unittest.main()