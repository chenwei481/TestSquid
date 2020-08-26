package main

import "fmt"

/*
//指针应用

// 交换函数
func swap(a, b *int) {
	// 取a指针的值, 赋给临时变量t
	t := *a
	fmt.Println("t", t)
	// 取b指针的值, 赋给a指针指向的变量
	*a = *b
	fmt.Println("a:", *a, "b:", *b)
	// 将a指针的值赋给b指针指向的变量
	*b = t
	fmt.Println("t:", t)
}
func main() {
	// 准备两个变量, 赋值1和2
	a, b := 1, 2
	// 交换变量值
	swap(&a, &b)
	// 输出变量值
	fmt.Println("a:", a, "b:", b)
}
*/

//结构体练习
//结构体
type student struct {
	id   int
	name string
	age  int8
	mark int
}

//构造函数
func newStudent(id int, name string, age int8, mark int) *student {
	return &student{
		id:   id,
		name: name,
		age:  age,
		mark: mark,
	}
}

//方法
func (s *student) getAll(id int, name string, age int8, mark int) {
	s.id = id
	s.name = name
	s.age = age
	s.mark = mark
}

func main() {
	a := newStudent(1, "张", 20, 90)
	a.getAll(2, "张三", 12, 80)
	fmt.Println(a.age)
}
