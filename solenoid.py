import RPi.GPIO as GPIO
from time import time, sleep
from moteino import moteino_write
from laser_sensors import is_separated
from file_logger import log_flight_info, log_downlink_msg

# constants
time_to_deploy = 0
DEPLOY_PULSE_DURATION = 2
is_solenoid_activated = False
TIME_TO_CHECK_SEPARATION = 5

# log key
MECHANISM_LK = "solenoid"

DOWNLINK_SEPARATING_CHAR = '-'

# setup
PIN_SOLENOID = 17
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_SOLENOID, GPIO.OUT)


def activate_solenoid():
    GPIO.output(PIN_SOLENOID, True)


def deactivate_solenoid():
    GPIO.output(PIN_SOLENOID, False)


def deploy(t0: float):

    t = time() - t0

    global time_to_deploy, is_solenoid_activated
    if ((t > time_to_deploy) and (is_solenoid_activated == False) and (not is_separated())):

        activate_solenoid()
        is_solenoid_activated = True

    if ((t > (time_to_deploy + DEPLOY_PULSE_DURATION)) and (is_solenoid_activated == True)):

        deactivate_solenoid()
        is_solenoid_activated = False
        time_to_deploy = t + TIME_TO_CHECK_SEPARATION

    if is_separated() and (t > time() - t0):

        info_arr = [MECHANISM_LK, "separated", t]

        log_flight_info(info_arr)
        log_downlink_msg(info_arr)

        comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
        moteino_write(comando)
        print(comando)
    elif (t > time() - t0):

        info_arr = [MECHANISM_LK, "not_separated", t]

        log_flight_info(info_arr)
        log_downlink_msg(info_arr)

        comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
        moteino_write(comando)
        print(comando)
        



