package main

import (
	"fmt"
)

//内置函数new和make

func main() {
	//new函数得到的是一个类型指针，零值
	a := new(int)
	b := new(bool)
	fmt.Printf("%T\n", a)
	fmt.Printf("%T\n", b)
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(*a)
	fmt.Println(*b)

	//make
	sl7 := make([]int, 2, 10)       //构造切片 2是切片中元素的数量，10是容量
	map1 := make(map[string]int, 5) //构造map
	c := make(chan int)             //构造channel

	map1["hello"] = 100
	fmt.Println("")
	fmt.Println(sl7)
	fmt.Println(map1)
	fmt.Println(c)

}

/*
1、二者都是用来做内存分配的。
2、make只用于slice、map以及channel的初始化，返回的还是这三个引用类型本身；
3、而new用于类型的内存分配，并且内存对应的值为类型零值，返回的是指向类型的指针。
*/
