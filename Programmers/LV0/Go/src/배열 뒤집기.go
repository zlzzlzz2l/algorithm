package main

import (
	"fmt"
)

func solution_120821(num_list []int) []int {
	length := len(num_list)
	result := []int{}
	for i := length - 1; i > -1; i-- {
		result = append(result, num_list[i])
	}
	return result
}

func main() {
	num_list := []int{1, 2, 3, 4, 5}

	fmt.Println(solution_120821(num_list))
}
