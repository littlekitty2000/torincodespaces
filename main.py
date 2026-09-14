def start_environment():
    subprocess.run("sudo fuser -k 8080/tcp && killall -9 Xvfb xpra firefox-esr 2>/dev/null", shell=True)
    
    print("[*] TORTORTOR...")
    subprocess.run("sudo service tor start", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("[*] the display thing bleh...")
    os.environ["DISPLAY"] = ":99"
    subprocess.Popen("Xvfb :99 -screen 0 1280x1024x24", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    
    print("[*] being NOT gay and smth abt the html...")
    xpra_cmd = "xpra start :99 --html=on --bind-tcp=0.0.0.0:8080 --exit-with-children=no --daemon=yes"
    subprocess.run(xpra_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    
    print("[*] The fox is on fire in a canvas...")
    firefox_cmd = "firefox-esr --profile ~/.mozilla/firefox/torprofile https://torproject.org &"
    subprocess.run(firefox_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("\n=======================================================")
    print("Tor is running now.")
    print("Tor")
    print("Why are you still here? If you don't know how to use this then READ THE README")
    print("=======================================================")
    print("\nok what did I JUST say lil bro")
