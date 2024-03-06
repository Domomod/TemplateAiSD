import random

class Generate:

    @staticmethod
    def ascending(n: int, max_step: int = None) -> list[int]:
        if max_step == None:
            max_step = int(n * 0.5)

        arr = [0]
        for i in range(1, n):
            arr.append(arr[i-1] + int(random.randint(0, max_step)))

        return arr
    
    @staticmethod
    def descending(n: int, max_step: int = None) -> list[int]:
        return Generate.ascending(n, max_step)[::-1]
    
    @staticmethod
    def random(n: int) -> list[int]:
        return [random.randint(0, n) for _ in range(n)]
    
    @staticmethod
    def as_des_cending(n: int, max_step: int = None) -> list[int]:
        return Generate.ascending(n//2, max_step) + Generate.descending((n//2) + (0 if not n%2 else 1), max_step)

