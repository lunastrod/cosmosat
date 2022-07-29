from time import time, sleep

from file_logger import log_flight_info, log_downlink_msg

import board
import busio
import adafruit_ina260


## time constants
time_counter_ina = 0
TIME_STEP_INA = 1

## log keys
INA1_LK = 0
INA2_LK = 1
INA3_LK = 2

## initialize i2c
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


def log_ina(t0: float):

    global time_counter_ina, TIME_STEP_INA, INA1_LK, INA2_LK, INA3_LK

    t = time() - t0

    ## ina_data
    if t > time_counter_ina:

        t = time() - t0

        ## ina260_1 data
        current, voltage, power = get_current_voltage_power_ina_1()

        log_flight_info([INA1_LK, current, voltage, power, t])
        log_downlink_msg([INA1_LK, current, voltage, power, t])

        ## ina260_2 data
        current, voltage, power = get_current_voltage_power_ina_2()

        log_flight_info([INA2_LK, current, voltage, power, t])
        log_downlink_msg([INA2_LK, current, voltage, power, t])

        ## ina260_3 data
        current, voltage, power = get_current_voltage_power_ina_3()

        log_flight_info([INA3_LK, current, voltage, power, t])
        log_downlink_msg([INA3_LK, current, voltage, power, t])

        time_counter_ina += TIME_STEP_INA

