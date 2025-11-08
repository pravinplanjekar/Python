import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent variables : ",X)
    print("Values of Dependent variables : ",Y)
    
    XSum = 0
    YSum = 0

    for i in range(len(X)):
        XSum = XSum + X[i]
        YSum = YSum + Y[i]
        
    mean_x = XSum / len(X)
    mean_y = YSum / len(Y)
    
    print("X_MEAN is : ",mean_x)
    print("Y_MEAN is : ",mean_y)
    
def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()