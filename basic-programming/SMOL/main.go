package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		var N, K int
		fmt.Scanf("%d %d", &N, &K)

		if K == 0 {
			fmt.Println(N)
		} else {
			fmt.Println(N % K)
		}
		T--
	}
}
