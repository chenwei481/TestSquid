package main

import (
	"fmt"
)

func main() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	i1 := 20
	//for循环的初始语句可以被忽略，但是初始语句后的分号必须要写
	for ; i1 > 10; i1-- {
		fmt.Println(i1)
	}

	i2 := 30
	//初始语句和结束语句都可以忽略
	for i2 > 20 {
		fmt.Println(i2)
		i2--
		//强制退出
		if i2 == 22 {
			break
		}
	}
}
