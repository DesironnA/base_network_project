from web3 import Web3
RPC = "https://sepolia.infura.io/v3/YOUR_KEY"
ACCOUNT = "0xYourAddress"
KEY = "YOUR_PRIVATE_KEY"
TARGET = "0xContractAddress"

web3 = Web3(Web3.HTTPProvider(RPC))
contract_abi = [
    {
        "name": "set",
        "type": "function",
        "inputs": [{"name": "_value", "type": "uint256"}],
        "outputs": [],
        "stateMutability": "nonpayable"
    }

]

instance = web3.eth.contract(
    address=web3.to_checksum_address(TARGET),
    abi=contract_abi
)
transaction = instance.functions.set(999).build_transaction({
    "chainId": 11155111,
    "from": ACCOUNT,
    "nonce": web3.eth.get_transaction_count(ACCOUNT),
    "gas": 120000,
    "gasPrice": web3.eth.gas_price

})


# this is a test comment.
# Please do not use this project for anything illegal.
# Send me pm on X for any questions. @Qoqnush
# this is a test comment.
