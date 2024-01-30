import pandas as pd


def men_stat(df: pd.DataFrame) -> (float, float, float, float):
    required_entries = df.loc[(df['Survived'] == 0) & (df['Sex'] == 'male'), 'Age']
    return required_entries.mean(), required_entries.median(), required_entries.max(), required_entries.min()


def main():
    print(men_stat(pd.read_csv('titanic_train.csv', index_col='PassengerId')))


if __name__ == "__main__":
    main()