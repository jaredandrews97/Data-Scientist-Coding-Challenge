import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import mean_squared_error

def csv_solution():
    df = pd.read_csv('testSet.csv')

    kf = KFold(shuffle=True)
    lr = LinearRegression()
    for i, (train_index, test_index) in enumerate(kf.split(df['Sickle Percentage'].to_frame())):
        train = df.loc[train_index]
        test = df.loc[test_index]

        lr.fit(train[['Sickle Percentage']], train['Pain Score'])
        print(lr.score(test[['Sickle Percentage']], test['Pain Score']))
    return lr


if __name__ == '__main__':
    csv_solution()
