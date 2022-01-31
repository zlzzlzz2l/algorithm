package main

import "fmt"

func solution_120829(angle int) int {
	if angle > 0 && angle < 90 {
		return 1
	} else if angle == 90 {
		return 2
	} else if angle > 90 && angle < 180 {
		return 3
	} else {
		return 4
	}
}

func main() {
	fmt.Println(solution_120829(30))
}
