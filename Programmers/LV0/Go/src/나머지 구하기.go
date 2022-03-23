package main

import "fmt"

func solution_divide(num1 int, num2 int) int {
	return num1 % num2
}

func main() {
	fmt.Println(solution_divide(15, 3))
}
