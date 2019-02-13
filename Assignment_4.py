import math


#Sin Approximations
#Lagrange Polynomial Interpolation
def lagrangeInterpolation(x,name):
    xArray = listGen();
    
    resultSoFar=0;
    for xk in xArray: #Summation from k to n
        for xi  in xArray: #Product from i to n
            innerRSF=1;
            if(xi!=xk): #Takes care of dividing by zero and cancelling out
                innerRSF= innerRSF*(delta(xi,xk)*((x-xi)/(xk-xi))); #Lik
        if(name=="sin"):
            resultSoFar=resultSoFar+(math.sin(xk)*innerRSF)
        if(name=="cos"):
            resultSoFar = resultSoFar + (math.cos(xk) * innerRSF)
    return resultSoFar;

    
#Helper Function for Lagrange Interpolation
def delta(i,k):
    if(i==k):
        return 1.0
    else:
        return 0.0;

#List Generating Function
def listGen():
    xArray= [.9];
    for i in range(1, 21):
        xArray.append(round(xArray[i - 1] + .01, 4))
    return xArray;

#Divided Difference Method

def newtonDividedDifference(x):
    xArray = [.9, 1.1]; #CAN NOT be done with more than 2 elements in guess array

    n= len(xArray);
    resultSoFar = dividedDifference([xArray[0]])

    for k in range(1,n):
        innerRSF=1
        for j in range (0,(k-1)):
            innerRSF= innerRSF*(x-xArray[j])
        resultSoFar = resultSoFar + (dividedDifference(upToKArray(xArray,k))*innerRSF)
    return resultSoFar

def dividedDifference(xList):
    #print(len(xList));
    if len(xList) ==1:
        return xList[0];
    else:
        (dividedDifference(chopStartOfArray(xList)) - dividedDifference(chopEndOfArray(xList)))/((xList[len(xList)-1]) - xList[0])

def upToKArray(myList,k):
    newList=[]
    for i in range(0,k):
        newList.append(myList[i])
    return newList
def chopEndOfArray(myList): #Returns an array with all but last element in myList
    newList= [];
    for i in range(0,len(myList)-1):
        newList.append(myList[i])
    return newList;

def chopStartOfArray(myList): #Returns an array with all but first element in myList
    newList = []
    for i in range(1,len(myList)):
        newList.append(myList[i])
    return myList


#NEWTON FORWARD DIFFERENCE METHOD

def newtonForwardDiff(x):
    xArray = listGen()

    h=.02

    f1 = math.sin(1.01)
    f0 = math.sin(.99)

    resultSoFar = f0
    for k in range(1,3):
        resultSoFar= resultSoFar + atkinDelta(k)/(math.factorial(k) *pow(h,k))
    return resultSoFar


def atkinDelta(k): #Calculated delta at f0
    f1 = math.sin(1.01)
    f0= math.sin(.99)
    aDelta=0
    if(k==0):
        aDelta=f1-f0
    else:
        aDelta=atkinDelta(k-1)-atkinDelta(k-1)

    return aDelta


#d/dt[sin(x) Methods

def firstLagrangePolynomial():
    return (math.sin(1.01)-math.sin(.99))/(.02)

def forwardDifference():
    return (math.sin(1.01) - math.sin(1))/(.02)

def backwardDifference():
    return (math.sin(1) - math.sin(.99))/(.02)

def nPointFormula(x,n):
    #Instead of needing to calculate a new L' polynomial, we can use the fact than the first
    #derivative of sin is cos. and than just calculate the lagrange polynomials of cos
    #Ill also assume we have the exact values of sin for this implementation

    xArray = listGen();
    rsf=0
    for k in range(4):
        rsf = rsf +math.sin(xArray[k])*lagrangeInterpolation(x, "cos")
    return rsf

#Formating Helper Functions
def absError(approx, exact):
    return approx-exact;

def relError(approx, exact):
    return (abs(approx-exact))/exact;
def main():

    print();
    print("Sin(x) Approximations")
    sinExact = math.sin(1)

    print("Lagrange Interpolation: ")
    approxValue = lagrangeInterpolation(1,"sin")
    print("     Exact Val: {} | Abs Err: {} | Rel Err: {}" .format(approxValue, absError(sinExact,approxValue), relError(sinExact, approxValue)))

    approxValue = newtonDividedDifference(1)
    print("Newton's Divided Difference Method: ")
    print("     Exact Val: {} | Abs Err: {} | Rel Err: {}".format(approxValue, absError(sinExact, approxValue), relError(sinExact, approxValue)))

    approxValue = newtonDividedDifference(1);
    print("Newton's Forward DIfference Method: ")
    print(" Exact Val: {} | Abs Err: {} | Rel Err: {}".format(approxValue, absError(sinExact, approxValue), relError(sinExact, approxValue)))


    print("Exact sin(1): " + str(sinExact))

    print("\n" + "\n")
    print("Derivative of Sin(x) Approximations")
    dsinExact = math.cos(1);
    approxValue = firstLagrangePolynomial();
    print("First Lagrange Polynomial: ")
    print("     Exact Val: {} | Abs Err: {} | Rel Err: {}".format(approxValue, absError(sinExact, approxValue),relError(dsinExact, approxValue)))

    approxValue = forwardDifference();
    print("Forward Difference: ")
    print("     Exact Val: {} | Abs Err: {} | Rel Err: {}".format(approxValue, absError(sinExact, approxValue),relError(dsinExact, approxValue)))

    approxValue = backwardDifference()
    print("Backward Difference: ")
    print("     Exact Val: {} | Abs Err: {} | Rel Err: {}".format(approxValue, absError(sinExact, approxValue),relError(dsinExact, approxValue)))

    approxValue = nPointFormula(1,3)
    print("3 Point Formula: ")
    print("     Exact Val: {} | Abs Err: {} | Rel Err: {}".format(approxValue, absError(sinExact, approxValue),relError(dsinExact, approxValue)))

    approxValue = nPointFormula(1,5)
    print("5 Point Formula: ")
    print("     Exact Val: {} | Abs Err: {} | Rel Err: {}".format(approxValue, absError(sinExact, approxValue),relError(dsinExact, approxValue)))

    print("Exact d/dx(sin(1)): " + str(math.cos(1)))



main();

