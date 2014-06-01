package main

// Function c6 finds the difference between the square of the sum of the first
// 100 natural numbers and the sum of the squares of those numbers.
func c6() int {
	sum := 0
	squareSum := 0
	for i := 1; i <= 100; i++ {
		sum += i
		squareSum += (i * i)
	}
	return (sum * sum) - squareSum
}
