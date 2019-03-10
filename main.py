from init_speech import init_speech
from say import say
from commands import Commander

commander = Commander("Siri")
while(True):
    command = init_speech()
    if len(command) > 0:
        print(command)
        commander.discover(command)
    else:
        break