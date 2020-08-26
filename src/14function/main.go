package main

import (
	"errors"
	"fmt"
)

func intSum(x int, y int) int {
	return x + y
}

//可变参数后用...，传多个值会成为切片
func intSum2(x ...int) int {
	fmt.Println(x) //x是一个切片
	sum := 0
	for _, v := range x {
		sum = sum + v
	}
	return sum
}

//注：可变参数一般作为函数最后一个参数
func intSum3(x int, y ...int) int {
	fmt.Println(x, y)
	sum := x
	for _, v := range y {
		sum = sum + v
	}
	return sum
}

//返回多个值，同时调用时也需要多个接收
func cl(x int, y int) (int, int) {
	fmt.Println(x, y)
	sum := x + y
	sub := x - y
	return sum, sub
}

//返回值先命名，然后直接return返回
func cl2(x int, y int) (sum int, sub int) {
	fmt.Println(x, y)
	sum = x + y //确定返回值名称之后，就用=
	sub = x - y
	return
}

//用type定义函数类型
type calculation func(int, int) int

func add(x, y int) int {
	return x + y
}

//函数作为参数
func sub(x, y int) int {
	return x - y
}
func subSc(x, y int, op func(int, int) int) int { //传入一个op后面类型的参数
	return op(x, y)
}

func do(s string) (func(int, int) int, error) {
	switch s {
	case "+":
		return add, nil
	case "-":
		return sub, nil
	default:
		err := errors.New("无法识别的操作符")
		return nil, err
	}
}

func main() {
	res := intSum(1, 20) //调用函数
	fmt.Println(res)
	fmt.Println("")

	res1 := intSum2()
	res2 := intSum2(1)
	res3 := intSum2(1, 2, 3)
	fmt.Println(res1, res2, res3)

	fmt.Println("")
	res4 := intSum3(10)
	res5 := intSum3(10, 20)
	res6 := intSum3(10, 20, 30)
	fmt.Println(res4, res5, res6)

	fmt.Println("")
	res7, res8 := cl(10, 20) //多个变量接收多个返回值
	fmt.Println(res7)
	fmt.Println(res8)

	fmt.Println("")
	res9, res10 := cl2(30, 40)
	fmt.Println(res9)
	fmt.Println(res10)

	fmt.Println("")
	var c calculation    //定义变量的类型
	c = add              //能把calculation类型的函数都赋值都变量
	fmt.Println(c(1, 2)) //可以和调用add函数一样，调用c
	fmt.Printf("%T\n", c)

	f := add              // 将函数add赋值给变量f1
	fmt.Printf("%T\n", f) // type of f:func(int, int) int
	fmt.Println(f(10, 20))

	fmt.Printf("")
	res11 := subSc(100, 200, sub) //调用函数时传入一个符合定义类型的函数
	fmt.Println(res11)

	//res12, res13 := do("*")
	fmt.Println("")
	//fmt.Println(res12, res13)
}
