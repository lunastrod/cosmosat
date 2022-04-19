"""
int sensor1 int sensor2 int sensor3
returns true/false if separated or not
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
    
    
"""
reads from distance sensors
returns true/false if separated or not
"""
def read_is_separated():
	#read s1
	#read s2
	#read s3
	return is_separated(s1,s2,s3)
	
	
"""
reads from altitude sensors
returns int altitude
"""
def read_altitude():
	#reads altitude from navio2
	return altitude

    
"""
returns true/false if able to activate microwave
"""
def can_activate_microwave():
	if(not read_is_separated()):
		return False
    if(read_altitude()<10000):
    	return False
    return True
    
"""
turns on power supply from microwave generator
"""
def activate_microwave():
    #turn on gpio pin


def loop:
	if(can_activate_microwave()):
		activate_microwave()