import pandas as pd

from src.reporter import DataFrameReporter


def main():
    df = pd.read_csv("data/payments.csv")

    reporter = DataFrameReporter(include_all=True)

    reporter.show_report(df,title="Отчёт по payments.csv")


if __name__ == "__main__":
    main()