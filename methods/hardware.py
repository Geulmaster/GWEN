import sys
import memory_profiler as memP

def memory():
    for value in memP.memory_usage():
        print(f"{value*1.04858} MB") #MiB to MB

def exit():
    sys.exit()