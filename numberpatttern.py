def pattern1(n):
    x = 0
    for i in range(0,n):
        x += 1
        for j in range(0, i+1):
            print(x, end=" ")
        print("\r")
pattern1(5)   

def pattern2(n):
    for i in range(0,n):
        for j in range(1, i+2):
            print(j, end=" ")
        print("\r")
pattern2(5)


def pattern(n):
    for i in range(0,n):
        for j in range(1, i+2):
            print(j, end=" ")
        print("\r")

    for i in range(n,0,-1):
        for j in range(i-1,0,-1):
            print(j, end=" ")
        print("\r")     
pattern(5)

def pattern4(n):
    num = 1
    gap = n-1
    for j in range(1,n+1):
        num =j
        for i in range(1,gap+1):
            print(" ", end="")
        gap= gap-1

        for i in range(1,j+1):
            print(num,end="")
            num=num+1
        num=num-2
        for i in range(1,j):
            print(num,end="")
            num=num-1
        print()
pattern4(5)