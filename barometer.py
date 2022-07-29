from time import time, sleep
import numpy as np

from file_logger import log_flight_info, log_downlink_msg


## time constants for each element
time_counter_barometer = 0
TIME_STEP_BAROMETER = 1

## log key
BAROMETER_LK = 4

## function to get the data from the barometer
def get_pressure():

    return 0

PRESSURE_11 = 22.65
PRESSURE_25 = 2.488


def get_altitude_from_pressure():

    pressure = get_pressure()

    #dividimos entre 10 para pasar de milibar a kilopascal
    pressure /= 10

    if (pressure > PRESSURE_11):
        T = (pressure/101.29)**(0.19026)*288.08 - 273.1
        h = (T - 15.04)/-6.49E-3

    elif ((pressure < PRESSURE_11) and (pressure > PRESSURE_25)):
        T = -56.46
        h = (np.log(pressure/22.65) - 1.73)/-1.57E-4

    else:
        T = (pressure/2.488)**(-0.087812)*216.6 - 273.1
        h = (T + 131.21)/2.99E-3

    #obtenemos la altura en metros
    return h

def log_barometer(t0: float):

    global time_counter_barometer, TIME_STEP_BAROMETER, BAROMETER_LK

    t = time() - t0

    ## barometer data
    if t > time_counter_barometer:

        altitude = get_altitude_from_pressure()
        pressure = get_pressure()

        log_flight_info([BAROMETER_LK, altitude, pressure, t])
        log_downlink_msg([BAROMETER_LK, altitude, pressure, t])

        time_counter_barometer += TIME_STEP_BAROMETER
