from algorithms import Algorithms
from generate import Generate

import time


volumes = [10, 100, 1_000, 2_500,  5_000, 10_000]

sorts = (
    ("Selection sort", lambda x: Algorithms.selection_sort(x)),
    ("Insert sort", lambda x: Algorithms.insert_sort(x)),
    ("Shell sort",lambda x: Algorithms.shell_sort(x)),
    ("Heap sort",lambda x: Algorithms.heap_sort(x)),
    ("Quicksort (rand pivot)",lambda x: Algorithms.quicksort(x, rand_pivot=True)),
    ("Quicksort (left pivot)",lambda x: Algorithms.quicksort(x, rand_pivot=False)),
)

gen = lambda v: Generate.ascending(v)

arrays = [gen(volume) for volume in volumes]

for name, sort in sorts:
    print(f'- {name} - ')

    for array in arrays:
        start = time.time()
        sort(array.copy())
        end = time.time()

        duration = (end - start)
        print(f'v: {len(array)} -  %.5f ' % duration)

    print('')




