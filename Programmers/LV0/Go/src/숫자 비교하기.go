package main

import "fmt"

func solution_num(num1 int, num2 int) int {
	if num1 != num2 {
		return -1
	}
	return 1
}

func main() {
	fmt.Println(solution_num(12, 3))
}
