package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		var N, X int
		fmt.Scanf("%d %d", &N, &X)

		var max int
		for N > 0 {
			var S, R int
			fmt.Scanf("%d %d", &S, &R)
			if S <= X {
				if R > max {
					max = R
				}
			}
			N--
		}

		fmt.Println(max)

		T--
	}
}
