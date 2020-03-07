import platform

os_name = platform.platform()

def osType():
    if "linux" in os_name:
        return "linux"
    else:
        return "windows"