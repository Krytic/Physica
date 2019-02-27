import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

class Dataset:
	def __init__(self, x, y):
		self.__size = len(x)
		if self.__size != len(y):
			raise ValueError('x and y must have the same dimension')

		self.__x = x
		self.__y = y
		self.__xlabel = self.__ylabel = ""

	def __iter__(self):
		self.__n = 0
		return self

	def __next__(self):
		if self.__n < self.__size:
			curr = (self.__x[self.__n], self.__y[self.__n])
			self.__n += 1
			return curr
		else:
			raise StopIteration

	def label(self, xlabel, ylabel):
		self.__xlabel = xlabel
		self.__ylabel = ylabel

	def fetch_data(self):
		x = y = ux = uy = []
		for x_i in self.__x:
			if type(x_i) == ufloat:
				x.append(x_i.n)
				ux.append(x_i.s)
			else:
				x.append(x_i)
				ux.append(0)
		for y_i in self.__y:
			if type(y_i) == ufloat:
				y.append(y_i.n)
				uy.append(y_i.s)
			else:
				y.append(y_i)
				uy.append(0)

		return x, y, ux, uy

	def plot(self):
		plt.figure()
		
		plt.xlabel(self.__xlabel)
		plt.ylabel(self.__ylabel)

		x, y, ux, uy = self.fetch_data()
		plt.errorbar(x, y, xerr=ux, yerr=uy)