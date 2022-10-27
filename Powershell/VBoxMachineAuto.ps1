#This is a powershell script for importing virtualbox machine from the internet from your server
#remember to $ Set-ExecutionPolicy unrestricted

wget "http://your-server/way/to/machine" -outfile "D:\where\to\put"
cd C:\way\to\virtualbox\directory\with\VBoxManage.exe
.\VBoxManage.exe unregistervm --delete "Win10"
.\VBoxManage.exe import D:\Win10.ova 
.\VBoxManage.exe modifyvm --memory <amount of RAM in mb> --cpus <number of cpus>
shutdown /s #optional comment if don't need