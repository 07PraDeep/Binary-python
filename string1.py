import decimalConversion as cc
def rev(number):
    st=""
    for i in range(len(number)-1,-1,-1):
        st=st+str(number[i])
        st1=st[::-1]
    return st1

