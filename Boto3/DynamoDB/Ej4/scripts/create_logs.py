import pandas as pd
import os
from datetime import datetime


def create_logs(sample_size=10):
    df = pd.read_csv('../data/OnlineRetail.csv', encoding = "ISO-8859-1").dropna()
    df_sample = df.sample(n=sample_size)

    name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    df_sample.to_json(f'../logs/{name}.log', orient="records")

    print('Creating Logs')


if __name__ == '__main__':
    sample_size=10
    create_logs(sample_size=sample_size)