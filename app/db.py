import mysql.connector
from mysql.connector import errorcode
import time

class DB:

    def __init__(self, _user, _passwd, _name):

        try:
            self.cnx = mysql.connector.connect(user=_user,
                                                password=_passwd,
                                                database=_name)
        except mysql.connector.Error as err:

            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")

            else:
                print(err)

            self.cnx = None

    def insertData(self, _timestamp, _sensor, _temperature, _humidity):

        cursor = self.cnx.cursor()
        add_data = ("INSERT INTO sensor_data (_timestamp, _sensor, temperature, humidity) VALUES (%s, %s, %s, %s)")
        data = (time.strftime('%Y-%m-%d %H:%M:%S'), _sensor, _temperature, _humidity)
        cursor.execute(add_data, data)
        self.cnx.commit()

    def selectData(self):
        cursor = self.cnx.cursor()
        select = ("SELECT temperature, humidity FROM sensor_data WHERE _timestamp >= (SELECT MAX(_timestamp) FROM sensor_data)")
        cursor.execute(select)
        return cursor.fetchone()

    def migrateData(self):
        cursor = self.cnx.cursor()
        update = ("")
        cursor.execute(update)
        delete = ("")
        cursor.execute(delete)
        cursor.close()
