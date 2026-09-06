class DataFrameReporter:
    def __init__(self, float_format = '0.05f', percent_format = '0.02%', include_all = False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title = None):
        if title:
            print(title)

        print('Количетсво столбцов: ', df.shape[1])
        print('Количетсво строк: ', df.shape[0])

        duplicates = df.duplicated().sum()

        print('Количетсво дубликатов: ', duplicates)

        print('Доля дупликатов: ', format(duplicates / df.shape[0], self.percent_format))

        print(df.describe(include = 'all' if self.include_all else None))

        print('Количетсво пропусков: ', df.isna().sum().sum())

        print('Доля пропусков: ', format(df.isna().mean(axis = None), self.float_format))