import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def main():
    y_actual =    [10,20,30,40,50]
    y_predicted = [12,18,32,38,52]

    MSE = mean_squared_error(y_actual,y_predicted)

    RMSE = np.sqrt(MSE)

    print("Actual values : ",y_actual)
    print("Predicted values : ",y_predicted)
    print("Mean Squared Error : ",MSE)
    print("Root Mean Squared Error : ",RMSE)

if __name__ == "__main__":
    main()