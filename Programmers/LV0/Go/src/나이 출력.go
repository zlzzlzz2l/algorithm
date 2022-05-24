package main

import "fmt"

func solution_age(age int) int {
	return 2022 - age + 1
}

func main() {
	fmt.Println(solution_age(20))
}
