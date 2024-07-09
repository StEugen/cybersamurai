package main

import (
	"fmt"
	"net/http"
	"os"
)

func redirectHandler(w http.ResponseWriter, r *http.Request) {
	targetURL := os.Getenv("TARGET_URL")
	if targetURL == "" {
		http.Error(w, "TARGET_URL environment variable is not set", http.StatusInternalServerError)
		return
	}

	http.Redirect(w, r, targetURL, http.StatusFound)
}

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8000"  
	}

	http.HandleFunc("/", redirectHandler)
	fmt.Printf("Starting server on port %s\n", port)
	err := http.ListenAndServe(":"+port, nil)
	if err != nil {
		panic(err)
	}
}

