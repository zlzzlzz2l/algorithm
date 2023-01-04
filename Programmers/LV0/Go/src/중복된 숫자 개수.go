package main

import "fmt"

func solution_120583(array []int, n int) int {
	var result int = 0

	for i := 0; i < len(array); i++ {
		if array[i] == n {
			result += 1
		}
	}

	return result
}

func main() {

	var array = []int{1, 1, 2, 3, 4, 5}
	var n int = 1

	fmt.Println(solution_120583(array, n))
}