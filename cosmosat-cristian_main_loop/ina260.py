from time import time, sleep

from file_logger import log_flight_info, log_downlink_msg

import board
import busio
import adafruit_ina260


## time constants
time_counter_ina = 0
TIME_STEP_INA = 1

## log keys
INA1_LK = 'ina_arriba'
INA2_LK = 'ina_abajo'

## initialize i2c
i2c = busio.I2C(board.SCL, board.SDA)

## ina1 (PAYLOAD) setup
ina1_adress = 0x40
ina1 = adafruit_ina260.INA260(i2c, i2c_address=ina1_adress)

## ina2 (CONDENSADOR) setup
ina2_address = 0x41
ina2 = adafruit_ina260.INA260(i2c, i2c_address=ina2_address)


DOWNLINK_SEPARATING_CHAR = '-'


def get_current_voltage_power_1():

    return ina1.current, ina1.voltage, ina1.power


def get_current_voltage_power_2():

    return ina2.current, ina2.voltage, ina2.power


def log_ina(t0: float):

    global time_counter_ina, TIME_STEP_INA, INA1_LK, INA2_LK, INA3_LK

    t = time() - t0

    ## ina_data
    if t > time_counter_ina:

        t = time() - t0

        ## ina260_1 data
        current, voltage, power = get_current_voltage_power_ina_1()

        info_arr = [INA1_LK, current, voltage, power, t]

        log_flight_info(info_arr)
        log_downlink_msg(info_arr)

        comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
        moteino_write(comando)

        ## ina260_2 data
        current, voltage, power = get_current_voltage_power_ina_2()

        info_arr = [INA2_LK, current, voltage, power, t]

        log_flight_info(info_arr)
        log_downlink_msg(info_arr)

        comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
        moteino_write(comando)

        time_counter_ina += TIME_STEP_INA

