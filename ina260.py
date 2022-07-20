import time
import board
import busio
import adafruit_ina260


i2c = busio.I2C(board.SCL, board.SDA)

## ina1 (PAYLOAD) setup
ina1_adress = 0x40
ina1 = adafruit_ina260.INA260(i2c, i2c_address=ina1_adress)

## ina2 (CONDENSADOR) setup
ina2_address = 0x41
ina2 = adafruit_ina260.INA260(i2c, i2c_address=ina2_address)

## ina3 (BATERIA) setup
ina3_address = 0x44
ina3 = adafruit_ina260.INA260(i2c, i2c_address=ina3_address)


def get_current_voltage_power_1():

    return ina1.current, ina1.voltage, ina1.power


def get_current_voltage_power_2():

    return ina2.current, ina2.voltage, ina2.power


def get_current_voltage_power_2():

    return ina3.current, ina3.voltage, ina3.power

