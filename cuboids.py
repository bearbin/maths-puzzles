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

import argparse

argumentParser = argparse.ArgumentParser(description="Generate cuboids with set surface areas.")
argumentParser.add_argument("-s", "--start", type=int, default=1,
                            help="Specify the start number for values to be tried.")
argumentParser.add_argument("-f", "--finish", type=int, default=100,
                            help="Specify the finish number for values to be tried.")
argumentParser.add_argument("-a", "--area", type=int, default=100,
                            help="Specify the area of the cuboid to match.")
arguments = argumentParser.parse_args()

def check_cuboid(x,y,z):
    if 2*(x*y+x*z+y*z) is arguments.area:
        print(str(x)+", "+str(y)+", "+str(z))

length = range(arguments.start, arguments.finish+1)

for x in length:
    if x is 0: continue
    for y in length:
        if y is 0: continue
        for z in length:
            if z is 0: continue
            check_cuboid(x,y,z)

