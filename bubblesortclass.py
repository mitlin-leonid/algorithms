class Buble:
    def __init__(self):
        self.name = "Я сортировщик пузырьком"
        pass

    def sort(self, A:list):
        N = len(A)
        for bypass in range(1, N):
            for k in range(0, N-bypass):
                if A[k] > A[k+1]:
                    A[k], A[k+1] = A[k+1], A[k]

bub = Buble()
A = [3,5,2,6,7]
print(A)
bub.sort(A)
print(A)