import subprocess

def say(text):
    print(text)
    command = "cscript \"C:\Program Files\Jampal\ptts.vbs\""
    subprocess.call("echo " + text + " | " + command, shell=True)