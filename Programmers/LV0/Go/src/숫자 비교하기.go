package main

import "fmt"

func solution_숫자비교하기(num1 int, num2 int) int {
	if num1 != num2 {
		return -1
	}
	return 1
}

func main() {
	fmt.Println(solution_숫자비교하기(12, 3))
}
