package main

import "fmt"

const (
	h1 = 1
	h2 = "haha"
)

const (
	n1 = iota
	n2
	n3
)

const (
	d1 = iota //0
	d2        //1
	_
	d4 //3
)

const (
	c1 = iota //0
	c2 = 100  //100
	c3 = iota //2
	c4        //3
)

func main() {
	fmt.Println(h1)
	fmt.Println(h2)
	fmt.Println(n1)
	fmt.Println(n2)
	fmt.Println(n3)
	fmt.Println(d1)
	fmt.Println(d2)
	fmt.Println(d4)
	fmt.Println(c1)
	fmt.Println(c2)
	fmt.Println(c3)
	fmt.Println(c4)
}
