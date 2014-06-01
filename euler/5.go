package main

// Function c5 finds the smallest integer that is cleanly divisible by all
// integers from one to twenty.
func c5() int {
	// We can skip the 19 numbers not divisible by 20 each time.
	for i := 20; ; i += 20 {
		if isDivisible(i, 20) {
			return i
		}
	}
}

// Function isDivisible tests in to see if it is divisible by all of the numbers
// from one to amount.
func isDivisible(in int, amount int) bool {
	for i := 1; i <= amount; i++ {
		if in%i != 0 {
			return false
		}
	}
	return true
}
