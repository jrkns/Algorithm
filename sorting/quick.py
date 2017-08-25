# Quick Sort O(n^2)

def partition(list, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if list[i] <= list[begin]:
            pivot += 1
            list[i], list[pivot] = list[pivot], list[i]
    list[pivot], list[begin] = list[begin], list[pivot]
    return pivot

def quick_sort(unsorted, begin, end):
    if begin >= end:
        return
    pivot = partition(unsorted, begin, end)
    quick_sort(unsorted, begin, pivot-1)
    quick_sort(unsorted, pivot+1, end)
    return unsorted

def main():
    unsorted = [11,2,5,3,4,6,1]
    print(quick_sort(unsorted, 0,len(unsorted)-1))

if __name__ == '__main__':
    main()