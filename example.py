from web3 import Web3
from hexbytes import HexBytes
import json

class HexJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, HexBytes):
            return obj.hex()
        return super().default(obj)

def jsonPrint(printData):
    print(json.dumps(dict(printData), indent=4, sort_keys=True, cls=HexJsonEncoder))

def main():
    w3 = Web3(Web3.IPCProvider('~/geth-ipc'))
    print('Connected to IPC: ', w3.isConnected())

    jsonPrint(w3.eth.get_block(10000000))

if __name__ == "__main__":
    main()
