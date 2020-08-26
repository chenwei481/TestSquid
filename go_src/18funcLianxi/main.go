package main

//练习，分金币

import (
	"fmt"
	"reflect"
)

var (
	coins = 50
	users = []string{
		"Matthew", "Sarah", "Augustus", "Heidi", "Emilie", "Peter", "Giana", "Adriano", "Aaron", "Elizabeth",
	}
	distribution = make(map[string]int, len(users))
)

func distribution1() int {
	for index1, v1 := range users {
		distribution[v1] = 0
		fmt.Println(distribution)
		fmt.Println(index1, v1)
		for index2, vv1 := range v1 {
			fmt.Printf("str[%d]=%c\n", index2, vv1)

			switch vv1 {
			case 'e', 'E':
				distribution[v1]++
				coins--
			case 'i', 'I':
				distribution[v1] += 2
				coins -= 2
			case 'o', 'O':
				distribution[v1] += 3
				coins -= 3
			case 'u', 'U':
				distribution[v1] += 4
				coins -= 4
			}
		}
	}
	fmt.Println(distribution)
	return coins
}

func main() {
	//left := dispatchCoin()
	//fmt.Println("剩下：", left)
	fmt.Println(coins)
	fmt.Println(users)
	fmt.Println(reflect.TypeOf(users))
	fmt.Println("")
	distribution1()
}
