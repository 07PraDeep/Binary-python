import decimalConversion as cv
import logicalGates as gt


def bitAddition(number1, number2, carry_in):
    carry_in=0
    listnew=[]
    product=""

    for i in range(len(number1)-1,-1,-1):
        first_bit=number1[i]
        second_bit=number2[i]
        sum1=gt.XOR_gate(first_bit, second_bit)
        sum2=gt.NAND_gate(sum1, carry_in)
        sum3=gt.OR_gate(sum1, carry_in)
        SUM=gt.AND_gate(sum2, sum3)
        cv1=gt.AND_gate(first_bit, second_bit)
        cv2=gt.AND_gate(sum1, carry_in)
        cv3=gt.NOR_gate(cv1, cv2)
        carry_out=gt.NOT_gate(cv3)
        carry_in=carry_out
        listnew.append(SUM)
        listNew1=listnew[::-1]
        product+=str(listnew[-1])
        product1=product[::-1]
    return product1


