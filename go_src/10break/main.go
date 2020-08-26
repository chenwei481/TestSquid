package main

import (
	"fmt"
)

func main() {
	//bbb:
	for i := 1; i < 10; i++ {
		for j := 1; j <= i; j++ {
			//if j == 10 {
			//	break //bbb //不指定bbb标签，只跳出本次循环；指标签可以跳出指定的标签的循环
			//}
			fmt.Printf("%v*%v=%v\t", i, j, i*j)
		}
		fmt.Println("")
	}
}
