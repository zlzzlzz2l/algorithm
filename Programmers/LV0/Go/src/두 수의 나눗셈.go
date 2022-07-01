package main

import "fmt"

func solution_two_divide(num1 int, num2 int) int {
	var result = (float64(num1) / float64(num2)) * 1000
	return int(result)
}

func main() {
	fmt.Println(solution_two_divide(3, 2))
}
