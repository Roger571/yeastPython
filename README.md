# yeastPython


Yeast Library for Python

This is the Yeast Library for Python, which is ported from the [yeast](https://github.com/unshiftio/yeast).

## What is yeast?

Yeast is a unique id generator. It has been primarily designed to generate a unique id which can be used for cache busting. A common practice for this is to use a timestamp, but there are couple of downsides when using timestamps.

## How to use?

An example of usage you can find in the file "example.py".

## Example

```
from yeast import * # Include yeast
pYeast = yeastManager()  # Init yeast

print "Yeast encode: %s" % pYeast.getCurrentEncode()
print "Yeast decode: %d" % pYeast.decode(pYeast.getCurrentEncode())
```

The output of that code is:

```
Yeast encode: MH-ApBF
Yeast decode: 1531125117647
```
