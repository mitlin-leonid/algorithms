def bubble_sort(A):
    """
    Алгоритм сортировки пузырьком
    1. берутся два первых элемента
    2. сравниваются
    3. меняем местами так, что больший двигаем вправо
    4. проходим до конца
    5. по ходу движения больший окажется последним в массиве
    6. начинаем заного и уменьшаем количество проходов на 1
    7. Сложность алгоритма O(N^2)

    Суть в том, что пузырек движеться вверх
    """
    count = 0
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
            count += 1
    print('длина последовательности', N, 'количество проходов', count)

def test_bubble_sort(sort_algorithm):
    print("testcase#1 ", end="")
    A1 = [4, 2, 5, 1, 3]
    A1_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A1)
    print("Ok" if A1 == A1_sorted else "fail")

    print("testcase#2 ", end="")
    A2 = list(range(10, 20)) + list(range(0, 10))
    A2_sorted = list(range(20))
    sort_algorithm(A2)
    print("Ok" if A2 == A2_sorted else "fail")

    print("testcase#3 ", end="")
    A3 = [4, 2, 2, 1, 4]
    A3_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A3)
    print("Ok" if A3 == A3_sorted else "fail")





if __name__ == "__main__":
    test_bubble_sort(bubble_sort)
