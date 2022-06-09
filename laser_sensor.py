"""
int sensor1 int sensor2 int sensor3
returns true/false if separated or not
"""
import time #SE HA TRABAJADO EN CM, PASAR LAS DISTANCIAS SI LA LECTURA DA EN OTRAS UNIDADES
"""
import VL53L0X

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
# I2C Address can change before tof.open()
# tof.change_address(0x32)
tof.open()
# Start ranging
tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

timing = tof.get_timing()
if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing/1000))

for count in range(1, 101):
    distance = tof.get_distance()
    if distance > 0:
        print("%d mm, %d cm, %d" % (distance, (distance/10), count))

    time.sleep(timing/1000000.00)

tof.stop_ranging()
tof.close()
"""
sensor1=VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
sensor1.change_address(0x32)

sensor2=VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
sensor2.change_address(0x31)

sensor3=VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)

def sensor_lecture() #debemos haber creado 3 objetos antes que serán los sensores con sus adress bien, FIJARSE BIEN EN ESO
    lecture1=sensor1.get_distance()
    lecture2=sensor2.get_distance()
    lecture3=sensor3.get_distance()

    distance= [lecture1,lecture2,lecture3]
    return distance


#se hace lectura de las 3, si el maximo y el minimo salen de la tolerancia, se descarta la mas alejada. Si entre las otras sigue sin cumplirse la tolerancia, se descarta la lactura entera

def sensor_redoundancy (distance) #Si se descarta alguna de las lecturas, sacar un mensaje de error. MIRAR CUAL ES EL VALOR Q SE LEE CUANDO NO REBOTA EN NADA
    TOLERANCE=5 # todas las distancias están en cm
    DEPLOY_LIMIT= 40
    mu=0
   
    for i in range(len(distance)):
        if (distance[i] <= 0):
            distance.pop(i)

    if (distance[1]> DEPLOY_LIMIT) and (distance[2]> DEPLOY_LIMIT) and (distance[3]> DEPLOY_LIMIT)
        return 200 #este número es suficientemente grande como para que la función deployment_management lo interprete como desplegado

    mu=sum(distance)/len(distance)
    if (max(distance)-min(distance)) > TOLERANCE:              
        distance.sort()
        if (abs(distance[1]-mu)) > (abs(distance[3]-mu)):
            distance.pop(1)
        else:
            distance.pop(3)
        
        mu= sum(distance)/len(distance)
        if (distance[2]-distance[1])> TOLERANCE:
            return -1 #Al devolver un número negativo, se muestra un error en la lectura de los sensores

        return mu
    return mu



def deployment_management (final_distance):
    SYSTEM_DEPLOYED= 25

    if final_distance > SYSTEM_DEPLOYED:
        return True

    elif final_distance < 0:
        return False 
        #WARNING DE Q NO SE HA HECHO BIEN LA MEDIDA XQ LOS 3 HAN DADO FUERA DE TOLERANCIA
        

    else:
        return False




def sensor_executor():
    distances_list= sensor_lecture()
    distance_measure= sensor_redoundancy (distances_list)
    return deployment_management(distance_measure)








"""

def is_separated(s1,s2,s3):


	#make sure the inputs aren't weird
	#are they ints? are they positive?
	#if they are weird, log an error msg
	
	#decide which is the most reliable sensor
	distance=most_reliable_sensor
	
	#is it separated?
	if(distance<threshold):
		return False
    return True
    
    


reads from distance sensors
returns true/false if separated or not

def read_is_separated():
	#read s1
	#read s2
	#read s3
	return is_separated(s1,s2,s3)


ORDEN DEL EJECTOR:
1-lectura de sensores da una lista
2-sensor redoundancy da un valor final
3 deployment_management da un bool 


"""