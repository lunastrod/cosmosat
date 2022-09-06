from time import time, sleep

from file_logger import log_flight_info, log_downlink_msg
from moteino import moteino_write
import adafruit_vl53l0x
import busio
import board


## time constants
time_counter_laser = 0
TIME_STEP_LASER = 5

## log key
LASER_LK = "laser_sensors"

## other constants
DISTANCE_SEPARATION = 300 # mm

DOWNLINK_SEPARATING_CHAR = '-'

## initialize sensor obj
SENSOR_I2C_ADDRESS = 0x29
i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = adafruit_vl53l0x.VL53L0X(i2c)


def get_laser_sensor_distance():

    ## obtain distance
    distance = sensor1.range
    return distance


def is_separated():
    distance = get_laser_sensor_distance()
    if distance >= DISTANCE_SEPARATION:
        return True
    else:
        return False


def log_laser_sensor(t0: float):

    global time_counter_laser, TIME_STEP_LASER, LASER_LK

    t = time() - t0

    ## laser sensors data
    if t > time_counter_laser:
        try:
            distance = get_laser_sensor_distance()
        except:
            distance= "$"

        info_arr = [LASER_LK, distance, t]

        log_flight_info(info_arr)
        log_downlink_msg(info_arr)

        comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
        moteino_write(comando)
        print(comando)
        time_counter_laser += TIME_STEP_LASER
