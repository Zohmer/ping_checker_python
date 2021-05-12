import subprocess, time
from sys import platform

pingResult = ""
offline = True
online = True

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
    pingResultSplitted = pingResult.split(" ")

    timeout = True
    for segment in pingResultSplitted:
        if segment == "from" or segment == "From" or segment == "FROM":
            timeout = False
            if offline:
                offline = False
                online = True
                print("Target is online")
        
    if timeout and online:
        offline = True
        online = False
        print("Target is offline")
    
    time.sleep(delay)

