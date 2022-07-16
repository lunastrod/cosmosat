from time import time, sleep

from ina260 import get_current_voltage_power
from file_logger import log_flight_info


while True:

    ## ina260 data
    current, voltage, power = get_current_voltage_power()

    ## laser sensors data

    ## barometer data

    ## execute camera

    ## execute solenoids

    log_flight_info((current, voltage, power))