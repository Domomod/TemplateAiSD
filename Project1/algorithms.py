class Algorithms:

    @staticmethod
    def insert_sort(arr: list) -> list:
        for i in range(0, len(arr)):
            key: int = arr[i]
            j: int = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def selection_sort(arr):
        for i in range(len(arr)-1):
            min_index = i
            for d in range(min_index + 1, len(arr)):
                if arr[d] < arr[min_index]:
                    min_index = d
            arr[i], arr[min_index] = arr[min_index], arr[i]


x = [2, 3, 4, 2, 1, 5]
alg = Algorithms()
alg.selection_sort(x)
print(x)
