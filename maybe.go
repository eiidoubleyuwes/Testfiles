package main

import (
	"fmt"
)

func add(a, b int) int {
	return a + b
}

func subtract(a, b int) int {
	return a - b
}

func multiply(a, b int) int {
	return a * b
}

func divide(a, b int) float64 {
	return float64(a) / float64(b)
}

func main() {
	fmt.Println("Calculator")

	// Perform some calculations
	num1 := 10
	num2 := 5

	sum := add(num1, num2)
	fmt.Printf("Sum: %d\n", sum)

	diff := subtract(num1, num2)
	fmt.Printf("Difference: %d\n", diff)

	product := multiply(num1, num2)
	fmt.Printf("Product: %d\n", product)

	quotient := divide(num1, num2)
	fmt.Printf("Quotient: %.2f\n", quotient)
}
