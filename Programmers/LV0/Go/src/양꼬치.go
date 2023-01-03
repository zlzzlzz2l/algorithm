package main

import "fmt"

func solution_120830(n int, k int) int {
	if n >= 10 {
		var beverage int = k - (n / 10)
		return 12000*n + beverage*2000
	} else {
		return 12000*n + k*2000
	}
}

func main() {
	var n int = 64
	var k int = 6

	fmt.Println(solution_120830(n, k))
}
