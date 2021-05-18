from platform import platform

os_name = platform()

def osType():
    if "linux" in os_name:
        return "linux"
    else:
        return "windows"
