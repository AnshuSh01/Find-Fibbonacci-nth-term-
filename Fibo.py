def Fibbo(index):
    if index==0:
        return 0
    elif index==1:
        return 1
    else:
        return Fibbo(index-1)+Fibbo(index-2)
 
if __name__ == '__main__':
    EnterInput=int(input("enter the nth term at which u want to know the value of that particular index no."))
    print(f"The value at Index {EnterInput} is ",Fibbo(EnterInput))
