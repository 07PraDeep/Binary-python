import bitAddition as ad1
import decimalConversion as con
import outputValidation as vd1
import string1 as st1

finalValue=0
print("Advance bit adder opening.........Done !")

state = True
while state==True:
    try:
        value1=int(input("Please enter first value:"))
        value3=vd1.outputValidation(value1)
        value5=con.bnum(value3)

        print("Conversion 1:- binary conversion of " +str(value3)+" is ", st1.rev(value5))
        
        value2=int(input("Please enter second value: "))
        value4=vd1.outputValidation(value2)
        value6=con.bnum(value4)
        
        print("Conversion 2:- binary conversion of " +str(value4)+" is ", st1.rev(value6))
        
        value7 = ad1.bitAddition(value5,value6, 0)
        finalValue=value3+value4
    
        print("Binary addition of " +str(st1.rev(value5))+" and "+str(st1.rev(value6))+" is ", value7)
        print("Final output of binary addition in decimal is ",str(finalValue))
    except:
        print("Only valid value are acceptable !!")

    condition = input("Type 1 for re-addition OR 2 for Shut down").lower()

    if condition=="2":
        state=False
        print("bit adder closed !")
        break
