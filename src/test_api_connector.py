import unittest
import src.api_connector as apiconn

class TestApiConnector(unittest.TestCase):

    def setUp(self):
        """Function is setting up variables to use through the test cases."""
        self.connection_instance = apiconn.ApiConnectionTools()
        self.test_categories = {'results': [{'tag': 'accounting-finance-jobs', 'label': 'something'}, {'label': 'something', 'tag': 'it-jobs'}]}
        self.test_salaries = {'__CLASS__': 'something', 'month': {'2021-11': 127694.84, '2021-10': 124508.58}}

    def test_sort_category_results_pass(self):
        """This checks to see the correct values get formatted into a list for categories."""
        self.assertEqual(['accounting-finance-jobs', 'it-jobs'], self.connection_instance._sort_category_results(self.test_categories))

    def test_sort_salary_results_pass(self):
        """This checks to see the correct values get formatted into a list for salaries."""
        self.assertEqual([('2021-10', 124508.58), ('2021-11', 127694.84)], self.connection_instance._sort_salary_results(self.test_salaries))

if __name__ == "__main__":
    unittest.main()
