# Divide and Conquer

def merge_sort(unsorted):
    if len(unsorted) >= 2:
        mid = len(unsorted) // 2
        left = unsorted[:mid]
        right = unsorted[mid:]

        merge_sort(left)
        merge_sort(right)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted[k] = left[i]
                i += 1
            else:
                unsorted[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            unsorted[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            unsorted[k] = right[j]
            j = j+1
            k = k+1
    return unsorted

def main():
    print(merge_sort([11,2,5,3,4,6,1]))

if __name__ == '__main__':
    main()