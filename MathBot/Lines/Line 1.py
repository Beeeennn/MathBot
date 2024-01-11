import numpy
6
def pointinp():
    x1 = float(input("What is the first x coord: "))
    y1 = float(input("What is the first y coord: "))
    x2 = float(input("What is the second x coord: "))
    y2 = float(input("What is the second y coord: "))
    print("\nyour coords:\n("+str(x1)+","+str(y1)+")\n("+str(x2)+","+str(y2)+")\n")
    return x1,y1,x2,y2

def grad (x1,y1,x2,y2):
    if x1==x2:
        gradient = "vertical"
    else:
        gradient = ((y1-y2)/(x1-x2))

    print("Gradient is "+str(gradient))
    return gradient

def eqn(x1,y1,x2,y2):
    grad1 = grad(x1,y1,x2,y2)
    print("\n(y - ("+str(y1)+"))= "+str(grad1)+"(x - ("+str(x1)+"))")

def intercept(x1,y1,x2,y2,grad1):
    YIntercept = y1-(grad1*x1)
    print ("Y Intercept is",str(YIntercept))
    XIntercept = x1-(y1/grad1)
    print ("X Intercept is",str(XIntercept))
    return XIntercept,YIntercept
def simpEqn(x1,y1,x2,y2):
    grad1 = grad(x1,y1,x2,y2)
    X,Y = intercept(x1,y1,x2,y2,grad1)
    print("\nEQUATIONS:")
    print("\nform 1:\ny = "+str(grad1)+"x + "+str(Y))



x1,y1,x2,y2 = pointinp()
simpEqn(x1,y1,x2,y2)
