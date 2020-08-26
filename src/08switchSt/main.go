package main

import (
	"fmt"
)

func main() {
	s := 3
	switch s {
	case 1:
		fmt.Println("1")
	case 2:
		fmt.Println("2")
	default:
		fmt.Println("33")

		switch n := 7; n {
		case 1, 2, 3:
			fmt.Println("1,2,3")
		case 4, 5, 6:
			fmt.Println("4,5,6")
		default:
			fmt.Println("gg")

			b := 10
			switch {
			case b > 5:
				fmt.Println("bbb")
				fallthrough
			case b != 10:
				fmt.Println("aaa")
			default:
				fmt.Println("gg")
			}
		}
	}
}
