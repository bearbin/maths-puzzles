package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	flag.Parse()
	challenge := flag.Arg(0)
	if "1" == challenge {
		fmt.Println(c1())
	} else if "2" == challenge {
		fmt.Println(c2())
	} else if "3" == challenge {
		fmt.Println(c3())
	} else {
		fmt.Println("Please enter a valid challenge number.")
		os.Exit(-1)
	}
}
