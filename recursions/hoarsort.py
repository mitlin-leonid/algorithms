def hoar_sort(A):
    """
        алгоритм Тони Хоара или быстрая сортировка (quick_sort)
    """
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1
    return A


def test_hoar_sort(sort_algorithm):
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
    test_hoar_sort(hoar_sort)