package main

import "fmt"

func main() {
	var T int
	fmt.Scanln(&T)
	for T > 0 {
		var A, B, X int
		fmt.Scanf("%d %d %d", &A, &B, &X)

		requiredWealth := B - A

		if requiredWealth%X == 0 {
			fmt.Println(requiredWealth / X)
		} else {
			fmt.Println((requiredWealth / X) + 1)
		}

		T--
	}
}
