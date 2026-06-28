from web3 import Web3


def connect(url: str) -> Web3:
    return Web3(Web3.HTTPProvider(url))

