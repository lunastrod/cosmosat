# cosmosat

TODO:
Funcion que calcule la altura a partir de barometro (pvlib.atmosphere?, navio?)

Ver como usar el gps de la navio2(https://docs.emlid.com/navio2/dev/gps-ublox-ucenter ????)

para configurar las ina con direcciones i2c: "ina260_2 = adafruit_ina260.INA260(i2c, address=0x41)"
biblioteca de las ina: sudo pip3 install adafruit-circuitpython-ina260

biblioteca de sensores de distancia https://github.com/pimoroni/VL53L0X-python/tree/master/python
para cambiar la direccion i2c https://github.com/pimoroni/VL53L0X-python/blob/master/python/VL53L0X.py

interfaz con la antena??? sockets??????????????????????? ficheros???????????

Logger

===========================================================================================================
Ficheros usados:
uplink_history.txt: guarda todos los mensajes de uplink que se han recibido
downlink_history.txt: guarda todos los mensajes de uplink que ha mandado

Log.txt: a una frecuencia fija escribe el estado actual
YYYY-MM-DD-HH:MM:SS:ms barometro(altura, presion), aceleracion, giroscopio, magnetometro, gps, 3 inas, 3 sensores distancia, separado?, transmitiendo?, grabando?

===========================================================================================================
mensaje de downlink:
barometro(altura, presion), aceleracion, giroscopio, magnetometro, gps, 3 inas, 3 sensores distancia, separado?, transmitiendo?, grabando?


===========================================================================================================
Funciones:

"""
configura los puertos de la raspberry, navio2 y todos los sensores y actuadores
"""
setup

main

"""

params: int sensor1 int sensor2 int sensor3
returns bool if separated or not
"""
is_separated

"""
reads from distance sensors
returns true/false if separated or not
"""
read_is_separated

"""
reads from altitude sensors
returns int altitude
"""
read_altitude

"""
returns true/false if able to activate microwave
"""
can_activate_microwave

"""
turns on power supply from microwave generator
"""
activate_microwave

===========================================================================================================

