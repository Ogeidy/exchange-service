import unittest
from unittest.mock import patch, Mock

from exchange_service import config
from exchange_service.exchange import exchange


class TestExchange(unittest.TestCase):

    @patch('exchange_service.exchange.get_rate')
    def test_normal_exchange(self, mock_get_rate):
        mock_get_rate.return_value = {'USD': 30}
        result = exchange(100, conf=config.TestingConfig)
        self.assertEqual(result, 3000)

    @patch(target='exchange_service.exchange.get_rate', new=Mock(return_value=None))
    def test_bad_rate(self):
        result = exchange(100, conf=config.TestingConfig)
        self.assertEqual(result, None)

    def test_bad_amount(self):
        result = exchange('abc', conf=config.TestingConfig)
        self.assertEqual(result, None)

    def test_bad_url(self):

        class BadUrlConfig(config.TestingConfig):
            RATE_API_URL = 'https://example.com'

        result = exchange(100, conf=BadUrlConfig)
        self.assertEqual(result, None)
