#!/bin/bash
echo "Updating system apt and installing dependencies..."
sudo apt update && sudo apt install -y tor xvfb xpra firefox-esr

echo "Putting the Tor in the Firefox..."
mkdir -p ~/.mozilla/firefox/torprofile
cat << 'EOF' > ~/.mozilla/firefox/torprofile/prefs.js
user_pref("network.proxy.type", 1);
user_pref("network.proxy.socks", "127.0.0.1");
user_pref("network.proxy.socks_port", 9050);
user_pref("network.proxy.socks_version", 5);
user_pref("network.proxy.socks_remote_dns", true);
EOF

echo "Installed."
