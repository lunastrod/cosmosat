
import time
from tkinter import Variable 

#we need to use the function of the comand reader that gives the order to activate the deployment (we will call it as "activate" and it's a bool)

def deploy_switcher (deploy_command: bool): #Activates de pyrocutter
    if (deploy_command):
        print("ahora se mandaría la señal de output de true")
     #   gpio.output(nº de puerto donde está el pyro, True)
    else:
        print("ahora terminaría la señal")
     #   gpio.output(nº de puerto donde está el pyro, false)
    return



def deploy_autonomous(altitude, autonomous_output: bool): #El segundo input va a ser la variable de output, que es una condición para el ejecutador
    MINIMUM_ALTITUDE=10000 #this is the limit height, at which if the order to deploy has not been received, it must be deployed
    MAXIMUM_ALTITUDE=10600

    if (altitude> MINIMUM_ALTITUDE) and (altitude< MAXIMUM_ALTITUDE):
        autonomous_output=True
    
    else:
        autonomous_output=False
    return


def deploy_activator(activation:bool, autonomous_output:bool, deploy_command:bool): #deploy_command es la variable que se mete luego en el switcher, es la que se activa finalmente. Activation es la q sale del command treader
    if activation or autonomous_output:
        deploy_command=True
    
    else:
        deploy_command=False
    return
    


def deploy_executor(activate:bool, autonomous_result:bool, deploy_order:bool, elevation): #En el loop principal, se llama a esta función y se le meten las 4 variables que requiere el deployment como input
    deploy_autonomous(elevation, autonomous_result)
    print(autonomous_result)
    deploy_activator(activate, autonomous_result, deploy_order)
    print(deploy_order)
    deploy_switcher(deploy_order)
    return



if __name__ == "__main__":

    activador=False
    autonomous=False
    order=False

    for idx in range(8000,12000,100):
        print(idx, end=" ")
        deploy_executor(activador, autonomous, order, idx)
        time.sleep(0.2)





"""
    #while (True):
        pyro_on(pyro_activation(idx, False))
        time.sleep(1)

    for idx in range(0,12000,100):
        print(idx, end=" ")
        pyro_on(pyro_activation(idx, False))

"""



















"""

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


def reset_activated ():

    if activate and (not activated) and (sensors_bool)

    global activated
    activated= True
    return




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





ESQUEMA
ejecutador:
llama a autonomous
llama a ejecutor_este 
llama a switcher



"""