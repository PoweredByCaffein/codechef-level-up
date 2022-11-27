package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)

	for T > 0 {
		var N, S int
		fmt.Scanf("%d %d", &N, &S)

		if S == N {
			fmt.Println(N)
		} else if S < N {
			fmt.Println(S)
		} else {
			fmt.Println(N - (S - N))
		}
		
		T--
	}
}
