import numpy as np
import pandas as pd
from datetime import datetime as dt
from pandas.testing import assert_frame_equal


def reformat_date_to_datetime(date: str):
    rus_to_eng_month = {
        'января': 'January',
        'февраля': 'February',
        'марта': 'March',
        'апреля': 'April',
        'мая': 'May',
        'июня': 'June',
        'июля': 'July',
        'августа': 'August',
        'сентября': 'September',
        'октября': 'October',
        'ноября': 'November',
        'декабря': 'December'
    }
    date_split = date.split(' ')
    date_split[1] = rus_to_eng_month[date_split[1]]
    return dt.strptime(' '.join(date_split), '%d %B %Y г.')


def rus_feature(df: pd.DataFrame) -> pd.DataFrame:
    df.insert(loc=3, column='Полных лет',
              value=(df['Дата смерти'].map(reformat_date_to_datetime) - df['Дата рождения'].map(
                  reformat_date_to_datetime)) // np.timedelta64(1, 'Y'))
    return df


def main():
    ######################################################
    names = pd.DataFrame({'Имя': ['Никола Тесла', 'Альберт Эйнштейн'],
                          'Дата рождения': ['10 июля 1856 г.', '14 марта 1879 г.'],
                          'Дата смерти': ['7 января 1943 г.', '18 апреля 1955 г.']})
    answer = pd.DataFrame({'Имя': ['Никола Тесла', 'Альберт Эйнштейн'],
                           'Дата рождения': ['10 июля 1856 г.', '14 марта 1879 г.'],
                           'Дата смерти': ['7 января 1943 г.', '18 апреля 1955 г.'],
                           'Полных лет': [86, 76]})
    assert_frame_equal(
        rus_feature(names),
        answer
    )
    ######################################################
    names = pd.DataFrame({'Имя': ['Никола Тесла'],
                          'Дата рождения': ['10 июля 1856 г.'],
                          'Дата смерти': ['7 января 1857 г.']})
    answer = pd.DataFrame({'Имя': ['Никола Тесла'],
                           'Дата рождения': ['10 июля 1856 г.'],
                           'Дата смерти': ['7 января 1857 г.'],
                           'Полных лет': [0]})
    assert_frame_equal(
        rus_feature(names),
        answer
    )
    ######################################################
    names = pd.DataFrame({'Имя': ['Никола Тесла'],
                          'Дата рождения': ['1 января 2000 г.'],
                          'Дата смерти': ['31 декабря 2000 г.']})
    answer = pd.DataFrame({'Имя': ['Никола Тесла'],
                           'Дата рождения': ['1 января 2000 г.'],
                           'Дата смерти': ['31 декабря 2000 г.'],
                           'Полных лет': [0]})
    assert_frame_equal(
        rus_feature(names),
        answer
    )


if __name__ == "__main__":
    main()