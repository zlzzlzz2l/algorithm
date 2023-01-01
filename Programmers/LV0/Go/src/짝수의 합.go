package main

import "fmt"

func solution_120831(n int) int {
	var result int = 0

	for i := 0; i < n+1; i++ {
		if i%2 == 0 {
			result += i
		}
	}
	return result
}

func main() {
	fmt.Println(solution_120831(10))
}
