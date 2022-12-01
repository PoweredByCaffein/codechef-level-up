package main

import "fmt"

func main() {

	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		var a, b, c, d, K int
		fmt.Scanf("%d %d %d %d %d", &a, &b, &c, &d, &K)
		x := c - a
		y := d - b
		if x < 0 {
			x *= -1
		}

		if y < 0 {
			y *= -1
		}

		distance := x + y 

		if K < distance || (K-distance)%2 != 0 {
			fmt.Println("NO")
		} else {
			fmt.Println("YES")
		}


		T--
	}

}
