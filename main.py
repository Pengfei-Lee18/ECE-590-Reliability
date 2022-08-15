from sort1 import SelectionSort;
from sort2 import InsertionSort;

def acceptance_test(unsortedList, sortedList):
    temp = unsortedList.copy()
    temp.sort()
    return temp == sortedList

def runCode(list1):
    print("\n\n\nTest primary module\n")
    res1 = SelectionSort(list1)
    if acceptance_test(list1, res1):
        print("Primary module functions correctly\n")
    else:
        print("Primary module failed, try Alternate module\n")
        res2 = InsertionSort(list1)
        if acceptance_test(list1, res2):
            print("Alternate module functions correctly\n")
        else:
            raise Exception("All modeles failed!", list1)


if __name__ == "__main__":
    list1 = [2,3,5,3,56,7,2,654,34]
    list2 = [10,9,8,7,6,5,4,3,2,1]
    list3 = [3,5,2,7,78,4,34,6]
    runCode(list1)
    runCode(list2)
    runCode(list3)
    
        