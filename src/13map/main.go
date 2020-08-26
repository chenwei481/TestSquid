package main

//map是一种无序的基于key-value的数据结构

import (
	"fmt"
	"math/rand"
	"sort"
	"strings"
	"time"
)

func main() {
	map1 := make(map[string]int, 5)
	map1["hello"] = 10
	map1["哈哈哈"] = 29
	fmt.Println(map1)
	fmt.Println(map1["哈哈哈"])
	fmt.Printf("type of a:%T\n", map1)
	fmt.Println("")

	map2 := map[int]string{
		1: "hahhah",
		2: "哈哈哈",
	}
	fmt.Println(map2)

	//判断值是否存在map，如果存在，ok为true
	v, ok := map2[1]
	if ok {
		fmt.Println(v)
	} else {
		fmt.Println("gg")
	}
	fmt.Println("")

	//遍历map
	for k, v := range map2 {
		fmt.Println(k, v)
	}
	fmt.Println("")

	//删除
	delete(map2, 2) //删map2中键为2的
	for k, v := range map2 {
		fmt.Println(k, v)
	}

	//按照指定顺序遍历map
	rand.Seed(time.Now().UnixNano()) //初始化随机数种子
	var map3 = make(map[string]int, 200)
	for i := 0; i < 100; i++ {
		key := fmt.Sprintf("stu%02d", i) //生成stu开头的字符串
		value := rand.Intn(100)          //生成0~99的随机整数
		map3[key] = value
		// for k1, v1 := range map3 {
		// fmt.Println(k1, v1)
		// }

		//取出map中的key存入keys
		var keys = make([]string, 0, 200)
		for key := range map3 {
			keys = append(keys, key)
		}

		//使用sort对切片进行排序
		sort.Strings(keys)
		for _, key := range keys {
			fmt.Println(key, map3[key])
		}
	}
	fmt.Println("")

	//元素类型是map的切片
	var mapSlice = make([]map[string]string, 3) //定义切片，类型为map
	for index, value := range mapSlice {
		fmt.Printf("index:%d value:%v\n", index, value)
	}
	fmt.Println("after init")
	// 对切片中的map元素进行初始化
	mapSlice[0] = make(map[string]string, 10) //定义索引为0的元素
	mapSlice[0]["name"] = "小"
	mapSlice[0]["password"] = "123456"
	mapSlice[0]["address"] = "沙"
	for index, value := range mapSlice {
		fmt.Printf("index:%d value:%v\n", index, value)
	}

	fmt.Println("")
	//切片类型的map
	var sliceMap = make(map[string][]string, 3) //定义map，里面元素类型为切片
	fmt.Println(sliceMap)
	fmt.Println("after init")
	key := "中国"
	value, ok := sliceMap[key]
	if !ok {
		value = make([]string, 0, 2)
	}
	value = append(value, "北京", "上海")
	sliceMap[key] = value
	fmt.Println(sliceMap)

	fmt.Println("")

	word := "how do you do"
	newword := strings.Split(word, " ")
	fmt.Println(newword)
	result := make(map[string]int, 8)
	for _, v := range newword {
		fmt.Println(v)
		fmt.Println(result)
		result[v] = result[v] + 1
	}
	fmt.Println(result)

}
