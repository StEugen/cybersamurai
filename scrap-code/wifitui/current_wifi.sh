#!/bin/bash
ssid=$(nmcli -t -f ACTIVE,SSID dev wifi | grep '^yes' | cut -d: -f2)
if [ -z "$ssid" ]; then
  echo "Not connected to any network."
else
  echo "Connected to Wi-Fi network: $ssid"
fi
