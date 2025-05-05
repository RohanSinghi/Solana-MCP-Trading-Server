from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.publickey import PublicKey

from src.config.config import SOLANA_CLUSTER_URL, EXAMPLE_ACCOUNT_ADDRESS

class SolanaClient:
    def __init__(self):
        self.client = Client(SOLANA_CLUSTER_URL)

    def get_account_info(self, account_address: str):
        try:
            account_info = self.client.get_account_info(PublicKey(account_address))
            return account_info
        except Exception as e:
            print(f"Error fetching account info: {e}")
            return None

    def get_balance(self, account_address: str):
        try:
            balance = self.client.get_balance(PublicKey(account_address))
            return balance
        except Exception as e:
            print(f"Error fetching balance: {e}")
            return None


    def get_recent_blockhash(self):
        try:
            result = self.client.get_latest_blockhash()
            return result
        except Exception as e:
            print(f"Error fetching recent blockhash: {e}")
            return None



if __name__ == '__main__':
    # Example usage
    solana_client = SolanaClient()

    # get account info
    account_info = solana_client.get_account_info(EXAMPLE_ACCOUNT_ADDRESS)
    if account_info:
        print(f"Account Info: {account_info}\n\n")

    # Get account balance
    balance = solana_client.get_balance(EXAMPLE_ACCOUNT_ADDRESS)
    if balance:
        print(f"Account balance: {balance}\n\n")


    # Get recent blockhash
    recent_blockhash = solana_client.get_recent_blockhash()
    if recent_blockhash:
         print(f"Recent Blockhash: {recent_blockhash}\n\n")