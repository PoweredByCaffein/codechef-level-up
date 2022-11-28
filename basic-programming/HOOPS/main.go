package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)

	for T > 0 {
		var N int
		fmt.Scanf("%d", &N)

		fmt.Println((N / 2) + 1)

		T--
	}
}
