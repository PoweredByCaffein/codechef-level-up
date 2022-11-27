package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)

	for T > 0 {
		var D, L, R int
		fmt.Scanf("%d %d %d", &D, &L, &R)

		if D >= L && D <= R {
			fmt.Println("Take second dose now")
		} else if D < L {
			fmt.Println("Too Early")
		} else {
			fmt.Println("Too Late")
		}

		T--
	}
}
