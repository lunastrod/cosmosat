"""

def read_is_separated():
    return True

microwave_on=False

def can_activate_microwave(ALTITUDE):
    global microwave_on
    manual_override=False
    if(manual_override):
        return True
    if(not read_is_separated()):
        return False

    if(microwave_on and ALTITUDE<8000):
        return False
    if(not microwave_on and ALTITUDE<10000):
        return False
    return True
    
def control_microwave():
    microwave_on=
    delay()
    #turn on gpio pin


for i in range(0,20000,100):
    print(i,end="")
    print(" ",can_activate_microwave(i))

"""


bytearray()