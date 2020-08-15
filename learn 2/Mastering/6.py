import cmd

class Interface(cmd.Cmd):
    prompt = "Command: "
    def do(self, arg):
        print(arg)

interface = Interface()
interface.cmdloop()
