from web3 import Web3


def connect(url: str) -> Web3:
    return Web3(Web3.HTTPProvider(url))


RPC_URL = "https://sepolia.infura.io/v3/YOUR_KEY"
