#!/usr/bin/env python3

import copy


import time
import random
import matplotlib.pyplot as plt

DEBUG = False

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

    @staticmethod
    def algo_insertion(l):
        iter_count = 0
        for i in range(1, len(l)):
            curr = l[i]
            j = i - 1
            # go to the left until find larger element
            while j >= 0 and l[j] > curr:
                iter_count+=1
                l[j+1] = l[j]
                j-=1
            # swap current value and minimum from the left
            l[j+1] = curr
        return l, iter_count

    @staticmethod
    def algo_bubble(l):
        iter_count = 0
        for i in range(0, len(l)):
            for j in range(len(l) - 1, i, -1):
                iter_count+=1
                # swap adjacent elements if left is larger
                if l[j-1] > l[j]:
                    tmp = l[j-1]
                    l[j-1] = l[j]
                    l[j] = tmp
        return l, iter_count

    @staticmethod
    def algo_shaker(l):
        iter_count = 0
        ileft = 0
        iright = len(l) - 1
        while ileft < iright:
            for j in range(iright, ileft, -1):
                iter_count+=1
                if l[j-1] > l[j]:
                    tmp = l[j-1]
                    l[j-1] = l[j]
                    l[j] = tmp
            iright-=1
            for j in range(ileft + 1, iright):
                iter_count+=1
                if l[j] > l[j+1]:
                    tmp = l[j]
                    l[j] = l[j+1]
                    l[j+1] = tmp
            ileft+=1
        return l, iter_count

    @staticmethod
    def algo_shell(l):
        iter_count = 0
        for d in [23, 10, 4, 1]:
            for i in range(d, len(l), d):
                curr = l[i]
                j = i - d
                while j >= 0 and l[j] > curr:
                    iter_count+=1
                    l[j+d] = l[j]
                    j-=d
                l[j+d] = curr
        return l, iter_count

    @staticmethod
    def algo_python_timsort(l):
        iter_count = 0
        l.sort()
        return l, iter_count


class Benchmark:
    def __init__(self, N0=1, N=10):
        self.dimensions = [n for n in range(N0, N+1)]

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
            l = [
                random.randrange(10*n) for x in range(n)
            ]
            for algorithm in self.algorithms:

                # execute certain algorithm
                start_time = time.time()
                res = getattr(Sort, algorithm)(copy.copy(l))
                execution_time = time.time() - start_time

                # save algorithm's benchmark results
                self.algorithm_results[algorithm]['execution_time'].append(execution_time)
                self.algorithm_results[algorithm]['iteration_count'].append(res[1])

                print(f'{algorithm:<30}N={n:<8}time={execution_time}')

    def plot(self):
        for param in self.algorithm_result_object:
            # if param == 'iteration_count':
                # continue
            for algorithm in self.algorithm_results:
                plt.plot(self.dimensions, self.algorithm_results[algorithm][param], label = algorithm)
            plt.xlabel('task_dimension')
            plt.ylabel(param)
            plt.grid(True)
            plt.legend()
            plt.show()


def main():
    if DEBUG:
        l = [random.randrange(256) for i in range(10)]
        print(l)
        # print(Sort.algo_...(l))
    else:
        benchmark = Benchmark(N=50)
        benchmark.execute()
        benchmark.plot()


if __name__ == '__main__':
    main()
