import requests
from decouple import config

def print_transfers(transaction_hash):
    api_url = "https://api.etherscan.io/api"
    params = {
        "module": "proxy",
        "action": "eth_getTransactionReceipt",
        "txhash": transaction_hash,
        "apikey": config("apikey")
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    a = data["result"]
    fromm = a["from"]
    to = a["to"]
    logss = a["logs"]
    dataa = logss[0]["data"]
    dataa = int(dataa, 16)
    
    return [
        {
            "from": fromm,
            "to": to,
            "amount": dataa
        }
    ]

transaction_hash = config("transaction_hash")
print_transfers(transaction_hash)