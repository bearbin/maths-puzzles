package main

// Function c3 returns the largest prime factor of 600851475143.
func c3() int64 {
	var largestFactor int64 = 1
	var x int64
	var w int64 = 600851475143
	for x = 2; w > 1; x++ {
		for w%x == 0 {
			largestFactor = x
			w /= x
		}
		if x^2 >= w {
			if w > 1 {
				largestFactor = w
			}
			break
		}
	}
	return largestFactor
}
