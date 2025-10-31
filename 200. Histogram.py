import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("iris.csv")

    plt.hist(df['sepal.length'], bins=10, color="skyblue", edgecolor = 'black')

    plt.xlabel("Sepal Length")
    plt.ylabel("Frequency")
    plt.title("Marvellous Histogram for IRIS")

    plt.show()

if __name__ == "__main__":
    main()