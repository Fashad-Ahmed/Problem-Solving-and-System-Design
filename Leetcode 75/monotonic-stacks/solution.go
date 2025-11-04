package main

import "fmt"

func dailyTemperatures(temperatures []int) []int {
	n := len(temperatures)
	answer := make([]int, n)
	stack := []int{} // Stack to store indices

	// Traverse from right to left
	for i := n - 1; i >= 0; i-- {
		// Pop elements from the stack while current temperature is >= top of stack temperature
        for len(stack) > 0 && temperatures[i] >= temperatures[stack[len(stack)-1]] {
			stack = stack[:len(stack)-1]
		}

		// If stack is not empty, top element is the next warmer day
		if len(stack) > 0 {
			answer[i] = stack[len(stack)-1] - i
		}

		// Push current index onto stack
		stack = append(stack, i)
	}

	return answer
}

func main() {
	temperatures := []int{73, 74, 75, 71, 69, 72, 76, 73}
	result := dailyTemperatures(temperatures)
	fmt.Println(result) // Output: [1 1 4 2 1 1 0 0]
}
