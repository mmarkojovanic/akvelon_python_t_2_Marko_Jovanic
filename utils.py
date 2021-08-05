def fibonacci(n):
    f1=0
    f2=1
    i=0
    while(i<n):
        tmp = f2
        f2=f1+f2
        f1=tmp
        i+=1
    return f1
