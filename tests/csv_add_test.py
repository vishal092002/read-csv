import unittest

from calc.calculations.addition import Addition
from csv_read.read_csv import ReadCSV


#class MyTestCase(unittest.TestCase):
def test_calculation_addition_csv():
    #def setUp(self) -> None:
    #    self.calculator = Calculator()

    #def test_instantiate_calculator(self):
     #   self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = ReadCSV("tests/data/add_numbers.csv").data
        for row in test_data:
            result = float(row['result'])
            val1 = float(row['val1'])
            val2 = float(row['val2'])
            mynumbers = (val1, val2)
            addition = Addition(mynumbers)
            newresult = addition.get_result()
            assert newresult == result
           # self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
           # self.assertEqual(self.calculator.result, result)

   # def test_results_property(self):
    #    self.assertEqual(self.calculator.result, 0)


#if __name__ == '__main__':
 #   unittest.main()