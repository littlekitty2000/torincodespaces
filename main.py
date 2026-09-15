import os
import subprocess
import time
import sys
import threading

def stop_environment():
    print("\n[*] Cleaning and clearing shit...")
    subprocess.run("sudo fuser -k 8080/tcp && killall -9 Xvfb xpra firefox-esr 2>/dev/null", shell=True)
    print("Adios amigo")
    os._exit(0)

def monitor_text_input():
    while True:
        try:
            user_input = input().strip().lower()
            if user_input == "stop":
                stop_environment()
        except (KeyboardInterrupt, EOFError):
            stop_environment()

def start_environment():
    subprocess.run("sudo fuser -k 8080/tcp && killall -9 Xvfb xpra firefox-esr 2>/dev/null", shell=True)
    subprocess.run("rm -rf /tmp/.X11-unix/X100 /tmp/.X100-lock 2>/dev/null", shell=True)
    
    print("[*] Puttiing the Tor in FireFo- oh wait FireFox doesn't even have a t in it...")
    subprocess.run("sudo service tor start", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    real_home = os.path.expanduser("~")
    
    print("[*] Putting Xpra on 8080...")
    xpra_cmd = (
        f"xpra start :100 --xvfb='Xvfb -screen 0 1280x1024x24' --html=on --bind-tcp=0.0.0.0:8080 "
        f"--start-child='firefox-esr --profile {real_home}/.mozilla/firefox/torprofile https://torproject.org' "
        f"--exit-with-children=no --daemon=yes"
    )
    subprocess.run(xpra_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("\n=======================================================")
    print("Tor is running now.")
    print("Tor")
    print("Why are you still here? If you don't know how to use this then READ THE README")
    print("=======================================================")
    print("\nok what did I JUST say lil bro")

if __name__ == "__main__":
    try:
        start_environment()
        input_thread = threading.Thread(target=monitor_text_input, daemon=True)
        input_thread.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_environment()
#why are you looking in the code?
