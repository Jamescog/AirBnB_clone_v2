from ast import arg
import cmd

class test(cmd.Cmd):


    def do_test(self, args):
        kwargs = {}
        commands = args.split(" ")
        for command in commands[1:]:
            key, value = tuple(command.split("="))
            value = value.replace("_", " ")
            value = value.replace('"', '\\"')
        
            kwargs[key] = value
        print(kwargs)


if __name__ == "__main__":
    test().cmdloop()