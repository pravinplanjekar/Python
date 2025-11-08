import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("iris.csv")

    sns.boxplot(x="variety", y = "petal.length", data=df)

    plt.title("Marvellous Boxplot for Petal length by variety")
    plt.show()

if __name__ == "__main__":
    main()