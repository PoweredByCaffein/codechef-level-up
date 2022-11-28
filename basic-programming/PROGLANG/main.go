package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		var A, B, C, D, E, F int
		fmt.Scanf("%d %d %d %d %d %d", &A, &B, &C, &D, &E, &F)

		fmt.Println(A, B, C, D, E, F)
		if (A == C || A == D) && (B == C || B == D) {
			fmt.Println(1)
		} else if (A == E || A == F) && (B == E || B == F) {
			fmt.Println(2)
		} else {
			fmt.Println(0)
		}

		T--
	}
}
