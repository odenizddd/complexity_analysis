from time_analysis import analyse, visualize
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.linear_pass import linear_pass

algorithms = {
    'Bubble Sort': bubble_sort,
    'Merge Sort': merge_sort,
    'Linear Pass': linear_pass
}

input_sizes = [i for i in range(0, 2000, 200)]

visualize(algorithms, input_sizes)