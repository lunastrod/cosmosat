import RPi.GPIO as GPIO
from time import time, sleep


# constants
time_to_deploy = 45*60
DEPLOY_PULSE_DURATION = 2
is_solenoid_activated = False
TIME_TO_CHECK_SEPARATION = 30

# log key
MECHANISM_LK = 7

DOWNLINK_SEPARATING_CHAR = '-'

# setup
PIN_SOLENOID = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_SOLENOID, GPIO.OUT)


def activate_solenoid():
    GPIO.output(PIN_SOLENOID, True)


def deactivate_solenoid():
    GPIO.output(PIN_SOLENOID, False)


def deploy(t0: float):

    t = time() - t0

    if ((t > time_to_deploy) and (is_solenoid_activated == False)):

        activate_solenoid()
        is_solenoid_activated = True

    elif ((t > (time_to_deploy + DEPLOY_PULSE_DURATION)) and (is_solenoid_activated == True)):

        deactivate_solenoid()
        is_solenoid_activated = False
        time_to_deploy = t + TIME_TO_CHECK_SEPARATION

    if is_separated():

        info_arr = [MECHANISM_LK, "separated", t]

        log_flight_info(info_arr)
        log_downlink_msg(info_arr)

        comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
        moteino_write(comando)
    else:

        info_arr = [MECHANISM_LK, "not_separated", t]

        log_flight_info(info_arr)
        log_downlink_msg(info_arr)

        comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
        moteino_write(comando)



