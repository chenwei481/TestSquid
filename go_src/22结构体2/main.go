package main

import (
	"fmt"
)

//结构体函数和方法

//定义结构体
type person struct {
	name string
	age  int
}

//结构体函数
func newPerson(name string, age int) *person {
	return &person{
		name: name,
		age:  age,
	}
}

//方法
/*func (接收者变量 接收者类型) 方法名(参数列表) (返回参数) {
    函数体
}
接收者变量：接收者中的参数变量名在命名时，官方建议使用接收者类型名称首字母的小写，而不是self、this之类的命名。例如，Person类型的接收者变量应该命名为 p，Connector类型的接收者变量应该命名为c等。*/
func (p person) student() {
	fmt.Println("好好学习")
	fmt.Println(p.name)
}

//指针类型接收者
/*什么时候应该使用指针类型接收者
需要修改接收者中的值
接收者是拷贝代价比较大的大对象
保证一致性，如果有某个方法使用了指针接收者，那么其他的方法也应该使用指针接收者。*/
func (p *person) setAge(newAge int) {
	p.age = newAge
}

//值类型接收（值类型接收只针对副本，不能修改接收者变量本身）
func (p person) setAge2(newAge int) {
	p.age = newAge
}

func main() {
	s := newPerson("jack", 19)
	s.student()
	fmt.Println(s.age) //19

	s.setAge(20)
	fmt.Println(s.age) //20

	s.setAge2(23)
	fmt.Println(s.age) //20（值类型接收只针对副本，不能修改接收者变量本身，所以这里还是20）

}
