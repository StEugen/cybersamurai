# Steps prepartions for windows

- Start-Service -Name WinRM
- Test-WSMan
From the C:\ drive: <br>
- $url ="https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
- $file = "$env:temp\ConfigureRemotingForAnsible.ps1"
- (New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
- powershell.exe -ExecutionPolicy ByPass -File $file
- winrm enumerate winrm/config/Listener


On Linux: <br>
- vim win_ping.yml
<pre>
- name: win_ping module test

  hosts: Windows_Host
  become: false
  gather_facts: false
  tasks:
    - name: test connection
      win_ping:
</pre>

- vim inventory.yml
<pre>
All:

  hosts:
    Windows_Host:
      ansible_host: {ip.address}
      ansible_user: {username.targeted.machine}
      ansible_password: {password.targeted.machine}
      ansible_connection: winrm
      ansible_port: 5986
      ansible_winrm_server_cert_validation: ignore
</pre>
- ansible-playbook win_ping.yml –i inventory.yml
