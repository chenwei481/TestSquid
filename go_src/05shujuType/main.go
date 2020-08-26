package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {
	var a int = 100
	fmt.Println(a)
	fmt.Printf("%b\n", a)  //%b二进制
	fmt.Printf("%o \n", a) //%o八进制
	fmt.Printf("%x\n", a)  //%x十六进制
	fmt.Printf("%f\n", math.Pi)
	fmt.Println("str := \"c:\\Code\\lesson1\\go.exe\"")

	j1 := `第一行
第二行
第三行
`
	j2 := "hello"
	j3 := j1 + j2
	fmt.Println(j1)
	fmt.Println(len(j1))
	fmt.Println(j3)
	l := "A,B,C"
	l1 := strings.Split(l, "B") //分割
	fmt.Println(l1)

	l2 := "A"
	l3 := strings.Contains(l, l2) //包含
	fmt.Println(l3)

	l4 := strings.Index(l2, l)
	l5 := strings.LastIndex(l2, l)
	fmt.Println(l4)
	fmt.Println(l5)

	s := []string{"foo", "bar", "baz"}
	fmt.Println(s)
	fmt.Println(strings.Join(s, "."))
}
