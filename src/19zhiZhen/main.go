package main

//指针

import (
	"fmt"
)

func modify1(x int) {
	x = 100
}

func modify2(x *int) {
	//传入的是一个*int类型，
	*x = 100
}

func main() {
	//地址操作符&和取值操作符*是一对互补操作符，&取出地址，*根据地址取出地址指向的值。
	//a是变量，变量b 是变量a的内存地址，&b是变量a地址的地址
	a := 1
	b := &a
	fmt.Printf("a:%d   ptr:%p\n", a, &a)
	fmt.Printf("b:%p   type:%T\n", b, b)
	fmt.Println(&b)

	//指针取值(根据指针从内存取值)
	c := *b
	fmt.Println(c)
	fmt.Printf("b type:%T\n", b)
	fmt.Printf("c type:%T\n", c)

	//指针传值
	d := 20
	modify1(d)
	fmt.Println(d)
	modify2(&d)
	fmt.Println(&d)
	fmt.Println(d)

	//指针应用
	x := 2
	var y *int = &x //声明指针并赋值
	*y = 3          //改变内存地址的值
	fmt.Println(x)
}
