import time

def manage_commands(msg):
    

TOLERANCE_ERROR=-1
def compute_redundancy(sensors):
    global TOLERANCE_ERROR
    MINIMUM_DISTANCE=0.10#m less than this isn't possible, the sensor must be wrong
    TOLERANCE=0.05
    
    for i in range(len(sensors)):#delete wrong values
        if(sensors[i]<MINIMUM_DISTANCE):
            sensors.remove(i)
            #log error msg, sensor malfunction

    if(min(sensors)+TOLERANCE>max(sensors)):
        #good, our sensors agree
        return sum(sensors)/len(sensors)
    
    #our sensors don't agree
    #log error msg, sensor malfunction
    return TOLERANCE_ERROR
    

def is_separated(s1, s2, s3):
    global TOLERANCE_ERROR
    DEPLOY_DISTANCE=0.30#m
    final_sensor_value=compute_redundancy([s1,s2,s3])
    if(final_sensor_value==TOLERANCE_ERROR):
        print("error")
        #log error msg, sensor malfunction
        return False #not separated, for safety (manual override?)
    
    if(final_sensor_value>DEPLOY_DISTANCE):
        return True
    return False






def read_navio():
    return (1,"hola", 1.0323)

def log_data():
    with open("test.txt",'a', encoding = 'utf-8') as f:
        s='Hey {name}, there is a 0x{errno:x} error!\n'.format(name="hola", errno=1232)
        f.write(s)


time_recording_started=time.time()
def manage_camera():
    global time_recording_started
    VIDEO_LEGTH=5#seconds
    #print(time_recording_started, time.time())

    if(time_recording_started+VIDEO_LEGTH<time.time()):
        #print("han pasado 5m")
        print("para video")
        print("saca foto")
        print("empieza video")
        #para video
        #saca foto
        #empieza video
        time_recording_started=time.time()
    else:
        print("continuo grabando")


        

def setup():
    print("setup")

def main():
    print("main")
    while(True):
        #navio_data=read_navio()
        manage_camera()

        if(can_activate_microwave()):
		    activate_microwave()

        #log_data()
        time.sleep(1)
        pass


if __name__ == "__main__":
    setup()
    main()

