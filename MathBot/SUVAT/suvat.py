
def InputSuvat():
    print ("Please input values with an X in the place of the missing one and a ? in the place of the one to work out: ")
    s = input ("Displacement (s): ")
    u = input ("Initial velocity (u): ")
    v = input ("Final Velocity (v): ")
    a = input ("Acceleration (a): ")
    t = input ("Time (t): ")
    return s,u,v,a,t
def Inputquadrat():
    print("please put your equation in the form [a]x^2 + [b]x + [c]")
    a=input("a = ")
    b=input("b = ")
    c=input("c = ")
    return a,b,c
def quadrat (a,b,c):
    x1 = (-float(b)-((float(b)**2)-(4*float(a)*float(c)))**0.5)/(2*float(a))
    x2 = (-float(b)+((float(b)**2)-(4*float(a)*float(c)))**0.5)/(2*float(a))
    return x1, x2
def runQuadrat ():
    a,b,c = Inputquadrat()
    x1,x2 = quadrat(a,b,c)
    print ("x = "+str(x1)+" or "+str(x2))
def workingsS (s,u,v,a,t):

    if (s=="X") or (s=="x"):
        x = s
    elif (u=="X") or (u=="x"):
        x = (float(v)*float(t))-(0.5*float(a)*(float(t)**2))
    elif (v=="X") or (v=="x"):
        x = (float(u)*float(t))+(0.5*float(a)*(float(t)**2))
    elif (a=="X") or (a=="x"):
        x = (0.5*(float(u)+float(v))*float(t))
    elif (t=="X") or (t=="x"):
        x = ((float(v)**2)-(float(u)**2))/(2*float(a))
    else:
        print("Invalid input")
        
    return x

def workingsU (s,u,v,a,t):

    if (s=="X") or (s=="x"):
        x = float(v)-(float(a)*float(t))
    elif (u=="X") or (u=="x"):
        x = u
    elif (v=="X") or (v=="x"):
        x = (float(s)+(0.5*float(a)*(float(t)**2)))
    elif (a=="X") or (a=="x"):
        x = (float(s)-(0.5*float(t)*float(v)))/(0.5*float(t))
    elif (t=="X") or (t=="x"):
        x = ((float(v)**2)+(2*float(a)*float(s)))**0.5
    else:
        print("Invalid input")
        
    return x

def workingsV (s,u,v,a,t):

    if (s=="X") or (s=="x"):
        x = (float(u)+(float(a)*float(t)))
    elif (u=="X") or (u=="x"):
        x = (float(s)+(0.5*float(a)*(float(t)**2)))/float(t)
    elif (v=="X") or (v=="x"):
        x = v
    elif (a=="X") or (a=="x"):
        x = (float(s)-(0.5*float(t)*float(u)))/(0.5*float(t))
    elif (t=="X") or (t=="x"):
        x = ((float(u)**2)+(2*float(a)*float(s)))**0.5
    else:
        print("Invalid input")
        
    return x

def workingsA (s,u,v,a,t):

    if (s=="X") or (s=="x"):
        x = (float(v)-float(u))/float(t)
    elif (u=="X") or (u=="x"):
        x = ((float(v)*float(t))-float(s))/(0.5*(float(t)**2))
    elif (v=="X") or (v=="x"):
        x = (float(s)-(float(u)*float(t)))/(0.5*(float(t)**2))
    elif (a=="X") or (a=="x"):
        x=a
    elif (t=="X") or (t=="x"):
        x=((float(v)**2)-(float(u)**2))/(2*float(s))
    else:
        print("Invalid input")
        
    return x

def workingsT (s,u,v,a,t):

    if (s=="X") or (s=="x"):
        x = (float(v)-float(u))/float(a)
    elif (u=="X") or (u=="x"):
        x1,x2 = quadrat((float(a)*-0.5),(float(v)),(float(s)*-1))
        x = str(x1)+" or "+str(x2)
    elif (v=="X") or (v=="x"):
        x1,x2 = quadrat((float(a)*0.5),(float(u)),(float(s)*-1))
        x = str(x1)+" or "+str(x2)
    elif (a=="X") or (a=="x"):
        x = (2*float(s))/(float(u)+float(v))
    elif (t=="X") or (t=="x"):
        x = t
    else:
        print("Invalid input")
        
    return x
def runSUVAT ():
    s,u,v,a,t = InputSuvat()
    if s == "?":
        x = workingsS(s,u,v,a,t)
        print("displacement = "+str(x))
    elif u == "?":
        x = workingsU(s,u,v,a,t)
        print("initial velocity = "+str(x))
    elif v == "?":
        x = workingsV(s,u,v,a,t)
        print("final velocity = "+str(x))
    elif a == "?":
        x = workingsA(s,u,v,a,t)
        print("acceleration = "+str(x))
    elif t == "?":
        x = workingsT(s,u,v,a,t)
        print("time = "+str(x))
    else:
        print("invalid input")
        runSUVAT()
runSUVAT()

