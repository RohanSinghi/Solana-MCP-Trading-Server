import unittest
from unittest.mock import MagicMock
from src.trading.trading_engine import TradingEngine

class TestTradingEngine(unittest.TestCase):

    def test_execute_trade(self):
        mock_solana_client = MagicMock()
        trading_engine = TradingEngine(mock_solana_client)
        trading_engine.execute_trade("SOL", 1, 100)
        mock_solana_client.get_balance.assert_not_called()

if __name__ == '__main__':
    unittest.main()