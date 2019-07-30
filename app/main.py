from display import Display
from sensors import Sensors
from blockchain import Blockchain
from db import DB
import time

lcd = Display(16, 2, 10)
sensors = Sensors()
blockchain = Blockchain()
db = DB('system', 'raspberry', 'db')

while True:

    # MOTD
    lcd.displayMOTD("   Welcome to Costaflores")

    # Blockchain data

    block_num = blockchain.getBlockNumber()
    block_head = blockchain.getBlockHeader()
    block_head = block_head[:16]
    lcd.displayBlockchain(block_num, block_head)

    # Sensor data

    (temp, hum) = sensors.getData()
    while (temp, hum) == (None, None):
        (temp, hum) = sensors.getData()

    db.insertData(time.time(), 'DHT22', temp, hum)
    lcd.displaySensor(temp, hum)


