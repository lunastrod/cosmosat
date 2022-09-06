from time import time
from os import makedirs,path

#log errors, warnings or debug msgs here, useful during testing
ERROR_FILE="log/err.txt"
#file to log every telemetry packet
TELEMETRY_FILE="log/telemetry.txt"
#csv file for flight data, useful for analysis afterwards
FLIGHT_INFO_FILE="log/flight_info.csv"

#writes a line to a file with a timestamp, do not use outside this module
def write_line(file,line):
    makedirs(path.dirname(file), exist_ok=True)
    with open(file,'a') as f:
        print("{t:.6f},{data}".format(t=time(),data=line),file=f)

#input a list to this function, it will write it to the TELEMETRY_FILE in csv format
def log_flight_info(list):
    write_line(FLIGHT_INFO_FILE,",".join(map(str,list)))

#log error msg to ERROR_FILE
def log_error_msg(error_str):
    write_line(ERROR_FILE,"ERROR:   {s}".format(s=error_str))

#log warning msg to ERROR_FILE
def log_warning_msg(warning_str):
    write_line(ERROR_FILE,"WARNING: {s}".format(s=warning_str))

#log info msg to ERROR_FILE
def log_info_msg(warning_str):
    write_line(ERROR_FILE,"INFO:    {s}".format(s=warning_str))

def log_uplink_msg(uplink_bytes):
    write_line(TELEMETRY_FILE,"UPLINK:   {s}".format(s=uplink_bytes))

def log_downlink_msg(downlink_bytes):
    write_line(TELEMETRY_FILE,"DOWNLINK: {s}".format(s=downlink_bytes))

if(__name__=="__main__"):
    log_flight_info((1.0,231.123687,817623.182,812.812))
    log_error_msg("laser sensor error: tolerance too big")
    log_warning_msg("downlink bytearray bigger than 64 bytes")
    log_uplink_msg(bytes.fromhex("cafebaca"))
    log_downlink_msg(bytes.fromhex("cafe"*32))


