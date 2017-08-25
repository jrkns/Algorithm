# Bubble Sort O(n^2)

def bubble_sort(unsorted):
    for i in range(len(unsorted)):
        for j in range(len(unsorted)-1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j],unsorted[j+1] = unsorted[j+1],unsorted[j]
    return unsorted

def main():
    print(bubble_sort([11,2,5,3,4,6,1]))

if __name__ == '__main__':
    main()