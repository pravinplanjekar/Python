from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def MarvellousCalculateAcuuracyKNN():
    iris = load_iris()
    
    data = iris.data
    target = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(data,target,test_size=0.5,random_state=42)

    model = KNeighborsClassifier(n_neighbors = 3)
    model.fit(X_train, Y_train)
    predictions = model.predict(X_test)
    Accuracy = accuracy_score(predictions,Y_test)
    print("Accuracy if K is 3 ",Accuracy*100)

    model = KNeighborsClassifier(n_neighbors = 5)
    model.fit(X_train, Y_train)
    predictions = model.predict(X_test)
    Accuracy = accuracy_score(predictions,Y_test)
    print("Accuracy if K is 5 ",Accuracy*100)

    model = KNeighborsClassifier(n_neighbors = 7)
    model.fit(X_train, Y_train)
    predictions = model.predict(X_test)
    Accuracy = accuracy_score(predictions,Y_test)
    print("Accuracy if K is 7 ",Accuracy*100)

def main():
    MarvellousCalculateAcuuracyKNN()

if __name__ == "__main__":
    main()