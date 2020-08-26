package main

import "fmt"

func funcA() {
	fmt.Println("func A")
}

//recover()必须搭配defer使用。
//defer一定要在可能引发panic的语句之前定义。
func funcB() {
	defer func() {
		err := recover()
		//如果程序出出现了panic错误,可以通过recover恢复过来
		if err != nil {
			fmt.Println("recover in B")
		}
	}()
	panic("panic in B")
}

func funcC() {
	fmt.Println("func C")
}
func main() {
	funcA()
	funcB()
	funcC()
}
