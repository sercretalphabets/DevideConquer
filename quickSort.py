__author__ = 'maryam esmaeili'

#Quick sort is typically faster than merge sort when the data is stored in memory.
#However, when the data set is huge and is stored on external devices such as a hard drive,
#merge sort is the clear winner in terms of speed.
#It minimizes the expensive reads of the external drive and also lends itself well to parallel computing.


from random import randint

import random

def qsort(qslist):

    if len(qslist) < 2:
        return qslist

    pivot = random.choice(qslist)
    small = [x for x in qslist if x < pivot]
    equal = [x for x in qslist if x == pivot]
    big = [x for x in qslist if x > pivot]

    return qsort(small) + equal + qsort(big)



def main():
    b = [0,3,4,5,6,12,2,1,7]
    print qsort(b)



if __name__ == "__main__":
    main()