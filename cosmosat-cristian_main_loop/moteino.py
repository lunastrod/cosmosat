import time
import serial
from file_logger import log_error_msg

try:
    ser = serial.Serial("/dev/tty.usbserial-D307BV4J", baudrate=9600) #Modificar el puerto serie de ser necesario
except Exception:
    log_error_msg('serial_error_moteino')


def moteino_write(comando: str):

    comandoBytes = comando.encode()
    try:
        ser.write(comandoBytes)
    except:
        log_error_msg('telemetry_error')

def moteino_read():

    read = ser.readline()
    return read
