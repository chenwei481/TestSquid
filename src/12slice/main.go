package main

import (
	"fmt"
)

//切片
func main() {
	var sl1 []string
	var sl2 = []int{1, 2, 3}
	var sl3 = []bool{false, true}
	fmt.Println(sl1)
	fmt.Println(sl2)
	fmt.Println(sl3)

	fmt.Println(sl1 == nil)
	fmt.Println(sl2 == nil)
	fmt.Println(sl3 == nil)

	//通过对数组索引得到切片
	ar9 := [5]int{1, 3, 5, 7, 8}
	sl4 := ar9[1:4]
	fmt.Println(sl4, len(sl4), cap(sl4)) //cap代表索引的上限

	//sl5 := sl4[2:5] //可以通过索引拿到数组ar9的值，就算sl4没有也可以
	//fmt.Println(sl5)

	sl6 := ar9[0:3:4] //切片并设置最大的索引上限4
	fmt.Println(sl6, cap(sl6))

	//使用make()函数构造切片
	sl7 := make([]int, 2, 10) //2是切片中元素的数量，10是容量
	fmt.Println(sl7, len(sl7), cap(sl7))

	//切片共享底层数组，修改一个切片会影响另外一个切片
	sl8 := []int{1, 2, 3}
	sl9 := sl8
	sl9[0] = 10
	fmt.Println("sl8=", sl8)
	fmt.Println("sl9=", sl9)

	//遍历切片
	for index, value := range sl9 {
		fmt.Println("索引=", index, "值:", value)
	}

	//append添加数据（append添加不超过容量会改变原切片，超过不影响）
	var sl10 []int
	sl10 = append(sl10, 1, 2, 3)
	fmt.Println(sl10)
	sl11 := []int{4, 5, 6}
	fmt.Println(sl11)
	sl10 = append(sl10, sl11...) //切片之前的合并
	fmt.Println(sl10)

	//切片扩容（随着append增加元素，容量也相应增加）
	var sl12 []int
	for i := 0; i < 10; i++ {
		sl12 = append(sl12, i)
		fmt.Println("len", len(sl12), "cap", cap(sl12), sl12)
	}

	//copy函数(copy函数是把复制到另外一片内存，不会改变原复制的切片)
	fmt.Println("")
	sl13 := []int{1, 2, 3, 4, 5}
	sl14 := make([]int, 5, 5)
	copy(sl13, sl14)
	fmt.Println(sl13)
	fmt.Println(sl14)
	sl13[0] = 10
	fmt.Println(sl13)
	fmt.Println(sl14)

	//删除(从切片a中删除索引为index的元素，操作方法是a = append(a[:index], a[index+1:]...))
	fmt.Println("")
	var sl15 = []int{1, 2, 3, 4, 5}
	fmt.Println(sl15)
	sl15 = append(sl15[:2], sl15[3:]...)
	fmt.Println(sl15)

	var a = make([]string, 5, 10)
	for i := 0; i < 10; i++ {
		a = append(a, fmt.Sprintf("%v", i))
	}
	fmt.Println(a)

}
