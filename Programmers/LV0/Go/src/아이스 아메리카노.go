package main

import "fmt"

func solution_120819(money int) []int {
	result := []int{}
	result = append(result, money/5500)
	result = append(result, money%5500)
	return result
}

func main() {
	var money int = 5500
	fmt.Println(solution_120819(money))
}
