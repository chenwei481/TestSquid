package main

import (
	"fmt"
)

func main() {
	var ar1 [3]int
	var ar2 = [2]int{1, 2}
	var ar3 = [3]string{"成都", "重庆", "beijing"}
	var ar4 = [...]string{"111", "222"} //不指定数量，编译器自行推断
	ar5 := [...]int{1, 2, 3}
	ar6 := [...]string{1: "hello", 4: "hi"} //根据索引指定数组值
	fmt.Println(ar1)
	fmt.Println(ar2)
	fmt.Println(ar3)
	fmt.Println(ar4)
	fmt.Println(ar5)
	fmt.Println(ar6)
	fmt.Println("")

	//遍历1
	for i := 0; i < len(ar3); i++ {
		fmt.Println(ar3[i])
	}

	//遍历2
	for index, value := range ar3 {
		fmt.Println(index, value)
	}

	//二维数组
	ar7 := [3][2]string{
		{"成都", "重庆"},
		{"北京", "南京"},
		{"江苏", "浙江"},
	}
	fmt.Println(ar7)
	fmt.Println(ar7[1])
	fmt.Println(ar7[0][1])

	//二维数组遍历
	for _, v1 := range ar7 {
		for i2, v2 := range v1 {
			fmt.Println(i2, v2)
		}
		fmt.Println("")
	}

	//练习
	//计算数组内的值的和
	ar8 := [...]int{1, 3, 5, 7, 8}
	a := 0
	for _, va1 := range ar8 {
		//fmt.Println(va1)
		a += va1
	}
	fmt.Println(a)
	fmt.Println("")

	//计算数组内加减
	ar9 := [...]int{1, 3, 5, 7, 8}
	for k := 0; k < len(ar9); k++ {
		for p := 0; p < len(ar9); p++ {
			//fmt.Println(ar9[k] + ar9[p])
			h := ar9[k] + ar9[p]
			if h == 8 {
				fmt.Println(ar9[k], ar9[p])
			}
		}
	}
}
