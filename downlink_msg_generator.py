"""
downlink msg:

struct msg{
    float altitude;
    float pressure;
    float acc[3];
    float gyro[3];
    float mag[3];
    float gps_pos[3];
    float gps_vel[3];
    float gps_fix;
    float ina260[9];
    float distance[3];
    float empty;
    int8_t bitfield1
    int8_t bitfield2
    int8_t bitfield3
    int8_t bitfield4
};//128 bytes
"""

DOWNLINK_STR_MAX_SIZE=4096

def encode_downlink_msg(s,size):
    #pad spaces in string
    s = s.ljust(size-1)
    s+='\0'
    s=s.encode()[:size]
    #print(s)
    #print(len(s))
    return s

def downlink_msg_generator(float31list,bool32list):
    global DOWNLINK_STR_MAX_SIZE
    if(len(float31list)!=31):#make sure it has 31 values
        print("error float31list size")
        if(len(float31list)>31):
            float31list=float31list[:31]
        while(len(float31list)<31):
            float31list.append(0)
        print(len(float31list))

    if(len(bool32list)!=32):#make sure it has 32 values
        print("error bool32list size")
        if(len(bool32list)>32):
            bool32list=bool32list[:32]
        while(len(bool32list)<32):
            bool32list.append(False)
        print(len(bool32list))
        
    bitfield_str=""
    for b in bool32list:
        if(b):
            bitfield_str+="1"
        else:
            bitfield_str+="0"

    float_str=""
    for n in float31list:                                                                                                                                                                               
        float_str=float_str+"{:.6f} ".format(n)
    
    msg=float_str+bitfield_str
    return encode_downlink_msg(msg,DOWNLINK_STR_MAX_SIZE)


print(downlink_msg_generator(list(range(31)),[True]*32))