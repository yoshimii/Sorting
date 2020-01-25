# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)): # for each index in array
        smallest = arr[i]
        index = i
        for j in range(index + 1, len(arr)):
            print('i:', i, 'j:', arr[j], 'smallest: ', smallest)
            if arr[j] < smallest:
                smallest = arr[j]
                print(arr[index],smallest)
                index = j
        arr[index], arr[i] = arr[i], arr[index]
    print(arr)
    return arr
arr = [9, 5, 8, 4, 2, 1, 6, 0, 3, 7]
selection_sort(arr)
selection_sort(arr)
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr