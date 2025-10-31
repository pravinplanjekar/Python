#include<iostream>
using namespace std;

class Arithematic
{
    public:
        int No1, No2;

        Arithematic(int A, int B)
        {
            this->No1 = A;
            this->No2 = B;
        }

        int Addition()
        {
            int Result = 0;
            Result = this->No1 + this->No2;
            return Result; 
        }
};

int main()
{
    Arithematic obj(10,11);

    int Ret = 0;
    Ret = obj.Addition();

    cout<<"Addition is : "<<Ret<<"\n";

    return 0;
}