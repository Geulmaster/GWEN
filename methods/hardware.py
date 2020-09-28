import sys
import memory_profiler as memP
import psutil

def memory():
    for value in memP.memory_usage():
        print(f"{value*1.04858} MB") #MiB to MB

def cpu():
    """
    CPU's load
    """
    print(str(psutil.cpu_percent()) + "%")

def ram():
    """
    Used RAM
    """
    print(str(psutil.virtual_memory().percent) + "%")

def exit():
    sys.exit()