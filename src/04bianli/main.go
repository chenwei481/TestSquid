package main

import (
	"fmt"
	"math"
)

// 遍历字符串
func main() {
	s := "hello沙河"
	for i := 0; i < len(s); i++ { //byte
		fmt.Printf("%v(%c) ", s[i], s[i])
	}
	fmt.Println()
	for _, r := range s { //rune
		fmt.Printf("%v(%c) ", r, r)
	}
	fmt.Println()

	m1 := "dog"
	//类型转换
	bym1 := []byte(m1)
	bym1[0] = 'f'
	fmt.Println(string(bym1))

	m2 := "大大小小"
	bym2 := []rune(m2)
	bym2[1] = '中'
	fmt.Println(string(bym2))

	var a, b = 3, 4
	var c int
	// math.Sqrt()接收的参数是float64类型，需要强制转换
	c = int(math.Sqrt(float64(a*a + b*b)))
	fmt.Println(c)

	p1 := "hahaha哈嘿嘿希"
	pp1 := []rune(p1)
	fmt.Println(len(pp1))
	fmt.Println(len(p1))
	fmt.Println("汉字数量:", int((len(p1)-len(pp1))/2))
}
