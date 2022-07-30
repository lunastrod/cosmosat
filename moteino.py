import time
import serial

ser = serial.Serial("/dev/tty.usbserial-D307BV4J", baudrate=9600) #Modificar el puerto serie de ser necesario


def moteino_write(comando: str):

    comandoBytes = comando.encode()
    ser.write(comandoBytes)

def moteino_read():

    read = ser.readline()
    return read



'''
try:
    while True:

except KeyboardInterrupt:
    print("\nInterrupcion por teclado")
except ValueError as ve:
    print(ve)
    print("Otra interrupcion")
finally:
    ser.close()
'''