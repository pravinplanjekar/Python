import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def main():
    diabetes = pd.read_csv("diabetes.csv")

    print(diabetes.columns)

    print(diabetes.head())

    print(diabetes.shape)

    X = diabetes.drop(columns = ['Outcome'])
    Y = diabetes['Outcome']

    print(X.shape)
    print(Y.shape)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    logreg = LogisticRegression().fit(X_train,Y_train)

    print("Training Accuracy : ")
    print(logreg.score(X_train,Y_train))

    print("Testing Accuracy : ")
    print(logreg.score(X_test,Y_test))

if __name__ == "__main__":
    main()