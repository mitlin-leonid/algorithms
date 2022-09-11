def choice_sort(A):
    """
    Алгоритм сортировки выбором
    1. Проходим по массиву и ищем наименьший элемент
    2. После его нахождения меняем с первым, так как надо было с чего-то начинать
    3. После смены начинаем проходить по массиву заново, исключая первый, так как он наименьший.
    7. Сложность алгоритма O(N^2)

    Суть в том, что пузырек движеться вверх
    """
    N = len(A)
    for pos in range(N-1):
        for i in range(pos + 1, N):
            if A[i] < A[pos]:
                A[i], A[pos] = A[pos], A[i]


def test_choice_sort(sort_algorithm):
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
    test_choice_sort(choice_sort)