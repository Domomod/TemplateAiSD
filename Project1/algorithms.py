import random
import math

class Algorithms:

    @staticmethod
    def insert_sort(arr: list) -> None:
        for i in range(0, len(arr)):
            key: int = arr[i]
            j: int = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            
    @staticmethod
    def selection_sort(arr: list) -> None:
        for i in range(len(arr)-1):
            min_index: int = i
            for d in range(min_index + 1, len(arr)):
                if arr[d] < arr[min_index]:
                    min_index = d
            arr[i], arr[min_index] = arr[min_index], arr[i]

    @staticmethod
    def selection_sort_with_step(arr: list, step: int = 1, shift: int = 0):
        for i in range(shift, len(arr)-step, step):
            min_index: int = i
            for d in range(min_index + step, len(arr), step):
                if arr[d] < arr[min_index]:
                    min_index = d
            arr[i], arr[min_index] = arr[min_index], arr[i]

    @staticmethod
    def shell_sort(arr: list) -> None:
        
        # Growth getting method by Robert Sedgewick
        # based on the content of the lecture
        # 1, 8, 23, 77, 281, 1073, ...
        def get_growth(k: int):
            return 1 if k <= 0 else 4**(k) + 3 * 2**(k-1) + 1
        
        # Calculate max growth
        max_growth = 0
        while(len(arr) // get_growth(max_growth) >= 2):
            max_growth += 1
        max_growth -= 1
        
        # For growth from max to 1
        for i in range(max_growth, -1, -1): # from g to 0
            curr_growth = get_growth(i)

            # For every set with step = max_growth use selection_sort
            for s in range(0, curr_growth): # current set
                Algorithms.selection_sort_with_step(arr, curr_growth, s)


    @staticmethod
    def quicksort_partition(arr: list, k: int, l: int, rand_pivot: bool = True) -> int:
        x = arr[k if not rand_pivot else random.randint(k, l)]
        i = k
        j = l
        while True:
            while arr[i] < x:
                i += 1
            while arr[j] > x:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            else:
                return j

    @staticmethod
    def quicksort(arr: list, k: int = 0, l: int = None, rand_pivot: bool = True):
        if l == None:
            l = len(arr)-1
        
        if k < l:
            p = Algorithms.quicksort_partition(arr, k, l, rand_pivot)
            Algorithms.quicksort(arr, k, p)
            Algorithms.quicksort(arr, p+1, l)

    @staticmethod
    def recover_heap(arr: list, length: int, parent: int = 0):

        if parent >= length:
            return
    
        ids = [parent, parent*2+1, parent*2+2]

        max_id = ids[0]
        for id in ids:
            if id < length and arr[id] > arr[max_id]:
                max_id = id
        
        arr[parent], arr[max_id] = arr[max_id], arr[parent]

        Algorithms.recover_heap(arr, length, ids[1])
        Algorithms.recover_heap(arr, length, ids[2])

    @staticmethod
    def heap_sort(arr: list):
        Algorithms.recover_heap(arr, len(arr))

        end_bound = len(arr)-1
        while end_bound >= 0:
            arr[0], arr[end_bound] = arr[end_bound], arr[0]
            Algorithms.recover_heap(arr, end_bound)
            end_bound -= 1
        
        

n = 20
x = [random.randint(1, n) for i in range(n)]

alg = Algorithms()

print(x)
alg.heap_sort(x)
print(x)
