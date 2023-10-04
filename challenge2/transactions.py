import requests

def print_transfers(transaction_hash):
    # transaction_hash = "0xadb8aec59e80db99811ac4a0235efa3e45da32928bcff557998552250fa672eb"
    api_url = "https://api.etherscan.io/api"
    params = {
        "module": "proxy",
        "action": "eth_getTransactionReceipt",
        "txhash": transaction_hash,
        "apikey": "HQZ6FAVGDFZMYQ7TB6UKEMIKQNG5SKDVHR"
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    a = data["result"]
    fromm = a["from"]
    to = a["to"]
    # print(data["result"])
    # print(data)

transaction_hash = "0xadb8aec59e80db99811ac4a0235efa3e45da32928bcff557998552250fa672eb"
print_transfers(transaction_hash)