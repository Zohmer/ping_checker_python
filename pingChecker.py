import subprocess, time, re
from sys import platform

pingResult = ""
online = False
firstRun = True

if platform.startswith("win32") or platform.startswith("cygwin"):
    pingCount = "/n"
elif platform.startswith("linux") or platform.startswith("darwin"):
    pingCount = "-c"

print("Enter ping target: ", end = "")
target = input()
print("Enter ping request delay: ", end = "")
delay = int(input())

while(True):
    pingResult = str(subprocess.run(["ping", pingCount, "1", target], stdout=subprocess.PIPE, text=True))

    if re.search("from", pingResult, re.IGNORECASE) or re.search("From", pingResult, re.IGNORECASE) or re.search("FROM", pingResult, re.IGNORECASE):
        timeout = False
        if online == False:
            online = True
            print("Target is online")
        
    elif online or firstRun:
        online = False
        print("Target is offline")
    
    firstRun = False
    time.sleep(delay)

