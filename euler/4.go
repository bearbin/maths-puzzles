package main

// Function c4 finds the largest palindromic number that is the multiple of 2 3-
// digit numbers.
func c4() int {
	largestPalindrome := 0
	for i := 0; i <= 999; i++ {
		for j := 0; j <= 999; j++ {
			num := i * j
			if num > largestPalindrome && isPalin(num) {
				largestPalindrome = num
			}
		}
	}
	return largestPalindrome
}

func isPalin(in int) bool {
	original := in
	rev := 0
	for in > 0 {
		rev = (rev * 10) + (in % 10)
		in /= 10
	}
	return original == rev
}
