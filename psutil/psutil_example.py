import psutil
import os
import time

os.system("title System Monitoring")
os.system("color A")

while True:

    os.system("cls")

    print("\n Processes:",len(psutil.pids()))

    cpu_n = 0

    for cpu in psutil.cpu_percent(percpu=True):
        cpu_n += 1
        print("\n CPU %s: %.1f%%"%(cpu_n,cpu))
    
    battery = psutil.sensors_battery()
    print("\n Battery: %i%%"%battery.percent)

    memory = psutil.virtual_memory()
    print("\n Memory: %.1f%%"%memory.percent)

    time.sleep(1)

    