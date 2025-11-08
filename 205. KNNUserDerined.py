#     A,B,C,D
# X : 1,2,3,6
# Y : 2,3,1,5
#     R,R,B,B
import numpy as np
import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['x']- P2['x']) ** 2 + (P1['y']- P2['y']) ** 2)
    return Ans

def MarvellousKNN():
    line = "-"*50

    data = [{'point': 'A', 'x' : 1, 'y' : 2, 'label' : 'Red'},
            {'point': 'B', 'x' : 2, 'y' : 3, 'label' : 'Red'},
            {'point': 'C', 'x' : 3, 'y' : 1, 'label' : 'Blue'},
            {'point': 'D', 'x' : 6, 'y' : 5, 'label' : 'Blue'}]

    print(line)
    print("Training data set : ")
    print(line)

    for i in data:
        print(i)
    print(line)

    new_point = {'x' : 3, 'y' : 3}

    # Calculate the distances
    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(line)
    print("Calculated Distances are : ")
    print(line)

    for d in data:
        print(d)

    print(line)

    # Sort by Distance
    sorted_data = sorted(data, key= lambda item : item['distance'])

    print(line)
    print("Sorted data is : ")
    print(line)

    for d in sorted_data:
        print(d)

    print(line)

    k = 3
    nearest = sorted_data[:k]
    print(line)
    print("Sorted 3 elements are : ")
    for d in nearest:
        print(d)
    print(line)

    # Voting
    votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0) + 1

    print(line)
    print("Result of voting is : ")
    print(line)

    for d in votes:
        print("Name : ",d, "Value : ",votes[d])
    print(line)

    predicted_class = max(votes, key=votes.get)

    print("Predicted class for point (3,3) is : ", predicted_class)

def main():
    print("Demonstration of KNN algorithm")
    MarvellousKNN()

if __name__ == "__main__":
    main()