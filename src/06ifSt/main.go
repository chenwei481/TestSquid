package main

import (
	"fmt"
)

func main() {
	s1 := 90
	if s1 == 90 {
		fmt.Println(s1)
	} else if s1 > 90 {
		fmt.Println("bbb")
	} else {
		fmt.Println("1111")
	}

	if s2 := 10; s2 >= 90 {
		fmt.Println("A")
	} else if s2 == 10 {
		fmt.Println("B")
	} else {
		fmt.Println("C")
	}
}
