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

        


if __name__ == '__main__':
    unittest.main()