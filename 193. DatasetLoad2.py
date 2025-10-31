from sklearn.datasets import load_iris

def main():
    dataset = load_iris()

    Line = "-"*30

    print("Elements from the dataset are : ")

    print(Line)

    for i in range(len(dataset.target)):
        print("ID %d , Fetures %s, Label : %s" % (i, dataset.data[i], dataset.target[i]))

    print(Line)
    
if __name__ == "__main__":
    main()