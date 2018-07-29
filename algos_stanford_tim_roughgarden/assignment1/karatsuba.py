#!/usr/local/bin/python3
'''
A simple python template
'''
import os
import sys
import argparse
import math
''' In this programming assignment you will implement one or more of the
integer multiplication algorithms described in lecture.

To get the most out of this assignment, your program should restrict itself to
multiplying only pairs of single-digit numbers. You can implement the
grade-school algorithm if you want, but to get the most out of the assignment
you'll want to implement recursive integer multiplication and/or Karatsuba's
algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627

[TIP: before submitting, first test the correctness of your program on some
small test cases of your own devising. Then post your best test cases to the
discussion forums to help your fellow students!]

[Food for thought: the number of digits in each input number is a power of 2.
Does this make your life easier? Does it depend on which algorithm you're
implementing?]

The numeric answer should be typed in the space below. So if your answer is
1198233847, then just type 1198233847 in the space provided without any space /
commas / any other punctuation marks.

(We do not require you to submit your code, so feel free to use any programming
language you want --- just type the final numeric answer in the following
space.)

'''

class karatsuba(object):
    def __init__(self,a=1,b=1):
        self.a=a
        self.b=b
        self.traditional_ab=1
        self.karatsuba_ab=1
        self.printm(a)
        self.printm(b)

    def t_multiply(self):
        self.traditional_ab=self.a*self.b
        print ("multiply ",self.a*self.b)

    
    def k_multiply(self):
        self.karatsuba_ab = self.k_core_multiply(self.a, self.b)
        print ("karatsuba mult   :",self.karatsuba_ab)
        print ("traditional mult :",self.t_multiply())
        if (self.karatsuba_ab == self.traditional_ab):
            print ("You passed ! ",self.a,self.b)
        else:
            print ("You failed ! ",self.a,self.b)

    def k_core_multiply(self, x, y):
        if (x <= 0 or y <= 0):
            return 0
        n = int(math.log10(x))+1
        m = int(math.log10(y))+1
        if (m == 1 or n == 1):
            return x*y
        #n = 2*(int(n/2) + n%2)
        #m = 2*(int(m/2) + m%2)
        if (n >m):
            m=n
        else:
            n=m
        tenPowerN = 10**(n - n%2)
        tenPowerNBy2 = 10**(int(n/2))
        tenPowerM = 10**(m - m%2)
        tenPowerMBy2 = 10**(int(m/2))
        
        b = int (x % (tenPowerNBy2))
        d = int (y % (tenPowerMBy2))
        # Following weirdity is don to avoid two pitfalls
        # python3 does not round off numbers correctly for ~32 digits
        # // is used tp get an integer result
        a = int ((x-b) // (tenPowerNBy2))
        c = int ((y-d) // (tenPowerMBy2))
        ac = self.k_core_multiply(a, c) 
        bd = self.k_core_multiply(b, d)
        aPbMcPd = self.k_core_multiply(a + b, c + d)
        if (n > m ):
          product = ac*(tenPowerN) + (aPbMcPd - ac - bd)*(tenPowerNBy2) + bd
        else:
          product = ac*(tenPowerM) + (aPbMcPd - ac - bd)*(tenPowerMBy2) + bd
        return product

    def printm(self, a):
        print (a, type(a))


def assignment1():
    myk2 = karatsuba(2884197169399375105820974944592,62497757247093699959574966967627)
    myk2.k_multiply()
    myk2 = karatsuba(2884197169399375105820974944592,10)
    myk2.k_multiply()
    myk2 = karatsuba(10,62497757247093699959574966967627)
    myk2.k_multiply()
    myk2 = karatsuba(62497757247093699959574966967627,1000)
    myk2.k_multiply()
    myk2 = karatsuba(1234,456)
    myk2.k_multiply()
    myk2 = karatsuba(6249775724709369995957496696762,1000)
    myk2.k_multiply()
    myk2 = karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                    2718281828459045235360287471352662497757247093699959574966967627)
    myk2.k_multiply()


def main(args):
    parser = argparse.ArgumentParser(description="Generic template")
    parser.add_argument("-v","--verbose",
                        help="Increase verbosity of the script",
                        action="store_true")
    args = parser.parse_args()
    assignment1()
    print ("Template script works fine")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


def main(args):
    parser = argparse.ArgumentParser(description="Generic template")
    parser.add_argument("-v","--verbose",
                        help="Increase verbosity of the script",
                        action="store_true")
    args = parser.parse_args()
    assignment1()
    print ("Template script works fine")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
