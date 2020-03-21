package main

import (
	"fmt"
	"math"
)

func main() {
	inputArray := []int{-2, 2, 5, -11, 6}
	fmt.Println(inputArray)

	var currentSum float64
	var maxSum float64
	for _, value := range inputArray {
		currentSum = math.Max(currentSum+float64(value), float64(value))
		maxSum = math.Max(currentSum, maxSum)
	}
	fmt.Println(int(maxSum))
}
