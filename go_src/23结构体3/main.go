package main

import "fmt"

//任意类型添加方法和结构体嵌套

//任意类型添加方法
type myInt int //将int自定义为myInt

func (m myInt) sayhello() { //为myInt添加一个sayhello方法
	fmt.Println("hello")
}

//结构体嵌套
type address struct {
	pv   string
	city string
}

type user struct {
	name    string
	address address
}

//嵌套匿名结构体
type user2 struct {
	name    string
	address //匿名结构体
}

func main() {
	var m1 myInt
	m1.sayhello()
	m1 = 10
	fmt.Printf("%#v,%T\n", m1, m1)

	//结构体嵌套
	user1 := user{
		name: "jack",
		address: address{
			pv:   "成都",
			city: "武侯",
		},
	}
	fmt.Printf("user1=%#v\n", user1)

	fmt.Println("")
	//匿名结构体嵌套
	var user3 user2
	user3.name = "LiSi"
	user3.address.pv = "重庆" //通过匿名结构体访问
	user3.city = "江北"       //直接访问
	fmt.Printf("%#v\n", user3)

}
