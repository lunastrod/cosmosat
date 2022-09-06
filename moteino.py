import time
import serial

ser = serial.Serial("/dev/ttyUSB0", baudrate=9600) #Modificar el puerto serie de ser necesario
comandos = ""

def moteino_send():
    global comandos
    if (comandos != ""):
        comandos += "\n"
        print(comandos)
        comandoBytes = comandos.encode()    
        ser.write(comandoBytes)
        comandos = ""


def moteino_write(comando: str):
    global comandos    
    comando += "\t"
    comandoBytes = comando.encode()
    #ser.write(comandoBytes)
    comandos += comando

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