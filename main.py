from time import time, sleep

from ina260 import get_current_voltage_power
from barometer import get_altitude_from_pressure, get_pressure
from file_logger import log_flight_info, log_downlink_msg
from laser_sensors import get_laser_sensor_distance
from camera import take_caption, take_video


## get initial time
t0 = time()

## time constants for each element
time_counter_ina = 0
time_step_ina = 1

time_counter_barometer = 0
time_step_barometer = 1

time_counter_laser = 0
time_step_laser = 1

time_counter_camera = 0
time_step_camera = 1*60

time_counter_video = 0
time_step_video = 10*60
video_duration = 10

time_to_deploy = 45*60
deploy_pulse_duration = 2
is_solenoid_activated = False
time_to_check_separation = 5

## log keys
ina1_lk = 0
ina2_lk = 1
ina3_lk = 2
laser_lk = 3
barometer_lk = 4
image_lk = 5
video_lk = 6
mechanism_lk = 7


while True:

    ## current time relative to initial time (t0)
    t = time() - t0

    ## ina_data
    if t > time_counter_ina:

        ## ina260_1 data
        current, voltage, power = get_current_voltage_power_ina_1()

        log_flight_info([ina1_lk, current, voltage, power, t])
        log_downlink_msg([ina1_lk, current, voltage, power, t])

        ## ina260_2 data
        current, voltage, power = get_current_voltage_power_ina_2()

        log_flight_info([ina2_lk, current, voltage, power, t])
        log_downlink_msg([ina2_lk, current, voltage, power, t])

        ## ina260_3 data
        current, voltage, power = get_current_voltage_power_ina_3()

        log_flight_info([ina3_lk, current, voltage, power, t])
        log_downlink_msg([ina3_lk, current, voltage, power, t])

        time_counter_ina += time_step_ina

    ## laser sensors data
    if t > time_counter_laser:

        distance = get_laser_sensor_distance()

        log_flight_info([laser_lk, distance, t])
        log_downlink_msg([laser_lk, distance, t])

        time_counter_laser += time_step_laser

    ## barometer data
    if t > time_counter_barometer:

        altitude = get_altitude_from_pressure()
        pressure = get_pressure()

        log_flight_info([barometer_lk, altitude, pressure, t])
        log_downlink_msg([barometer_lk, altitude, pressure, t])

        time_counter_barometer += time_step_barometer

    ## take image
    if t > time_counter_image:

        take_caption()

        log_flight_info([image_lk, "caption", t])

        time_counter_image += time_step_image

    ## take video
    if t > time_counter_video:

        take_video(video_duration)

        log_flight_info([video_lk, "video", t])

        time_counter_video += time_step_video

    ## execute solenoids
    if ((t > time_to_deploy) and (is_solenoid_activated == False)):

        activate_solenoid()
        is_solenoid_activated = True

    elif ((t > (time_to_deploy + deploy_pulse_duration)) and (is_solenoid_activated == True)):

        deactivate_solenoid()
        is_solenoid_activated = False
        time_to_deploy = t + time_to_check_separation

    if is_separated():

        log_flight_info([mechanism_lk, "separated", t])
        log_downlink_msg([mechanism_lk, "separated", t])

        time_to_deploy = 1e10
