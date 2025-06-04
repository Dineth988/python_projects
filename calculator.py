

# This is my first python project


nm1 = float(input("Number 1: "))
nm2 = float(input("Number 2: "))
op = input("Operation: ")




def cal():
    if op=="+":
        answer = nm1+nm2
    elif op=="-":
        answer = nm1-nm2
    elif op=="*":
        answer = nm1*nm2
    elif op=="/":
        answer = nm1/nm2        
    return answer

print(cal())