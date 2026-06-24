from web3 import Web3

RPC_URL = "https://sepolia.infura.io/v3/YOUR_INFURA_KEY"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
WALLET = "0xYourWalletAddress"
CONTRACT_ADDRESS = "0xContractAddress"

w3 = Web3(Web3.HTTPProvider(RPC_URL))

abi = [
    {
        "inputs": [{"name": "_value", "type": "uint256"}],
        "name": "set",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract = w3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=abi
)

nonce = w3.eth.get_transaction_count(WALLET)

tx = contract.functions.set(123).build_transaction({
    "from": WALLET,
    "nonce": nonce,
    "gas": 100000,
    "gasPrice": w3.eth.gas_price,
    "chainId": 11155111
})

signed_tx = w3.eth.account.sign_transaction(
    tx,
    private_key=PRIVATE_KEY
)

tx_hash = w3.eth.send_raw_transaction(
    signed_tx.raw_transaction
)

print("TX Hash:", tx_hash.hex())
# this is a test comment.
# Please do not use this project for anything illegal.
# Send me pm on X for any questions. @Qoqnush
