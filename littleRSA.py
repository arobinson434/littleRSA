#! /usr/bin/python

import random
import sys

def gcd(x, y):
    while y != 0:
        t = y
        y = x % y
        x = t
    return x

def lcm(x, y):
    return ( abs(x*y) / gcd(x,y))

def calc_e(cmf):
    e = random.randint(2,cmf)
    while e < cmf and gcd(e, cmf) != 1:
        e = random.randint(2,cmf)
    return e

def mod_mult_inv(e, cmf):
    d = 1
    while ((d*e) % cmf) != 1:
        d = d + 1
    return d

def main():
    if len(sys.argv) != 4:
        print "Invalid Arguments:"
        print "\tPlease provide: prime1 prime2 value"
        exit(1)

    p   = int(sys.argv[1])
    q   = int(sys.argv[2])
    v   = int(sys.argv[3])
    n   = p * q
    cmf = lcm(p-1, q-1)

    e   = calc_e(cmf)
    d   = mod_mult_inv(e, cmf)

    encVal = pow(v,e,n)
    decVal = pow(encVal,d,n)

    print "LittleRSA:"

    print "\tp = " + str(p)
    print "\tq = " + str(q)
    print "\tn = " + str(n)
    print "\tCarmichael Function = cmf = " + str(cmf)
    print "\te such that 1 < e < cmf and e is coprime to cmf = " + str(e)
    print "\td such that (d * e) % cmf is one = " + str(d)
    print ""
    print "\tencVal = (value ^ e) % n = " + str(encVal)

    if ( v >= n ):
        print "\n\tWell... This is kinda embarrassing."
        print "\tYour value is greater than n. Please choose a smaller value or larger primes."
        sys.exit(1)

    print "\tdecVal = (value ^ d) % n = " + str(decVal)

if __name__ == "__main__":
    main()
