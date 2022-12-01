package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		var N int
		fmt.Scanf("%d", &N)

		x := N % 4

		if x == 0 || x == 3 {
			fmt.Println(N)
		} else {
			fmt.Println(N - 1)
		}

		T--
	}
}
