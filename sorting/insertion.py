# Insertion Sort O(n^2)

def insertion_sort(unsorted):
    for i in range(1,len(unsorted)):
        now = unsorted[i]
        j = i
        while j > 0 and unsorted[j-1] > now:
            unsorted[j] = unsorted[j - 1]
            j -= 1
        unsorted[j] = now
    return unsorted

def main():
    print(insertion_sort([11,2,5,3,4,6,1]))

if __name__ == '__main__':
    main()