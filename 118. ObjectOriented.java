class Arithematic
{
    public int No1, No2;

    public Arithematic(int A, int B)
    {
        this.No1 = A;
        this.No2 = B;
    }

    public int Addition()
    {
        int Result = 0;
        Result = this.No1 + this.No2;
        return Result;
    }
}

class ObjectOriented
{
    public static void main(String A[])
    {
        Arithematic obj = new Arithematic(10,11);

        int Ret = 0;

        Ret = obj.Addition();

        System.out.println("Addition is : "+Ret);
    }
}