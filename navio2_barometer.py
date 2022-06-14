import time
import numpy as np

'''
import navio.ms5611
import navio.util

if __name__ == "navio2_barometer":

    navio.util.check_apm()

    baro = navio.ms5611.MS5611()
    baro.initialize()


def get_pressure():

    global baro

    baro.refreshPressure()
	time.sleep(0.01) # Waiting for pressure data ready 10ms
	baro.readPressure()

    # es posible que no haga falta hacer esto aquí
    baro.refreshTemperature()
	time.sleep(0.01) # Waiting for temperature data ready 10ms
	baro.readTemperature()

    baro.calculatePressureAndTemperature()

    return baro.PRES


def get_temperature():

    global baro

    # es posible que no haga falta hacer esto aquí
    baro.refreshPressure()
	time.sleep(0.01) # Waiting for pressure data ready 10ms
	baro.readPressure()

    baro.refreshTemperature()
	time.sleep(0.01) # Waiting for temperature data ready 10ms
	baro.readTemperature()

    baro.calculatePressureAndTemperature()

    return baro.TEMP

'''

PRESSURE_11 = 22.65
PRESSURE_25 = 2.488


def get_altitude_from_pressure(pressure):

    #pressure = get_pressure()

    #dividimos entre 10 para pasar de milibar a kilopascal
    pressure /= 10

    if (pressure > PRESSURE_11):
        T = (pressure/101.29)**(0.19026)*288.08 - 273.1
        h = (T - 15.04)/-6.49E-3

    elif ((pressure < PRESSURE_11) and (pressure > PRESSURE_25)):
        T = -56.46
        h = (np.log(pressure/22.65) - 1.73)/-1.57E-4

    else:
        T = (pressure/2.488)**(-0.087812)*216.6 - 273.1
        h = (T + 131.21)/2.99E-3

    #obtenemos la altura en metros
    return h




# REDUNDANCY

# READER