package main

import (
	"fmt"
)

//闭包
func adder() func(int) int {
	var x int
	return func(y int) int {
		x += y
		return x
	}
}

func adder2(x int) func(int) int {
	return func(y int) int {
		x += y
		return x
	}
}

func main() {
	//匿名函数
	//匿名函数赋值给变量
	add := func(x, y int) {
		fmt.Println(x + y)
	}
	add(1, 2) //调用变量，执行匿名函数

	//自执行匿名函数
	func(x, y int) {
		fmt.Println(x + y)
	}(10, 20)

	//闭包
	fmt.Println("")
	var f = adder()
	fmt.Println(f(40))
	fmt.Println(f(50))

	f1 := adder()
	fmt.Println(f1(40))
	fmt.Println(f1(50)) //在f1生命周期内，x一直存在

	fmt.Println("")
	f3 := adder2(10)
	fmt.Println(f3(10))
	fmt.Println(f3(20))
	fmt.Println(f3(30))

	//defer语句（先被defer的语句最后执行，最后defer的语句最先执行）
	fmt.Println("")
	//执行顺序是start、end、3、2、1
	fmt.Println("start")
	defer fmt.Println(1)
	defer fmt.Println(2)
	defer fmt.Println(3)
	fmt.Println("end")

}
