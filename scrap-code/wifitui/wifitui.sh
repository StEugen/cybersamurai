#!/bin/bash

scan_and_display_networks() {
  local networks=$(nmcli -t -f SSID,SIGNAL dev wifi list | sort -t: -k2 -n -r)
  local menu_items=()
  while IFS=: read -r ssid signal; do
    [ -n "$ssid" ] && menu_items+=("$ssid" "Signal: $signal")
  done <<<"$networks"
  dialog --menu "Select Wi-Fi Network" 20 50 10 "${menu_items[@]}" 2>/tmp/wifi_choice
  local exit_status=$?
  if [ $exit_status -ne 0 ]; then
    clear
    echo "No network selected. Exiting."
    exit 1
  fi
  cat /tmp/wifi_choice
}

connect_to_network() {
  local ssid=$1
  local password
  dialog --passwordbox "Enter Wi-Fi password for $ssid" 10 50 2>/tmp/wifi_password
  password=$(cat /tmp/wifi_password)
  nmcli dev wifi connect "$ssid" password "$password" >/tmp/wifi_result 2>&1
  if [ $? -eq 0 ]; then
    dialog --msgbox "Successfully connected to $ssid!" 10 50
  else
    dialog --msgbox "Failed to connect to $ssid. See details below:\n$(cat /tmp/wifi_result)" 20 50
  fi
}

clear
ssid=$(scan_and_display_networks)
connect_to_network "$ssid"
rm -f /tmp/wifi_choice /tmp/wifi_password /tmp/wifi_result
clear
