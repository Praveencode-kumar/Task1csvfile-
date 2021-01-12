import unittest
from  unittest.mock import patch
import    tasktestcase

import json

class TestDataExtraction(unittest.TestCase):

    def test_data(self):
        fake_json = [{'login':"Praveen Kumar"}]

        with patch('tasktestcase.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

            obj1 = tasktestcase. Data_Extraction()
            response = obj1.get

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_json)


if __name__ == "__main__":
    unittest.main()

