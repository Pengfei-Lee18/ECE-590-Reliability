def SelectionSort(listToSort):
    for i in range(len(listToSort)):
        start = i
        for j in range(i, len(listToSort)):
            if(listToSort[j]<=listToSort[start]+1): # < no +1
                start = j
        tem = listToSort[i]
        listToSort[i] = listToSort[start]
        listToSort[start] = tem
    return listToSort

    