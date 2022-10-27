wget "http://10.0.122.153:82/Win10.ova" -outfile "D:\Win10.ova"
#Set-ExecutionPolicy unrestricted

cd C:\'Program Files'\Oracle\VirtualBox\

.\VBoxManage.exe unregistervm --delete "Win10"
.\VBoxManage.exe import D:\Win10.ova 

shutdown /s