package main

// Function c1 finds the sum of the natural numbers below 1000 that are divisible
// by three or five.
func c1() int {
	total := 0
	for i := 1; i < 1000; i++ {
		if (i%3 == 0) || (i%5 == 0) {
			total += i
		}
	}
	return total
}
