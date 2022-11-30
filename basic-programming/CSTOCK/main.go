package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		var S, A, B, C float64
		fmt.Scanf("%f %f %f %f", &S, &A, &B, &C)
		newPrice := S + ((C / 100) * S)
		if newPrice >= A && newPrice <= B {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
		T--
	}
}
