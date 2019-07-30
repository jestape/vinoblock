import json
import web3
from web3 import Web3, HTTPProvider

class Blockchain:

    def __init__(self):
        self.w3 = Web3(HTTPProvider("http://10.112.48.25:7545"))

    def getBlockNumber(self):
        return self.w3.eth.blockNumber

    def getBlockHeader(self):
        return self.w3.eth.getBlock('latest')['hash'].hex()
