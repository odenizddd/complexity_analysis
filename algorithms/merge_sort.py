def merge(arr1, arr2):
    if len(arr1) == 0 and len(arr2) == 0:
        return []
    elif len(arr1) != 0 and len(arr2) == 0:
        return arr1
    elif len(arr1) == 0 and len(arr2) != 0:
        return arr2
    else:
        left_array_index = 0
        right_array_index = 0

        return_array = []

        while True:
            if left_array_index == len(arr1) and right_array_index == len(arr2):
                break
            if left_array_index == len(arr1):
                return_array.append(arr2[right_array_index])
                right_array_index += 1
            elif right_array_index == len(arr2):
                return_array.append(arr1[left_array_index])
                left_array_index += 1
            else:
                if arr1[left_array_index] < arr2[right_array_index]:
                    return_array.append(arr1[left_array_index])
                    left_array_index += 1
                else:
                    return_array.append(arr2[right_array_index])
                    right_array_index += 1
        
        return return_array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    division_index = len(arr) // 2

    return merge(merge_sort(arr[:division_index]), merge_sort(arr[division_index:]))
