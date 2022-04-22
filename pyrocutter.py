

#we need to use the function of the comand reader that gives the order to activate the deployment (we will call it as "activate" and it's a bool)


def pyro_activation(height, activate: bool): #will manage the activation of the pyrocutter
    
    MAXIMUM_HEIGHT=10000 #this is the limit height, at which if the order to deploy has not been received, it must be deployed

    if height< MAXIMUM_HEIGHT:
        if activate:
            print("se activa1")
            return True
        else:
            print("no se activa")
            return False

    else:
        print("se activa2")
        return True
        

def pyro_on(activation: bool,); #will send the signal to the pyrocutter to activate it, do it knowing hardware
    if activation:
        gpio.
    return 


if __name__ == "__main__":

    for idx in range(0,11000,100):
        print(idx, end=" ")
        pyro_activation(idx, False)
