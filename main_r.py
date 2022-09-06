from time import time, sleep
from ina260 import log_ina
from barometer import log_barometer
from laser_sensors import log_laser_sensor
from GPS import log_GPS
from camera import take_caption, take_video
from solenoid import deploy
from moteino import moteino_send

## get initial time
t0 = time()
tstep = 5

while True:

    log_ina(t0)
    

    log_laser_sensor(t0)
    deploy(t0)
    
    #sleep(tstep)
    
    log_barometer(t0)

    #sleep(tstep)
    log_GPS(t0)

    #sleep(tstep)
    take_caption(t0)

    #sleep(tstep)
    take_video(t0)
    
    moteino_send()
    

    sleep(tstep)
    