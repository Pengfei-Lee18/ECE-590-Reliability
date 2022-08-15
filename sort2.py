def InsertionSort(listToSort):
    for i in range(len(listToSort)):
        k = i
        while(k>2 and listToSort[k]<listToSort[k-1]): #k>0
            tem = listToSort[k]
            listToSort[k] = listToSort[k-1]
            listToSort[k-1] = tem
            k-=1
    return listToSort

    