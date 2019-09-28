from matplotlib import pyplot as plt
def  selectionSort(array):

    def indexOfMinimum(array, startIndex):
        minIndex = startIndex
        for i, num in enumerate(array[startIndex:], startIndex):
            if num<array[minIndex]:
                minIndex = i
        return minIndex

    for i,_ in enumerate(array):
        index = indexOfMinimum(array, i)
        array[i], array[index] = array[index], array[i]

array = [22, 11, 99, 88, 9, 7, 42]
print(array)
plt.bar(range(len(array)),array)
plt.show()
selectionSort(array)
plt.bar(range(len(array)),array)
plt.show()
print(array)
assert array == [7, 9, 11, 22, 42, 88, 99]