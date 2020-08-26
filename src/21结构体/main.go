package main

import (
	"fmt"
)

//类型别名和自定义类型
type newint int    //定义类型，具有int类型的特性
type newint2 = int //定义类型别名

//定义结构体（person是类型名，关键字struct）
type person struct {
	name, city string
	age        int
}

func main() {
	var a newint
	var b newint2
	fmt.Printf("%T\n", a) //定义类型的变量就是一个新的类型
	fmt.Printf("%T\n", b) //定义类型别名的变量还是int类型

	fmt.Println("")
	//结构体基本实例化
	var s1 person
	s1.name = "张三"
	s1.city = "成都"
	s1.age = 18
	fmt.Printf("s1=%v\n", s1)
	fmt.Printf("类型：%T\n", s1)

	//匿名结构体(临时数据场景)
	var user struct {
		id   int
		like string
	}
	user.id = 1
	user.like = "basketball"
	fmt.Println(user)
	fmt.Println("")

	//指针类型结构体
	var s2 = new(person)
	fmt.Printf("%v\n", s2)
	fmt.Printf("%T\n", s2)

	s2.name = "jack"
	s2.city = "成都"
	s2.age = 18
	fmt.Printf("s2:%v\n", s2)

	fmt.Println("")
	//取结构体的地址实例化
	s3 := &person{}
	fmt.Printf("%T\n", s3)
	fmt.Println("s3=", s3)
	s3.age = 10
	s3.name = "hhh"
	s3.city = "lll"
	fmt.Println(s3)
	fmt.Println(*s3) //直接取值

	fmt.Println("")
	//使用键值对初始化
	s5 := person{
		name: "哈哈哈",
		city: "dd",
		age:  19,
	}
	fmt.Println(s5)

	s6 := &person{
		name: "快快快",
		//city: "kkk", //没有值可以不写
		age: 10,
	}
	fmt.Println(s6) //指针
	fmt.Println(*s6)

	//初始化简写的话必须写上所有定义的值，且顺序不能乱
	s7 := &person{
		"来来来",
		"啦啦啦",
		17,
	}
	fmt.Printf("s7=%#v\n", s7)

	//内存结构对齐
	type test struct {
		a int8
		b int8
		c int8
	}
	n := test{
		1,
		2,
		3,
	}
	fmt.Printf("n.a %p\n", &n.a) //n.a 0xc00011e0f8
	fmt.Printf("n.b %p\n", &n.b) //n.b 0xc00011e0f9
	fmt.Printf("n.c %p\n", &n.c) //n.c 0xc00011e0fa

	fmt.Println("")
	//调用结构体函数
	n2 := newPer("jire", "成都", 10)
	fmt.Printf("n2=%#v", n2)
}

//构造结构体函数
func newPer(name, city string, age int) *person {
	return &person{
		name: name,
		city: city,
		age:  age,
	}
}
