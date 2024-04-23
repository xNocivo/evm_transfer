#need Python >=3.7.2
#first run need to install web3 library using command: pip install web3
from web3 import Web3

rpc = 'https://polygon-rpc.com' #RPC HTTP

receiver = '' #Public Address receiver

arrayAcc = [] #array of privatekeys 


w3 = Web3(Web3.HTTPProvider(rpc))
def pvkey_check_0x(string):
    if not string.startswith("0x"):
        string = "0x" + string
    return string

def rapa_eth(pk):
    pv_key = pvkey_check_0x(pk)
    accounts = w3.eth.account.from_key(pv_key)
    
    gas_price = w3.eth.gas_price
    balance = w3.eth.get_balance(account=accounts.address)
    remain_balance = balance - (gas_price * 21000)
    if(w3.from_wei(balance, "ether") <= 0): 
        print(f"address: {accounts.address} has no balance |")
        print('---------------------------')
        return
    print('sending:', w3.from_wei(remain_balance, "ether"), 'gasprice:', w3.from_wei(gas_price, 'gwei'))

    txObj = {
        "from": w3.to_checksum_address(accounts.address),
        "to": w3.to_checksum_address(receiver),
        "gasPrice": gas_price,
        "gas": 21000,
        "value": remain_balance,
        "nonce": w3.eth.get_transaction_count(account=accounts.address),
        "chainId": w3.eth.chain_id,
        "data": "0x"
    }
    sign = accounts.sign_transaction(txObj)
    tx_hash = w3.eth.send_raw_transaction(sign.rawTransaction)
    print(w3.to_hex(tx_hash))
    print('----------------')


for i in arrayAcc:
    rapa_eth(i)
