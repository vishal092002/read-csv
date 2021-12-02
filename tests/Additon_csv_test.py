import unittest
from csv_read.read_csv import ReadCSV, ClassFactory
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csvRead = ReadCSV('tests/data/add_numbers.csv')

    def test_return_data_as_objects(self):
        people = self.readCSV.return_data_as_class('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])

        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)
            pprint(vars(people))

if __name__ == '__main__':
    unittest.main()