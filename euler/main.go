package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	flag.Parse()
	switch flag.Arg(0) {
	case "1":
		fmt.Println(c1())
	case "2":
		fmt.Println(c2())
	case "3":
		fmt.Println(c3())
	case "4":
		fmt.Println(c4())
	case "5":
		fmt.Println(c5())
	default:
		fmt.Println("Please enter a valid challenge number.")
		os.Exit(-1)
	}
}
