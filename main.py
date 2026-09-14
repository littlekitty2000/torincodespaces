import os
import subprocess
import time
import sys
import threading

def stop_environment():
    print("\n[*] Cleaning and clearing shit...")
    # Your exact cleanup routine sequence executed directly via system shell
    subprocess.run("sudo fuser -k 8080/tcp && killall -9 Xvfb xpra firefox-esr 2>/dev/null", shell=True)
    print("Adios amigo")
    os._exit(0) # Aggressively close all execution loops immediately

def monitor_text_input():
    """Listens."""
    while True:
        try:
            user_input = input().strip().lower()
            if user_input == "stop":
                stop_environment()
        except (KeyboardInterrupt, EOFError):
            stop_environment()

def start_environment():
    subprocess.run("sudo fuser -k 8080/tcp && killall -9 Xvfb xpra firefox-esr 2>/dev/null", shell=True)
    
    print("[*] Activating background Tor core circuit service...")
    subprocess.run("sudo service tor start", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("[*] Initializing virtual monitor canvas display...")
    os.environ["DISPLAY"] = ":99"
    subprocess.Popen("Xvfb :99 -screen 0 1280x1024x24", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    
    print("[*] Deploying Xpra HTML5 stream engine panel on Port 8080...")
    xpra_cmd = (
        "xpra start :99 --html=on --bind-tcp=0.0.0.0:8080 "
        "--start-child='firefox-esr --profile $HOME/.mozilla/firefox/torprofile https://torproject.org' "
        "--exit-with-children=no --daemon=yes"
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
