package main

import "fmt"

func solution_120817(numbers []int) float64 {
	var number_sum int = 0

	for i := 0; i < len(numbers); i++ {
		number_sum += numbers[i]
	}

	var result float64 = float64(number_sum) / float64(len(numbers))

	return result
}

func main() {
	var numbers = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println(solution_120817(numbers))
}
