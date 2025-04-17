package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Hello from Go Web Server on Scratch!")
}

func main() {
    http.HandleFunc("/", handler)
    fmt.Println("Server is running on :8080")
    http.ListenAndServe(":8080", nil)
}
