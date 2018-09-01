**THIS IS IN NO WAY SECURE!!!**

# LittleRSA
I was reading about RSA encryption and decided to write a small python script
that implements the basic mathematical principals used in the process. This is
purely meant to be a proof of concept! The primes in play are (and must be due
to variable size) waaayyy too small, and the process is far from efficient.
BUT, if you just want to see what is going on from a rough mathematical
perspective, hopefully this will offer some insight.

## Links/References
In this READEM, I will be summarizing concepts that I learned from the
following links, so if you would rather hear it from the source, please be my
guest!
* [RSA - Wiki](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

## Basic Concept
The basic concept of RSA encryption is pretty straight forward. You want a
public and private key pair. The public key is shared freely, and is used to
encrypt data. The private key is secret, and can be used decrypt messages/values
generated with the public key. Lets call call these keys `e` and `d` for encrypt
and decrypt respectively.

RSA relies on a key pair `e` and `d` such that:
<code> encValue =  value<sup>e</sup> mod n </code>
<code> value    =  encValue<sup>e</sup> mod n </code>

That is, to encrypt a value, `value`, you would raise it to the power of the
public key, `e`, and take the remainder after dividing by `n` (we will get to
what `n` is in a minute).

To get back the original value, we would raise the encrypted value, `encVal`,
to the power of `d`, and take the remainder after dividing by again by `n`.

## Getting `e`, `d`, and `n`
So the basic concept is fine, but how in the absolute hell do you find values
that work together in this magical way? Lets jump into the math, but before we
do, I want to offer this disclaimer: I am an engineer and NOT a mathematician.
While I understand the math in play, I am almost certainly missing the finer
points of the underlying number theory that explain *why* these numbers work
together the way they do. That being said, lets jump in!

The first thing that we need, are two primes. Lets call them `p` and `q`. From
these primes, we will derive `e`, `d`, and `n` starting with `n`.

### Finding `n`
Fortunately, this is an easy one. `n` is simply the product of our two primes:
`n = p * q`

### Finding `e`
Here is where things start to pickup. We need to find the [Carmichael Function](https://en.wikipedia.org/wiki/Carmichael_function)
output for `n`. Please read the linked wiki for a proper definition. The basic
concept comes down to this, the Carmichael function output for `n`, `cmf`, is 
the smallest integer such that, you could take any of the integers between `1`
and `n` that are [coprime](https://en.wikipedia.org/wiki/Coprime_integers) to
`n`, and raise them to the power of `cmf` and then get a remainder of `1` if
you divide the result by `n`.

Okay, that probably sounds like jiberish. Lets look at it more mathematically.
For any integer `a` between `1` and `n` that is also coprime to `n`, find the
smallest integer, `cmf`, that makes the following true for all values of `a`:
<code> a<sup>cmf</sup> mod n == 1 </code>

Okay.... so how do we calculate that?!?! For us, we are lucky, given that n is
the product of two primes, `p` and `q`, we have a shortcut. The Carmichael
function output, `cmf`, of `n` is the least common multiple of `p-1` and `q-1`.
Yep, all of that talking to tell you to just find `lcm(p-1, q-1)`. But hopefully
you got something out of the journey. 

ENOUGH! Tell me what `e` is!!! Alright alright, lets get back on topic. `e`
needs to be any random number between `1` and `cmf` that is also coprime to `cmf`.

### Finding `d`
Home stretch! `d` is the [modular multiplicative inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)
of `e`. In other words, solve for `d` such that `(d * e) mod cmf == 1`

Now that you have `e`, `d`, and `n`, we can perform basic RSA encryption!

## The script
The script in this repo, `littleRSA.py`, is a simple implementation of the
above concepts. It takes two primes and a `value` as input. The `value` will
be encrypted and decrypted using values of `e`, `d`, and `n` computed using the
provided primes.

The output will look something like this:
``` bash
~/code $ ./littleRSA.py 37 41 45
LittleRSA:
    p = 37
    q = 41
    n = 1517
    Carmichael Function = cmf = 360
    e such that 1 < e < cmf and e is coprime to cmf = 119
    d such that (d * e) % cmf is one = 239

    encVal = (value ^ e) % n = 236
    decVal = (value ^ d) % n = 45
```

That's all I have! Thanks for reading.
