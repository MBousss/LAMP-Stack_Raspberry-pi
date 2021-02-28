import os

def lampStackSetup():
    lampCommands = open("LAMP-commands.txt", "r")

    for command in lampCommands:
        os.system( command );
        print(command)

lamp = input('Setup LAMP Stack install (Yes or No): ').lower()

if lamp == 'yes':
    lampStackSetup();
