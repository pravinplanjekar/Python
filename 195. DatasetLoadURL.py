import pandas as pd

def main():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

    header = ['sepal_length', 'sepal_with', 'petal_length', 'petal_width','class']

    dataset = pd.read_csv(url,names=header)

    print(dataset.head())

if __name__ == "__main__":
    main()