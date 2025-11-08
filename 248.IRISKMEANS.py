import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def main():
    dataset = pd.read_csv("iris.csv")
    X = dataset.iloc[:, [0,1,2,3]].values

    WCSS = []

    for k in range(1,11):
        model = KMeans(n_clusters=k, init='k-means++',n_init=10, random_state=42)
        model.fit(X)
        print(model.inertia_)   #WCSS
        WCSS.append(model.inertia_)

    plt.plot(range(1,11), WCSS, marker = 'o')
    plt.title("Elbow method for KMEANS")
    plt.xlabel("Value of K")
    plt.ylabel("Within Cluster Sum of Square")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()