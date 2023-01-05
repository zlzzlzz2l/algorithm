package main

import "fmt"

func solution_120841(dot []int) int {
	if dot[0] > 0 && dot[1] > 0 {
		return 1
	} else if dot[0] < 0 && dot[1] > 0 {
		return 2
	} else if dot[0] < 0 && dot[1] < 0 {
		return 3
	} else {
		return 4
	}
}

func main() {
	dot := []int{2, 4}

	fmt.Println(solution_120841(dot))
}
