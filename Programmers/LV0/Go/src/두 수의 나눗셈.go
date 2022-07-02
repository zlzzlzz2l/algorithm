package main

import "fmt"

func solution_두수의나눗셈(num1 int, num2 int) int {
	var result = (float64(num1) / float64(num2)) * 1000
	return int(result)
}

func main() {
	fmt.Println(solution_두수의나눗셈(3, 2))
}
