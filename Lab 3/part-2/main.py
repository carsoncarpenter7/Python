#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-09-26
# carson.carpenter7@csu.fullerton.edu
#


from cartesian import *

def main():
  a = Cartesian2D(2.3, 3.4)
  b = Cartesian2D(4.5, 1.8)
  c = Cartesian2D(8.1, 0.3)
  print("The distance from a to b is {}".format(a.distanceTo(b)))
  print("The distance from b to c is {}".format(b.distanceTo(c)))
  d = a + b
  print("a + b = ({},{})".format(d.x, d.y))
  d = c - b
  print("c - b = ({}, {})".format(d.x, d.y))
  print("The length of a is {}".format(a.length()))
  print("The length of b is {}".format(b.length()))
  print("The length of c is {}".format(c.length()))
  # the normalize method returns a unit length vector
  unita = a.normalize()
  unitb = b.normalize()
  unitc = c.normalize()
  print("The length of unit a is {}".format(unita.length()))
  print("The length of unit b is {}".format(unitb.length()))
  print("The length of unit c is {}".format(unitc.length()))
  if a == b:
    print('Somehow a is equal to b?')
  else:
    print('a is not equal to b')
  s = 4
  d = unita * s
  print(d)
  print("The length of d is {}".format(d.length()))
  e = s * unitb
  f = dot(a, b)
  g = dot(unita, unitb)
  h = dot(d, e)
  print("dot(a, b) = {}".format(f))
  print("dot(unita, unitb = {}".format(g))
  print("dot(d, e) = {}".format(h))

if __name__ == "__main__":
  main()
