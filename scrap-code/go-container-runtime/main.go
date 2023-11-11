package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main(){
	switch os.Args[1]{
		case "run":
			run()
		default:
			panic("Error")
	}
}

func run(){
	cmd := exec.Command(os.Args[2], os.Args[3:]...)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS,
	}


	must(cmd.Run()) 
}

func must(err error){
	if err != nil{
		panic(err)
	}
}
