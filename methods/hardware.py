import sys
import memory_profiler as memP
import psutil
import speedtest
import GPUtil
from tabulate import tabulate


def memory():
    for value in memP.memory_usage():
        print(f"{value*1.04858} MB") #MiB to MB


def cpu():
    """
    CPU's load
    """
    print(str(psutil.cpu_percent()) + "%")
    return str(psutil.cpu_percent()) + "%"


def battery():
    battery_status = psutil.sensors_battery()
    if not battery_status:
        print("Device does not have a battery")
        return None
    print(f"Battery is {battery_status.percent}")
    return f"Battery is {battery_status.percent}"


def ram():
    """
    Used RAM
    """
    print(str(psutil.virtual_memory().percent) + "%")
    return str(psutil.virtual_memory().percent) + "%"


def processes():
    for process in psutil.process_iter():
        try:
            process_name = process.name()
            process_id = process.pid
            print(process_name, " ::: ", process_id)
        except (psutil.NoSuchProcess, \
            psutil.AccessDenied, psutil.ZombieProcess):
            pass


def network():
    print("Please wait a few seconds...")
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() * 0.000001 #Converts bytes to MBs
    upload_speed = st.upload() * 0.000001
    print(f"""Download speed is {download_speed} MB per second
            Upload speed is {upload_speed} MB per second""")
    return f"""Download speed is {download_speed} MB per second
            Upload speed is {upload_speed} MB per second"""


def graphics():
    gpus = GPUtil.getGPUs()
    gpus_list = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load*100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} C"
        gpus_list.append((gpu_id, gpu_name, gpu_load, 
        gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temperature))
    print(str(tabulate(gpus_list, headers=("id", "name", "load",
    "free memory", "used memory", "total memory", "temperature"))), "\n")


def exit():
    sys.exit()