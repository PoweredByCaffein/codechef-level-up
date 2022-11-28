package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		var N, A, B, C int
		fmt.Scanf("%d %d %d %d", &N, &A, &B, &C)

		if B >= N && A+C >= N {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}

		T--
	}
}
