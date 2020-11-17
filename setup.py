import os

def lampStackSetup():
    lampCommands = open("LAMP-commands.txt", "r")

    for command in lampCommands:
        # os.system( command );
        print(command)

def ftpServerSetup():
    ftpCommands = open("FTP-commands.txt", "r")

    for command in ftpCommands:
        # os.system( command );
        print(command)

# def f(x):
#     return {
#         'a': test(),
#         'b': 2,
#     }[x]

lamp = input('Setup LAMP Stack install (Yes or No): ').lower()
ftp = input('Setup FTP acces (Yes or No): ').lower()

if lamp == 'yes':
    lampStackSetup();
elif ftp == 'yes':
    ftpServerSetup();

