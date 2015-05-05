__author__ = 'maryam esmaeili'


#For Merge sort worst case is O(n*log(n)), for Quick sort: O(n2). For other cases (avg, best) both have O(n*log(n)).
#  However Quick sort is space constant where Merge sort depends on the structure you're sorting.




def mergesort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    return merge(left, right)

def merge(left, right):
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + merge(left[1:], right)
        return [right[0]] + merge(left, right[1:])


def main():
    b = [0,3,4,5,6,12,2,1,7]
    print mergesort(b)





if __name__ == "__main__":
    main()







