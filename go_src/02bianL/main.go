package main

import (
	"fmt"
)

var (
	s1 string
	s2 int
	s3 bool
)

var s4 = 3.14

func foo() (int, string) {
	return 10, "dada"
}

func main() {
	s5 := 100 //短声明
	var s1 = "sq"
	var s2 = 123
	var s3 = true
	fmt.Println(s1)
	fmt.Println(s2)
	fmt.Println(s3)
	fmt.Println(s4)
	fmt.Println(s5)

	x, _ := foo()
	fmt.Println("x=", x)
}
