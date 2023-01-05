package main

import "fmt"

func solution_120814(n int) int {
	if n%7 != 0 {
		return n/7 + 1
	} else {
		return n / 7
	}
}

func main() {
	var n int = 15

	fmt.Println(solution_120814(n))
}
