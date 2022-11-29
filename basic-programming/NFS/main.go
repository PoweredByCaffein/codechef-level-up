package main

import (
	"fmt"
	"math"
)

func main() {
	var T int
	fmt.Scanf("%d", &T)

	for T > 0 {
		var U, V, A, S int
		fmt.Scanf("%d %d %d %d", &U, &V, &A, &S)
		
		if U <= V {
			fmt.Println("Yes")
		} else {
			temp := (U*U) - (2*A*S)
			if temp <= 0 {
				fmt.Println("Yes")
			} else {
				minVelocity := math.Sqrt(float64(temp))
				if minVelocity <= float64(V) {
					fmt.Println("Yes")
				} else {
					fmt.Println("No")
				}
			}
		}

		T--
	}
}
