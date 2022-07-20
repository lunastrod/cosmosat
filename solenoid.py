import RPi.GPIO as GPIO


pin_solenoid = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_solenoid, GPIO.OUT)


def activate_solenoid():
    GPIO.output(pin_solenoid, True)

def deactivate_solenoid():
    GPIO.output(pin_solenoid, False)

