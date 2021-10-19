import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin_lab

class TestBitcoinLab(TestCase):

    @patch('bitcoin_lab.request_rate')
    def test_bitcoin_to_dollars(self, mock_rates):
        mock_rate = 12345.67
        example_api_response = {"bpi": {
                                "USD": {
                                "code": "USD",
                                "symbol": "&#36;",
                                "rate": "61,563.2567",
                                "description": "United States Dollar",
                                "rate_float": mock_rate
                                }}}
        mock_rates.side_effect = [ example_api_response ]
        conversion = bitcoin_lab.convert_bitcoin_to_dollars(100, mock_rate)
        self.assertEqual(1234567, conversion)

if __name__ == '__main__':
    unittest.main()