package main

// Function c2 calculates the sum of all even fibonnaci numbers below four
// million.
func c2() int {
	sum := 0
	a := 1
	b := 1
	c := 2
	// This makes use of the fact that only every third number is divisible by two.
	for c < 4000000 {
		sum += c
		a = b + c
		b = c + a
		c = a + b
	}
	return sum
}
