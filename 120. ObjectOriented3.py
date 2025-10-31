class Employee:
    CompanyName = "Marvellous"

    def __init__(self, A, B, C):
        print("Inside constructor")
        self.Name = A
        self.Salary = B
        self.City = C

    def __del__(self):
        print("Inside destructor")

def main():
    print("Class variable : "+Employee.CompanyName)
    
    emp1 = Employee('Rahul',15000,'Pune')
    emp2 = Employee('Pooja',25000,'Mumbai')

    print("Emplyee Name : "+emp1.Name)
    print("Emplyee Salary : ",emp1.Salary)
    print("Emplyee City : "+emp1.City)
    
if __name__ == "__main__":
    main()