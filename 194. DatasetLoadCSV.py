import pandas as pd

def main():
    dataframe = pd.read_csv("iris.csv")

    print(dataframe.head())

if __name__ == "__main__":
    main()