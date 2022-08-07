from time import time

from ina260 import log_ina
from barometer import log_barometer
from laser_sensors import log_laser_sensor
from GPS import log_GPS
from camera import take_caption, take_video
from solenoid import deploy


## get initial time
t0 = time()

while True:

    log_ina(t0)

    log_laser_sensor(t0)

    log_barometer(t0)

    log_GPS(t0)

    take_caption(t0)

    take_video(t0)

    deploy(t0)
