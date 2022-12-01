package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		var L, R int
		fmt.Scanf("%d %d", &L, &R)

		L, R = 2*L, 2*R
		fmt.Println(R - L + 1)

		T--
	}
}
