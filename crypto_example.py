from web3 import Web3


def connect(url: str) -> Web3:
    return Web3(Web3.HTTPProvider(url))


RPC_URL = "https://sepolia.infura.io/v3/YOUR_KEY"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
ACCOUNT = "0xYourAddress"
CONTRACT = "0xContractAddress"

client = connect(RPC_URL)

ABI = [{
    "type": "function",
    "name": "set",
    "inputs": [{"name": "_value", "type": "uint256"}],
    "outputs": [],
    "stateMutability": "nonpayable"
}]

contract = client.eth.contract(
    address=client.to_checksum_address(CONTRACT),
    abi=ABI
)
