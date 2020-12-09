from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper


class TestDbHelper(TestCase):
    def setUp(self):
        self.db_help = DbHelper()

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self, MockDbHelper):
        """
        Mock the get_maximum_salary() method of DbHelper class to
        return value '10000'. Mock the get_minimum_salary()
        method to return '5000'. Then check for max_salary greater
        than the min salary using self.assertGreater()
        """
        db_helper = MockDbHelper()  # create a mock object of DbHelper class.
        # This will help to customize output of class methods
        db_helper.get_maximum_salary.return_value = 10000

        actual_1 = db_helper.get_maximum_salary(self, None)
        # calling the get_maximum_salary method
        # but the mocked version will actually get called
        expected_1 = 10000  # expected is 10000 because we are expecting 10000
        self.assertEqual(expected_1, actual_1)

        db_helper.get_minimum_salary.return_value = 5000

        actual_2 = db_helper.get_minimum_salary(
            self, None)  
        # calling the get_minimum_salary method
        # but the mocked version will actually get called
        expected_2 = 5000
        # expected is 5000 because we are expecting 5000
        self.assertEqual(expected_2, actual_2)

        # now obtain the greater value using
        self.assertGreater(expected_1, expected_2)
