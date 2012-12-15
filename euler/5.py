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

# This is puzzle #5 from projecteuler.net

d = 0

while 1:
    d += 1
    i = 20 * d
    if i % 1 != 0: continue
    if i % 2 != 0: continue
    if i % 3 != 0: continue
    if i % 4 != 0: continue
    if i % 5 != 0: continue
    if i % 6 != 0: continue
    if i % 7 != 0: continue
    if i % 8 != 0: continue
    if i % 9 != 0: continue
    if i % 10 != 0: continue
    if i % 11 != 0: continue
    if i % 12 != 0: continue
    if i % 13 != 0: continue
    if i % 14 != 0: continue
    if i % 15 != 0: continue
    if i % 16 != 0: continue
    if i % 17 != 0: continue
    if i % 18 != 0: continue
    if i % 19 != 0: continue
    print(i)
    break
