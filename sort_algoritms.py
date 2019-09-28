from matplotlib import pyplot as plt
def  selectionSort(array):

    def swap(array, first_index, second_index):
        array[first_index], array[second_index] = array[second_index], array[first_index]

    def indexOfMinimum(array, startIndex):
        minIndex = startIndex
        for i, num in enumerate(array[startIndex:], startIndex):
            if num<array[minIndex]:
                minIndex = i
        return minIndex

    for i in range(len(array)):
        index = indexOfMinimum(array, i)
        swap(array, i, index)

array = [22, 11, 99, 88, 9, 7, 42]
print(array)
plt.bar(range(len(array)),array)
plt.show()
selectionSort(array)
plt.bar(range(len(array)),array)
plt.show()
print(array)
assert array == [7, 9, 11, 22, 42, 88, 99]