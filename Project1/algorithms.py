import random

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

n = 20
x = [random.randint(1, n) for i in range(n)]

alg = Algorithms()

print(x)
alg.shell_sort(x)
print(x)
