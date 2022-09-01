import serial
from time import sleep
import sys


## GPS Setup
ser = serial.Serial ('/dev/ttyS0')
gpgga_info = '$GPGGA,'
GPGGA_buffer = 0
NMEA_buff = 0

## GPS Constants
time_counter_GPS = 0
TIME_STEP_GPS = 1
GPS_LK = 5
DOWNLINK_SEPARATING_CHAR = '-'


def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = '%.4f' %(position)
    return position


def get_GPS_location():
    try:
        received_data = (str)(ser.readline())   ## Read NMEA string received
        GPGGA_data_available = received_data.find(gpgga_info)   ## Check for NMEA GPGGA string

        if (GPGGA_data_available > 0):

            GPGGA_buffer = received_data.split('$GPGGA,',1)[1]
            NMEA_buff = (GPGGA_buffer.split(','))

            latitude = NMEA_buff[1]
            longitude = NMEA_buff[3]
            altitude = NMEA_buff[8]
            alt_ref = NMEA_buff[10]

            latitude = (float)(latitude)
            latitude = convert_to_degrees(latitude)
            longitude = (float)(longitude)
            longi = convert_to_degrees(longitude)

            altitude = (float)(altitude)
            alt_ref = (float)(alt_ref)

            return latitude, longitude, altitude, alt_ref
    
    except:
        return "$", "$", "$", "$"


def log_GPS(t0: float):

    global time_counter_GPS, TIME_STEP_GPS, GPS_LK

    t = time() - t0

    ## GPS data
    if t > time_counter_GPS:
        try:
            latitude, longitude, altitude, ref_alt = get_GPS_location()

        except:
            latitude, longitude, altitude, ref_alt= "$", "$", "$", "$"

        info_arr = [GPS_LK, latitude, longitude, altitude, ref_alt, t]

        log_flight_info(info_arr)
        log_downlink_msg(info_arr)

        comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
        moteino_write(comando)

        time_counter_GPS += TIME_STEP_GPS



