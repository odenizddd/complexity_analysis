def bubble_sort(arr):
    for end in range( len(arr)-2, -1, -1 ):
        for index in range( 0, end+1 ):
            if arr[index] > arr[index+1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]
