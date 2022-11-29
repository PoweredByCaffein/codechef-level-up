package main

import "fmt"

func main() {
	var T int
	fmt.Scanf("%d", &T)

	for T > 0 {
		var w1, w2, x1, x2, M int
		fmt.Scanf("%d %d %d %d %d", &w1, &w2, &x1, &x2, &M)
		lowerRange := w1 + (x1 * M)
		upperRange := w1 + (x2 * M)

		if lowerRange <= w2 && w2 <= upperRange {
			fmt.Println(1)
		} else {
			fmt.Println(0)
		}

		T--
	}
}
