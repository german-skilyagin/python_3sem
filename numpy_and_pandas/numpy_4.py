import numpy as np
from numpy.testing import assert_array_equal


def get_sum_of_digits(n) -> np.ndarray:
    return np.sum([int(d) for d in str(n)])


def num_sum(a: np.ndarray) -> np.ndarray:
    vectorized = np.vectorize(get_sum_of_digits)
    return vectorized(a)


def main():
    ######################################################
    assert_array_equal(num_sum(np.array([82])), np.array([10]))
    ######################################################
    assert_array_equal(num_sum(np.array([1241, 354, 121])), np.array([8, 12, 4]))
    ######################################################
    assert_array_equal(num_sum(np.array([1, 22, 333, 4444, 55555])), np.array([1, 4, 9, 16, 25]))


if __name__ == "__main__":
    main()