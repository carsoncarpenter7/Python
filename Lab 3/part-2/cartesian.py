#!/usr/bin/env python3
#
# Carson Carpenter
# CPSC 223P-03
# 2020-09-26
# carson.carpenter7@csu.fullerton.edu
#
# class to define the cartesian points


from math import *

# returns the dot product of two vectors
def dot(self, otherPoint):
    return ((self.x * otherPoint.x) + (self.y * otherPoint.y))


class Cartesian2D:

	def __init__(self, x, y):
		""" parameters: x -> first point, y -> second point """
		self.x = x
		self.y = y


	def __add__(self, otherPoint):
		""" adds two vectors; returns the answer in a vector """
		x = self.x + otherPoint.x
		y = self.y + otherPoint.y
		return Cartesian2D(x, y)


	def __sub__(self, otherPoint):
		""" subtracts two vectors; returns the answer in a vector """
		x = self.x - otherPoint.x
		y = self.y - otherPoint.y
		return Cartesian2D(x, y)

	def __rmul__(self, s):
		""" Overloading the * operator """
		if isinstance(s, float) or isinstance(s, int):
			return Cartesian2D(self.x * s, self.y * s)
		else:
			raise TypeError('must be an int or float')

	# overloading
	def __mul__(self, scalar_mult):
		" multiplies a vector and a scalar value; returns the answer in a vector """
		x = self.x * scalar_mult
		y = self.y * scalar_mult
		return Cartesian2D(x, y)


	def length(self):
		""" returns the length of a vector """
		return sqrt((self.x ** 2) + (self.y ** 2))


	def distanceTo(self, otherPoint):
		""" returns the distance from one vector to another """
		return (self - otherPoint).length()


	def __str__(self):
		""" returns a string of the vectors"""
		return 'X: {self.x}, Y: {self.y}'.format(self = self)


	def normalize(self):
		""" returns a length vector (unit vector) """
		x = self.x / self.length()
		y = self.y / self.length()
		return Cartesian2D(x, y)
