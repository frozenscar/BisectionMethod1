#bisection method
def f(a):
    return (a**3)-(5*a)+1
x1 =0
x2 =1
for i in range(5):
    print("x1 = ",x1,"      x2 =",x2)
    f1 = f(x1)
    f2 = f(x2)
    print("f(",x1,")=",f1,"f(",x2,")=",f2)
    x0 = (x1+x2)/2
    f0 =  f(x0)
    print("f(",x0,")=",f(x0))
    if(f0 > 0):
        x1=x0
    elif(f0 < 0):
        x2 = x0
