__author__ = 'm.esmaeili'


import random

class KthStatistics():


    def __init__(self, array, k):
        self.array=array
        self.k=k

    def pivot(self, start,end):
        pivotind=random.randint(start, end)
        pivot=self.array[pivotind]
        self.array[pivotind],self.array[end]=self.array[end],self.array[pivotind]
        pivotind = end;
        ppos=start-1
        for j in range(start,end):
            if self.array[j]<=pivot:
                ppos+=1
                self.array[ppos],self.array[j]=self.array[j],self.array[ppos]
        ppos+=1
        self.array[pivotind],self.array[ppos]=self.array[ppos],self.array[pivotind]

        return ppos

    def random_selection(self, start,end):
        if start==end:
            return self.array[start]
        if self.k==0:
            return -1
        if start<end:
            pposition=self.pivot(start,end)
            i=pposition-start+1
            if i==self.k:
                return self.array[pposition]
            if i>self.k:
                return self.random_selection(start,pposition-1)
            else:
                self.k=self.k-i
                return self.random_selection(pposition+1,end)


'''
nothing in the above outline is terribly deep; its just a straighforward divide-and-conquer approach to solving
the selection problem. The clever part of the algorithm is the choice of pivot element.
It is not hard to see that, much like quicksort, if we naively choose the pivot element, this algorithm has a worst
case performance of O(n2). Continuing the parallel with quicksort,  if we choose a random pivot, we get expected linear
time performance, but still a worst case scenario of quadratic time.

'''


def main():
    b = [0,3,4,5,6,12,2,1,7]

    mis=KthStatistics(b,3)
    end=len(b)-1
    print (mis.random_selection(0,end))
    b=[9,5,7,1,10,2,3]
    mis=KthStatistics(b,5)
    end=len(b)-1
    print (mis.random_selection(0,end))



if __name__ == "__main__":
    main()