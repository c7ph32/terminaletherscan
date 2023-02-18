import requests

# Replace with your own Etherscan API key
api_key = "ETHERSCAN_API"

# Replace with the address you want to query
address = "ADDRESS"

balance_endpoint = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
txlist_endpoint = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={api_key}"

balance_response = requests.get(balance_endpoint).json()
account_balance = int(balance_response['result']) / 1000000000000000000

txlist_response = requests.get(txlist_endpoint).json()

print(f"Account: {address}")
print(f"Balance: {account_balance} ETH")
print(f"Transaction Count: {txlist_response['result'].__len__()}")
print("Transaction List:")

for tx in txlist_response['result']:
    print(f"Transaction Hash: {tx['hash']}")
    print(f"From: {tx['from']}")
    print(f"To: {tx['to']}")
    print(f"Value: {int(tx['value']) / 1000000000000000000} ETH")
    print()