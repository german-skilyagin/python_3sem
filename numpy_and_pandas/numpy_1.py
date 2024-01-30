import numpy as np
import numpy.testing as test


def nearest_value(x: np.array, a: float) -> float:
    x = x.flatten()
    x.sort()
    return x.flat[np.abs(a - x).argmin()]#вычисляется абсолютная разница между числом a и каждым элементом массива x с помощью функции np.abs(). Результат сортируется с помощью метода argmin(), чтобы найти индекс элемента массива x, который наименее отличается от числа a
#находим ближайшее значение к числу a в массиве x с помощью метода flat.

def main():
    ######################################################
    test.assert_equal(
        nearest_value(np.array([1, 2, 13]), 10),
        13)
    ######################################################
    test.assert_equal(
        nearest_value(np.array([-1, 0]), -0.5),
        -1)
    ######################################################
    test.assert_equal(
        nearest_value(np.array([[[1], [2], [3]], [[4], [5], [6]]]), 4.5),
        4)
    ######################################################
    test.assert_equal(
        nearest_value(np.array([[1, 2, 13],
                                [15, 6, 8],
                                [7, 18, 9]]), 7.2),
        7)
    ######################################################
    test.assert_equal(
        nearest_value(np.array([[-1, -2],
                                [-15, -6]]), -100),
        -15)
    ######################################################
    test.assert_equal(
        nearest_value(np.array([[2, 2],
                                [12, 12]]), 7),
        2)
    #####################################################
    test.assert_equal(
        nearest_value(np.array([[-2, -2],
                                [-12, -12]]), -7),
        -12)
    #####################################################


if __name__ == "__main__":
    main()