X2 = []
Y2 = []
XY = []

def input(check, X, Y):
    global c, x, y
    c = check
    x = X
    y = Y
    
if c == "n":
    for a in x:
        X2.append(a**2)
    for b in y:
        Y2.append(b**2)
    for j, k in zip(x, y):
        XY.append(j * k)
    for c in X:
        Xt = Xt + c
    print("Summation of x  = " + str(Xt) )
    for d in Y:
        Yt = Yt + d
    print("Summation of y = " + str(Yt) )
    for f in X2:
        X2t = X2t + f
    print("Summation of x^2 = " + str(X2t) )
    for e in Y2:
        Y2t = Y2t + e
    print("Summation of y^2 = " + str(Y2t) )
    for g in XY:
        XYt = XYt + g
    print("Summation of xy = " + str(XYt) )
    
def Observations(N):
    global n
    n = N
    
def Xbar(Xt):
    global xbar
    xbar = Xt / n
    print("Xbar = " + str(xbar))
     
def Ybar(Yt):
    global ybar
    ybar = Yt / n
    print ("Ybar = " + str(ybar))
    
def Cov(XYt):
    global cov
    cov = XYt / n - xbar * ybar
    print("Cov = "+ str(cov))

def sigmaX(X2t):
    global sigmax
    sigmax = (X2t/ n - xbar*xbar)**(1/2)
    print("SigmaX = " + str(round(sigmax, 3)))
    
def sigmaY(Y2t):
    global sigma_y
    sigma_y = (Y2t / n - ybar*ybar)**(1/2)
    print("SigmaY = " + str(round (sigma_y, 3)))
    
def rXY():
    rxy = cov / (sigmax*sigma_y)
    print("rxy = " + str(round(rxy, 3)))



