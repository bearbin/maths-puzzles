#!/usr/bin/env python3

# Copyright © 2012 Alexander Harkness
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software
#and associated documentation files (the “Software”), to deal in the Software without restriction,
#including without limitation the rights to use, copy, modify, merge, publish, distribute,
#sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or
#substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
#BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# This is puzzle #4 from projecteuler.net

def is_palindrome(num):
    if str(num)[::-1] == str(num):
        return True

palindromes = []

for x in range(100,1000):
    for y in range(100,1000):
        if is_palindrome(x*y):
            palindromes.append(x*y)


palindromes.sort()
print (palindromes[-1])
