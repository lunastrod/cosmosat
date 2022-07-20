import VL53L0X


## initialize sensor obj
sensor_i2c_address = 0x29
sensor1=VL53L0X.VL53L0X(i2c_bus=1, i2c_address=sensor_i2c_address)


def get_laser_sensor_distance():

    ## obtain distance
    distance = sensor1.get_distance()

    return distance