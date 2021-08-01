def AND_gate(A, B):
    if A == 1 and B == 1:
        return 1
    else:
        return 0

def XOR_gate (A, B):
    if A == 0 and B == 0:
        return 0
    elif A == 1 and B == 1:
        return 0
    else:
        return 1

def NAND_gate(A, B): 
    if A == 1 and B == 1: 
        return  0
    else:
        return 1

def OR_gate(A, B): 
    if A == 0 and B == 0: 
        return  0
    else:
        return 1
        
def NOR_gate (A, B):
    if A == 0 and B == 0: 
        return  1
    else:
          return 0

def NOT_gate(A):
    if A == 0:
        return 1
    else:
        return 0

