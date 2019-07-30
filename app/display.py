import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd


class Display:

    def __init__(self, _lcd_columns, _lcd_rows, _time):

        self.lcd_columns = _lcd_columns
        self.lcd_rows = _lcd_rows

        lcd_rs = digitalio.DigitalInOut(board.D5)
        lcd_en = digitalio.DigitalInOut(board.D6)
        lcd_d4 = digitalio.DigitalInOut(board.D13)
        lcd_d5 = digitalio.DigitalInOut(board.D19)
        lcd_d6 = digitalio.DigitalInOut(board.D26)
        lcd_d7 = digitalio.DigitalInOut(board.D20)
        lcd_backlight = digitalio.DigitalInOut(board.D4)

        self.lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, self.lcd_columns, self.lcd_rows)

        self.duration = _time

    def displayMOTD(self, _scroll_message):

        self.lcd.message = _scroll_message;

        for i in range(len(_scroll_message) + 1):
            time.sleep(self.duration / (len(_scroll_message) + 1))
            self.lcd.move_left()

        self.lcd.clear()

    def displayBlockchain(self, _block_number, _last_transacion):

        self.lcd.message = 'Block: ' + str(_block_number) + '\n' + _last_transacion
        time.sleep(self.duration)
        self.lcd.clear()

    def displaySensor(self, _temperature, _humidity):
        self.lcd.message = 'Temp: ' + str(_temperature) + '\nHumidity: ' + str(_humidity)
        time.sleep(self.duration)
        self.lcd.clear()


