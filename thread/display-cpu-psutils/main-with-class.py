import random
import threading
import psutil

class DisplayCPU(threading.Thread):

    def run(self):
        self.running = True
        
        current_process = psutil.Process()

        while self.running:
            print(current_process.cpu_percent(interval=1))

    def stop(self):
        self.running = False
    
# ----

def i_hate_this():
    tab = []
    for i in range(10000000):
        tab.append(random.randint(1, 10000))
    tab.sort()
    return tab

# ----

display_cpu = DisplayCPU()
display_cpu.start()

try:
    result = i_hate_this()
finally: # stop thread even when I press Ctrl+C
    display_cpu.stop()


