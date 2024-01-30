import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal


def ZOOtable(zoo: dict) -> pd.DataFrame:
    table = pd.DataFrame.from_dict(zoo, orient='index')
    table.insert(loc=0, column='Type', value=np.array(zoo.keys()))
    table = table.loc[:, table.notna().all(axis=0)]#yдаляются все столбцы, содержащие хотя бы одно значение NaN
    table.sort_values(by=['Type'])
    reordered_columns = list(table.columns)
    reordered_columns[1:] = sorted(reordered_columns[1:])
    table = table.reindex(reordered_columns, axis=1)
    return table


def main():
    ######################################################
    ZOO = {
        'cat': {'color': 'black', 'tail_len': 50.0, 'injured': False},
        'dog': {'age': 6, 'tail_len': 30.5, 'injured': True}
    }
    answer = pd.DataFrame(
        {
            'Type': ['cat', 'dog'],
            'injured': [False, True],
            'tail_len': [50.0, 30.5]
        }
    )
    df = ZOOtable(ZOO)

    assert_frame_equal(
        df.reset_index(drop=True),
        answer
    )
    ######################################################
    ZOO = {
        'cat': {'color': 'black'},
        'dog': {'age': 6}
    }
    answer = pd.DataFrame(
        {
            'Type': ['cat', 'dog']
        }
    )

    df = ZOOtable(ZOO)

    assert_frame_equal(
        df.reset_index(drop=True),
        answer
    )
    ######################################################


if __name__ == "__main__":
    main()