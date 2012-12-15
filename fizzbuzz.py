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

# This program generates a FizzBuzz sequence (by default 1 - 100, but configurable)

import argparse

argumentParser = argparse.ArgumentParser(description="Generate a FizzBuzz sequence.")
argumentParser.add_argument("-s", "--start", type=int, default=1,
                help="Specify the start number for the sequence.")
argumentParser.add_argument("-f", "--finish", type=int, default=100,
                help="Specify the finish number for the sequence.")
arguments = argumentParser.parse_args()

def getFizzBuzz(number):
    if number % 3 is 0 and number % 5 is 0:
        print("FizzBuzz")
    elif number % 3 is 0:
        print("Fizz")
    elif number % 5 is 0:
        print("Buzz")
    else:
        print(number)

for i in range(arguments.start,arguments.finish+1):
    getFizzBuzz(i)
