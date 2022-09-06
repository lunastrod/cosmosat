from time import time, sleep

from file_logger import log_flight_info, log_downlink_msg

import VL53L0X


## time constants
time_counter_laser = 0
TIME_STEP_LASER = 1

## log key
LASER_LK = 3

## other constants
DISTANCE_SEPARATION = 300 # mm

DOWNLINK_SEPARATING_CHAR = '-'

## initialize sensor obj
SENSOR_I2C_ADDRESS = 0x29
sensor1=VL53L0X.VL53L0X(i2c_bus=1, i2c_address=SENSOR_I2C_ADDRESS)


def get_laser_sensor_distance():

    ## obtain distance
    distance = sensor1.get_distance()

    return distance


def is_separated():

    distance = get_laser_sensor_distance()

    if distance >= SEPARATION_DISTANCE:
        return True
    else:
        return False


def log_laser_sensor(t0: float):

    global time_counter_laser, TIME_STEP_LASER, LASER_LK

    t = time() - t0

    ## laser sensors data
    if t > time_counter_laser:

        distance = get_laser_sensor_distance()

        info_arr = [LASER_LK, distance, t]

        log_flight_info(info_arr)
        log_downlink_msg(info_arr)

        comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
        moteino_write(comando)

        time_counter_laser += TIME_STEP_LASER
