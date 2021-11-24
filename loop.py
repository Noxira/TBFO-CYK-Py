def loop2(A):
    stop = False
    i = 1
    while(stop==False):
        if(A<10**i):
            stop=True
        else:
            i=i+1

    print (10**i)

def loop2(A):
    for i in range(A):
        B = input("minta b dong ngab")
        print(i + B)
