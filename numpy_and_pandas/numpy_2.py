import numpy as np
from numpy.testing import assert_array_equal


def sort_evens(a: np.array) -> np.ndarray:
    result = np.copy(a)
    even_numbers_indices = np.where(result % 2 == 0)
    result[even_numbers_indices] = np.sort(result[even_numbers_indices])#извлекаются все четные числа из копии массива, они сортируются с помощью np.sort() и заменяются обратно в копию массива на соответствующие им позиции
    return result


def main():
    #####################################################
    assert_array_equal(sort_evens(np.array([])), np.array([]))
    ######################################################
    assert_array_equal(sort_evens(np.array([2, 0])), np.array([0, 2]))
    ######################################################
    assert_array_equal(sort_evens(np.array([9, 3, 1, 5, 7])), np.array([9, 3, 1, 5, 7]))
    ######################################################
    assert_array_equal(sort_evens(np.array([8, 12, 4, 10, 6, 2])), np.array([2, 4, 6, 8, 10, 12]))
    #####################################################


if __name__ == "__main__":
    main()