import time

def write_line(file,line):
    with open(file,'a') as f:
        print("{t:.6f},{data}".format(t=time.time(),data=line),file=f)

while(True):
    write_line("a.csv","hola")
    time.sleep(1)
