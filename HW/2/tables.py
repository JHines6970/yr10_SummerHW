
number2=0
number=0
x=0
Finish=False
WO=0

while Finish == False:
    number=0
    x=1
    while x > 0:
        try:
            number=int(input("Enter a number >>>"))
        except ValueError:
            print("Please enter a number!")
            continue
        else:
            print("Number accepted.")
            print()
            x=0
    for x in range(0,10):
        WO=WO+1
        number2=number2+number
        print(str(number)+" X "+(str(WO)+" = "+str(number2)))
    Finish=True
    
