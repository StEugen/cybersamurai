package main

import (
	"fmt"
	"golang.org/x/crypto/ssh"
	"golang.org/x/crypto/ssh/terminal"
	"io"
	"net"
	"os"
	"strings"
)

func main() {
	if len(os.Args) != 5 {
		fmt.Println("Usage: spf <ssh_username> <ssh_host> <remote_port> <local_port>")
		os.Exit(1)
	}

	sshUsername := os.Args[1]
	sshHost := os.Args[2]
	remotePort := os.Args[3]
	localPort := os.Args[4]

	fmt.Printf("Enter password for %s@%s: ", sshUsername, sshHost)
	password, err := terminal.ReadPassword(int(os.Stdin.Fd()))
	if err != nil {
		fmt.Println("Failed to read password:", err)
		os.Exit(1)
	}
	fmt.Println()

	sshConfig := &ssh.ClientConfig{
		User: sshUsername,
		Auth: []ssh.AuthMethod{
			ssh.Password(string(password)),
		},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
	}

	sshClient, err := ssh.Dial("tcp", sshHost+":22", sshConfig)
	if err != nil {
		fmt.Println("Failed to dial SSH server:", err)
		os.Exit(1)
	}
	defer sshClient.Close()

	localListener, err := net.Listen("tcp", "localhost:"+localPort)
	if err != nil {
		fmt.Println("Failed to start local listener:", err)
		os.Exit(1)
	}
	defer localListener.Close()

	fmt.Printf("Forwarding remote port %s on %s to local port %s...\n", remotePort, sshHost, localPort)

	for {
		localConn, err := localListener.Accept()
		if err != nil {
			fmt.Println("Failed to accept incoming connection:", err)
			continue
		}

		go func(localConn net.Conn) {
			defer localConn.Close()

			remoteConn, err := sshClient.Dial("tcp", sshHost+":"+remotePort)
			if err != nil {
				fmt.Println("Failed to dial remote server:", err)
				return
			}
			defer remoteConn.Close()

			go func() {
				_, err := io.Copy(localConn, remoteConn)
				if err != nil && !strings.Contains(err.Error(), "use of closed network connection") {
					fmt.Println("Error while copying data from remote to local:", err)
				}
			}()

			_, err = io.Copy(remoteConn, localConn)
			if err != nil && !strings.Contains(err.Error(), "use of closed network connection") {
				fmt.Println("Error while copying data from local to remote:", err)
			}
		}(localConn)
	}
}

