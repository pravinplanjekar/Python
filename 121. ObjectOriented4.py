class Employee:
    CompanyName = "Marvellous"          # Class variable

    def __init__(self, A, B, C):        # Constructor
        print("Inside constructor")
        self.Name = A                   # Instance variable
        self.Salary = B                 # Instance variable
        self.City = C                   # Instance variable

    def __del__(self):                  # Destructor
        print("Inside destructor")

    def DisplayInfo(self):              # Instance method
        print("Inside Instance method DisplayInfo")
        print("Emplyee Name : "+self.Name)
        print("Emplyee Salary : ",self.Salary)
        print("Emplyee City : "+self.City)
        
    @classmethod
    def DisplayCompanyDetails(cls):     # Class method
        print("Inside Class method DisplayCompanyDetails")
        print("Company Name : "+cls.CompanyName)

    @staticmethod
    def DisplayCompanyPolicy():
        print("Inside static method DisplayCompanyPolicy")
        print("All employees are 18+")
        print("Working hours are 9 to 6")
        print("Holidays : Saturday & Sunday")

def main():
    print("Class variable : "+Employee.CompanyName)
    Employee.DisplayCompanyDetails()

    emp1 = Employee('Rahul',15000,'Pune')       # Object creation
    emp2 = Employee('Pooja',25000,'Mumbai')     # Object creation

    print("Emplyee Name : "+emp1.Name)
    print("Emplyee Salary : ",emp1.Salary)
    print("Emplyee City : "+emp1.City)
    
    emp2.DisplayInfo()

    Employee.DisplayCompanyPolicy()

    del emp1
    del emp2
    
if __name__ == "__main__":
    main()