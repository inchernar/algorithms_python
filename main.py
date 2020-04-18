#!/usr/bin/env python3

import copy
import time
import random
import matplotlib.pyplot as plt

class Sort:
	@staticmethod
	def algo_selection(l):
		iter_count = 0
		for i in range(len(l) - 1):
			# mark current index as index of min
			imin = i;

			# find min in the rest of list
			for j in range(i + 1, len(l)):
				iter_count += 1
				if(l[j] < l[imin]):
					imin = j;

			# swap current element and found min
			tmp = l[i]
			l[i] = l[imin]
			l[imin] = tmp
		return l, iter_count

class Benchmark():
	def __init__(self, N0=1, N=10):
		self.dimensions = [n for n in range(N0, N)]

		# collect all algorithms (static methods, named as 'algo_*') from Sort
		self.algorithms = []
		for property in dir(Sort):
			if property.startswith('algo_'):
				self.algorithms.append(property)

		self.algorithm_result_object = {
			'execution_time': [],
			'iteration_count': []
		}

		self.algorithm_results = {}
		for algorithm in self.algorithms:
			self.algorithm_results[algorithm] = copy.deepcopy(self.algorithm_result_object)

	def execute(self):
		for n in self.dimensions:
			l = [random.randrange(10*n) for x in range(n)]
			for algorithm in self.algorithms:

				# execute certain algorithm
				start_time = time.time()
				res = getattr(Sort, self.algorithms[0])(copy.copy(l))
				execution_time = time.time() - start_time

				# save algorithm's benchmark results
				self.algorithm_results[algorithm]['execution_time'].append(execution_time)
				self.algorithm_results[algorithm]['iteration_count'].append(res[1])

	def plot(self):
		for param in self.algorithm_result_object:
			for algorithm in self.algorithm_results:
				plt.plot(self.dimensions, self.algorithm_results[algorithm][param], label = algorithm)
			plt.xlabel('task_dimension')
			plt.ylabel(param)
			plt.grid(True)
			plt.legend()
			plt.show()

def main():
	benchmark = Benchmark()
	benchmark.execute()
	benchmark.plot()

if __name__ == '__main__':
	main()
