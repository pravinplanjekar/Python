class Base:
    def Display(self):
        print("Inside Base Display")

class Derived(Base):
    def Display(self):  # overrided method
        print("Inside Derived Display")

def main():
    bobj = Base()
    dobj = Derived()

    bobj.Display()
    dobj.Display()
    
if __name__ == "__main__":
    main()
    
