

#translates 4 bytes into a command
COMMAND_TRANSLATION={
    b'\x01\x00\x00\x00':"force_deployment",
    b'\x02\x00\x00\x00':"null",
    b'\x03\x00\x00\x00':"null",
    b'\x04\x00\x00\x00':"null",
    b'\x05\x00\x00\x00':"null",
    b'\x06\x00\x00\x00':"null",
    b'\x07\x00\x00\x00':"null",
}


class up_command():
    def __init__(self):
        #self.last_uplink_msg = bytes(4)
        self.commands=self.init_commands()
    
    def init_commands(self):
        result={}
        for uplink_bytes in COMMAND_TRANSLATION:
            result[COMMAND_TRANSLATION[uplink_bytes]]=False
        return result
    
    def update_uplink_msg(self,msg):
        translated=COMMAND_TRANSLATION.get(msg)
        if(translated==None):
            #warning, update_uplink_msg wrong msg
            return None
        self.commands[translated]=True
        #TODO: update this to add args to commands. Probably overkill for this project, but not really that hard to make
    
    #returns true
    def get_command(self,str_command):
        value=self.commands.get(str_command)
        if(value==None):
            #warning, tried to access wrong str_command
            return None
        self.commands[str_command]=False
        return value

    def look_command(self,str_command):
        value=self.commands.get(str_command)
        if(value==None):
            #warning, tried to look wrong str_command
            return None
        return value


if(__name__=="__main__"):
    x=up_command()
    print("testing update")
    x.update_uplink_msg(123123)
    print(x.commands)
    x.update_uplink_msg(b'\x01\x00\x00\x00')
    print(x.commands)
    x.update_uplink_msg(b'\x09\x00\x00\x00')
    print(x.commands)


    print("testing wrong command")
    print(x.get_command("force_deploymenta"))
    print("testing get")
    x.update_uplink_msg(b'\x01\x00\x00\x00')
    print(x.get_command("force_deployment"))
    print(x.get_command("force_deployment"))
    print(x.get_command("force_deployment"))
    x.update_uplink_msg(b'\x01\x00\x00\x00')
    print(x.get_command("force_deployment"))
    print(x.get_command("force_deployment"))
    print("testing look")
    x.update_uplink_msg(b'\x01\x00\x00\x00')
    print(x.look_command("force_deployment"))
    print(x.look_command("force_deployment"))
    print(x.look_command("force_deployment"))
    print(x.look_command("force_deployment"))
    print(x.look_command("force_deployment"))
    print(x.get_command("force_deployment"))
    print(x.look_command("force_deployment"))





