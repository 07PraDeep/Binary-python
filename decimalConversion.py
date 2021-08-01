def bnum(number):
    list3=[]
    count=0
    out_value=""
    while count!=8:
        reminder=number%2
        list3.append(reminder)
        number=number//2
        count+=1
        list4=list3[::-1]
    return list4

