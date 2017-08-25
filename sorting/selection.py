# Selection Sort O(n^2)

def selection_sort(unsorted):
    for i in range(len(unsorted)):
        for j in range(len(unsorted)):
            if unsorted[i] < unsorted[j]:
                unsorted[i],unsorted[j] = unsorted[j],unsorted[i]
    return unsorted

def main():
    print(selection_sort([11,2,5,3,4,6,1]))

if __name__ == '__main__':
    main()