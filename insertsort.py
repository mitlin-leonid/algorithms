def insertion_sort(array):
    """
    Алгоритм сортировки вставками
    1. берется первый элемент и он считается уже "отсортированным массивом"
    2. берем следующий за "отсортированным массивом" элемент
    3. сравниваем этот элемент с каждым элементом "отсортированного массива"
    4. если элемент меньше, то меняем местами
    5. После каждого прохода "отсортированный массив" увеличивается на один элемент
    7. Сложность алгоритма O(N^2)

    Суть в том, что отсортированный массив становиться больше, до тех пор, пока весь не отсортируется
    """
    N = len(array)
    for top in range(1, N):
        k = top
        while k > 0 and array[k-1] > array[k]:
            array[k], array[k-1] = array[k-1], array[k]
            k -= 1

def test_insertion_sort(sort_algorithm):
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
    test_insertion_sort(insertion_sort)
