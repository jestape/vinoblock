from display import Display
from blockchain import Blockchain
from db import DB
import time

lcd = Display(16, 2, 10)
blockchain = Blockchain()
db = DB('system', 'raspberry', 'db')

while True:

    # MOTD
    lcd.displayMOTD("   Welcome to Costaflores")
    print("motd")

    # Blockchain data

    block_num = blockchain.getBlockNumber()
    block_head = blockchain.getBlockHeader()
    block_head = block_head[:16]
    lcd.displayBlockchain(block_num, block_head)
    print("blockchain: " + str(block_num) + " - " + str(block_head))
    
    # Sensor data

    (temp, hum) = db.selectData()
    lcd.displaySensor(temp, hum)
    print("sensor: " + str(temp) + " - " + str(hum))
    db.migrateData()
