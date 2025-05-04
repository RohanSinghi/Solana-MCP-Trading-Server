class Config:
    def __init__(self):
        self.solana_endpoint = "https://api.devnet.solana.com"
        self.api_port = 8000
        # TODO: Load configuration from file or environment variables

config = Config()