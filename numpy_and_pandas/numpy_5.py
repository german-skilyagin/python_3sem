import numpy as np
from numpy.testing import assert_array_equal


def replace_nans(x: np.array) -> np.ndarray:
    mask = np.ma.array(x, mask=np.isnan(x))#создается маска, которая скрывает все значения NaN в массиве x.
    return np.where(np.isnan(x), np.ma.median(mask, axis=0), x)#вычисляется медиана для каждого столбца массива x с учетом маски, то есть игнорируя значения NaN.
#используется функция np.where(), чтобы заменить все значения NaN в массиве x на соответствующие значения медианы по столбцам.

def main():
    ######################################################
    assert_array_equal(replace_nans(
        np.array([[np.nan], [np.nan], [np.nan]])),
        np.array([[0.], [0.], [0.]])
    )
    ######################################################
    assert_array_equal(replace_nans(
        np.array([[0, 42, 42]])),
        np.array([[0, 42, 42]])
    )
    ######################################################
    assert_array_equal(replace_nans(
        np.array([[np.nan], [1], [np.nan]])),
        np.array([[1.], [1.], [1.]])
    )
    ######################################################
    assert_array_equal(replace_nans(
        np.array([[4], [1], [np.nan]])),
        np.array([[4], [1], [2.5]])
    )
    ######################################################
    assert_array_equal(replace_nans(
        np.array([[np.nan, np.nan, np.nan],
                  [4, np.nan, 5],
                  [np.nan, 8, np.nan]]).T),
        np.array([[0., 0., 0.],
                  [4., 4.5, 5.],
                  [8., 8., 8.]]).T
    )
    ######################################################


if __name__ == "__main__":
    main()