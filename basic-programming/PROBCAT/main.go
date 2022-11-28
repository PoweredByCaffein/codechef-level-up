package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		var x int
		fmt.Scanf("%d", &x)

		if x < 100 {
			fmt.Println("Easy")
		} else if x < 200 {
			fmt.Println("Medium")
		} else {
			fmt.Println("Hard")
		}

		T--
	}
}
