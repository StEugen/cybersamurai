#!/bin/bash

status=$(nmcli radio wifi)

if [ "$status" = "enabled" ]; then
  nmcli radio wifi off
  echo "Wi-Fi is now OFF."
else
  nmcli radio wifi on
  echo "Wi-Fi is now ON."
fi
