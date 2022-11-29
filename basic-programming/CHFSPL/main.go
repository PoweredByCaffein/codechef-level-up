package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)

	for T > 0 {
		var A, B, C int
		fmt.Scanf("%d %d %d", &A, &B, &C)

		sum := A + B + C
		min := A

		if min > B {
			min = B
		}
		if min > C {
			min = C
		}

		fmt.Println(sum - min)

		T--
	}
}
