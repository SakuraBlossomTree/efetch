import distro
import platform
import os
import time
import psutil


yellow='\033[93m'
green='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

os_arch = platform.architecture()[0]

kernel = platform.release()

os_hostname = platform.node()

os_name = distro.name() 

uptime = time.time() - psutil.boot_time()

uptime = uptime // 60

uptime = int(uptime)

shell = os.popen("echo ${SHELL##*/}").read()

shell = shell.strip()

if __name__ == "__main__":
    

    f = open("./output.txt" , "w")

    f.write(b+cyan+f"           OS:  {os_name}\n\n")
    f.write(b+green+f"          Hostname:  {os_hostname}\n\n")
    f.write(b+red+f"        Shell:  {shell}\n\n")
    f.write(b+pink+f"    Kernel:  {kernel}\n\n")
    f.write(b+yellow+f"    Uptime:  {uptime} mins\n\n")
    
    f.close()
