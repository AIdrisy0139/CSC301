import math

exact = (-math.cos(1.5) + math.cos(.5))
print(exact)


def sin(x):
    return math.sin(x)


def listGen(start, end, stepSize):
    arr = []
    current = start;
    while (current <= end):
# Round is used because due to Floating Point Arithmetic, being of by 1 ULP will make the expressesion eval to false
# Ex: .5900000000001 IS NOT <= .59
        arr.append(current)
        current += stepSize
    if(len(arr)<4):
        arr.append(current)
    #print(current)
    return arr


'''TRAP Methods'''


def trapMethod(a, b):
    h = b - a
    return (h / 2) * (math.sin(a) + math.sin(b))


def compTrapRule(start, end, n):
    step = (end - start) / n

    current = start
    rsf = 0
    while (current < end):
        rsf += trapMethod(current, current + step)
        current += step
    return rsf


'''Simpsons Methods'''


def simpsonRule(a, b):
    h = (b - a) / 2
    x0 = a
    x2 = b
    x1 = a + h
    return (h / 3) * (math.sin(x0) + 4 * math.sin(x1) + math.sin(x2))


def compSimpsonRule(start, end, n):
    step = (end - start) / n

    current = start
    rsf = 0
    while (current < end):
        rsf += simpsonRule(current, current + step)
        current += step
    return rsf


'''3/8ths Rules'''


def threeEighthsRule(a, b):
    h = (b - a) / 3
    xArray = listGen(a, b, h)
   # print(xArray)
    return ((3 * h) / 8) * (
            math.sin(xArray[0]) + 3 * math.sin(xArray[1]) + 3 * math.sin(xArray[2]) + math.sin(xArray[3]))


def compThreeEightsRule(start, end, n):
    step = (end - start) / n

    current = start
    rsf = 0
    while (current < end):
        rsf += threeEighthsRule(current, current + step)
        current += step
    return rsf
compThreeEightsRule(.5,1.5,16)

'''Closed Newton-Cotes, n=4 Methods'''


def nIs4NCForm(a, b):
    h = (b - a) / 4
    xArray = listGen(a, b, h)
    return ((2 * h) / 45) * (
            7 * math.sin(xArray[0]) + 32 * math.sin(xArray[1]) + 12 * math.sin(xArray[2]) + 32 * math.sin(
        xArray[3] + 7 * math.sin(xArray[4])))


def compnIs4NCForm(start, end, n):
    step = (end - start) / n

    current = start
    rsf = 0
    while (current < end):
        rsf += nIs4NCForm(current, current + step)
        current += step
    return rsf


'''Midpoint Rule Methods'''


def midpointRule(a, b):
    n = 0
    h = (b - a) / (n + 2)
    xArray = listGen(a, b, h)
    return 2 * h * math.sin(xArray[1])


def compMidpointRule(start, end, n):
    step = (end - start) / n

    current = start
    rsf = 0
    while (current < end):
        rsf += midpointRule(current, current + step)
        current += step
    return rsf


'''Open Newton-Cotes Formula, n=1 methods'''


def nis1OpenNCForm(a, b):
    n = 1
    h = (b - a) / (n + 2)
    xArray = listGen(a, b, h)
    return ((3 * h) / 2)*(math.sin(xArray[0]) + math.sin(xArray[1]))


def compNis1OpenNCForm(start, end, n):
    step = (end - start) / n

    current = start
    rsf = 0
    while (current < end):
        rsf += nis1OpenNCForm(current, current + step)
        current += step
    return rsf


'''Open Newton-Cotes,n=2'''


def nis2OpenNCForm(a, b):
    n = 2
    h = (b - a) / (n + 2)
    xArray = listGen(a, b, h)
    return ((4 * h) / 3) * (2 * sin(xArray[1]) - sin(xArray[2]) + 2 * sin(xArray[3]))


def compNis2OpenNCForm(start, end, n):
    step = (end - start) / n

    current = start
    rsf = 0
    while (current < end):
        rsf += nis2OpenNCForm(current, current + step)
        current += step
    return rsf


'''Open Newton-Cotes, n=3'''


def nis3OpenNCForm(a, b):
    n = 3
    h = (b - a) / (n + 2)
    xArray = listGen(a, b, h)  # Has interesting rounding issue in xArray[3]
    return ((5 * h) / 24) * (11 * sin(xArray[1]) + sin(xArray[2]) + sin(xArray[3]) + 11 * sin(xArray[4]))


def compNis3OpenNCForm(start, end, n):
    step = (end - start) / n

    current = start
    rsf = 0
    while (current < end):
        rsf += nis3OpenNCForm(current, current + step)
        current += step
    return rsf


def absoluteError(approx, exact):
    return approx-exact;

def relativeError(approx, exact):
    return (abs(approx-exact))/exact;

def myPrint(name,approx):
    #Should print out the name, approx value abs, rel erros
    print(name)
    absError = absoluteError(approx,exact)
    relError = relativeError(approx,exact)
    print(" Approximate Val: {} | Abs Err: {} | Rel Err: {}".format(approx, absError, relError))

def squareArrayGen(length):
    arr=[];
    for i in range(0,length):
        arr.append(pow(2,i))
    return arr
def main():
    start=.5
    end=1.5
    stepArray = squareArrayGen(4)
    for stepNumber in stepArray:
        print()
        print("-------------------------------------------------------------------------------------------------------")
        print("Number of Steps  'N' = " + str(stepNumber))
        myPrint("Composite Trapezoid Rule",compTrapRule(start,end,stepNumber))
        myPrint("Composite Simpson's Rule",compSimpsonRule(start,end,stepNumber))
        if(stepNumber>=4):
            myPrint("Composite 3/8ths Rule",compThreeEightsRule(start,end,stepNumber))
        myPrint("Composite, Closed Newton-Cotes Form where n=4",compnIs4NCForm(start,end,stepNumber))
        myPrint("Composite Midpoint Rule",compMidpointRule(start,end,stepNumber))
        myPrint("Composite, Open Newton-Cotes Form where n=1",compNis1OpenNCForm(start,end,stepNumber))
        myPrint("Composite, Open Newton-Cotes Form where n-2",compNis2OpenNCForm(start,end,stepNumber))
        myPrint("Composite, Open Newton-Cotes Form where n=3",compNis3OpenNCForm(start,end,stepNumber))




main()

# TODO: WTF is up with compThreeEigths rule and the general 3/8ths rule?

#compThreeEightsRule(.5,1.5,10)
def adaptiveQuad(a, b ,sum):
    notGoodEnough = True
    # resultSoFar = simpsonRule(a, b)
    half = ((a + b) / 2)
    '''
    while (notGoodEnough):
        # resultSoFar = resultSoFar - simpsonRule(a, ((a + b) / 2)) + simpsonRule( ((a + b ) / 2), b)
        return (adaptiveQuad(a, half) + adaptiveQuad(half, b))
        print(resultSoFar)
        if (abs(resultSoFar - exact) < .1):
            notGoodEnough = False;
    return resultSoFar;
    '''

    '''
    if(recursive call is in range)
        return the value of the recursive call
    else
        recursive call of simpsonRule(a,half) + simpsonRule(half,b)
    '''




'''
def closedNewtonCotesForm(a,b,n):
    #n= number of intervals desired
    xArray=[]

    h=(b-a)/n #Step Size
    k=a
    while(k<=b):
        xArray.append(k)
        k=k+h
    print(xArray)


    for i in range(0,n+1):
        rsf=1
        for j in range(0,i):
            if(xArray[i]!=xArray[j]):
                rsf=xArray[i]



closedNewtonCotesForm(0,4,4);
'''
