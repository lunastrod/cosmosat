
import time 

#we need to use the function of the comand reader that gives the order to activate the deployment (we will call it as "activate" and it's a bool)

def pyro_switcher (activation: bool): #Activates de pyrocutter
    if (activation):
        print("ahora se mandaría la señal de output de true")
     #   gpio.output(nº de puerto donde está el pyro, True)
    else:
        print("ahora terminaría la señal")
     #   gpio.output(nº de puerto donde está el pyro, false)
    return



def pyro_management(height, activate: bool): #will manage the activation of the pyrocutter
    
    MAXIMUM_HEIGHT=10000 #this is the limit height, at which if the order to deploy has not been received, it must be deployed

    if (height< MAXIMUM_HEIGHT):
        if (activate):
            print("se activa1")
            return True
        else:
            print("no se activa")
            return False

    else:
        print("se activa2")
        return True
        



time_pyro_started=time.time()
activated= True

"""
def reset_activated ():

    if activate and (not activated) and (sensors_bool)

    global activated
    activated= True
    return
"""



def pyro_activation(activation: bool): #will send the signal to the pyrocutter to activate it, do it knowing hardware
    global time_pyro_started 
    global activated
    TIME_DELAY= 5 # time that we need to cut the thread
    T1= time_pyro_started
    T2= T1+ TIME_DELAY  
    T3=0
    
    if (activation) and (activated):
        pyro_switcher(True)
        T3=time.time()
    
    if (T3>T2):
        pyro_switcher(False)
        activated=False 
    return


if __name__ == "__main__":

    #while (True):
        pyro_on(pyro_activation(idx, False))
        time.sleep(1)

    for idx in range(0,12000,100):
        print(idx, end=" ")
        pyro_on(pyro_activation(idx, False))

    
