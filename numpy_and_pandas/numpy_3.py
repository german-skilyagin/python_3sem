import numpy as np
from numpy.testing import assert_array_equal


def tensor_mask(x: np.ndarray, mask: np.ndarray) -> np.ndarray:
    return np.logical_xor(x, mask)#выполняет операцию логического исключающего ИЛИ (XOR) между этими двумя массивами при помощи функции np.logical_xor()
    return (x ^ mask)

def main():
    ######################################################
    x = np.zeros(9, dtype=int).reshape((1, 3, 3))
    mask = np.zeros(9, dtype=int).reshape((3, 3))
    assert_array_equal(tensor_mask(x, mask), np.zeros(9, dtype=int).reshape((1, 3, 3)))
    ######################################################
    x = np.zeros(9 * 3, dtype=int).reshape((3, 3, 3))
    mask = np.ones(9, dtype=int).reshape((3, 3))
    assert_array_equal(tensor_mask(x, mask), np.ones(9 * 3, dtype=int).reshape((3, 3, 3)))
    ######################################################
    x = np.array([[[1, 0, 1],
                   [1, 1, 1],
                   [0, 0, 1]]])
    mask = np.array([[1, 1, 0],
                     [1, 1, 0],
                     [1, 1, 0]])
    assert_array_equal(tensor_mask(x, mask),
                       np.array([[[0, 1, 1],
                                  [0, 0, 1],
                                  [1, 1, 1]]]))
    ######################################################


if __name__ == "__main__":
    main()