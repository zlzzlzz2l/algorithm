package main

import "fmt"

func solution_120854(strlist []string) []int {
	result := []int{}

	for _, s := range strlist {
		result = append(result, len(s))
	}

	return result
}

func main() {
	strlist := []string{"We", "are", "the", "world!"}

	fmt.Println(solution_120854(strlist))
}
