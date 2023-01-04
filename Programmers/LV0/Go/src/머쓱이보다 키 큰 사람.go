package main

import "fmt"

func solution_120585(array []int, height int) int {
	var result int = 0

	for i := 0; i < len(array); i++ {
		if array[i] > height {
			result += 1
		}
	}

	return result
}

func main() {
	var array = []int{149, 180, 192, 170}
	var height int = 167

	fmt.Println(solution_120585(array, height))
}
