def  selectionSort(array):

    def swap(array, fristIndex, secondIndex):
        temp = array[fristIndex]
        array[fristIndex] = array[secondIndex]
        array[secondIndex] = temp

    def indexOfMinimum(array, startIndex):
        minIndex = startIndex
        for i in range(startIndex, len(array)):
            if array[i]<array[minIndex]:
                minIndex = i
        return minIndex

    for i in range(len(array)):
        index = indexOfMinimum(array, i)
        swap(array, i, index)

array = [22, 11, 99, 88, 9, 7, 42]
selectionSort(array)
assert array == [7, 9, 11, 22, 42, 88, 99]