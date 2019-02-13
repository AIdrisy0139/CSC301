import math;


#TODO: Make tabulating/graphing function
def main():
    X = [(1/32),(1/16),(1/8),(1/4),(1/2),1,2,4]
    N = (1,2,4,8,16,32,64,128,256)
    NAME = ["sin", "cos","exp","ln"]
    for name in NAME:
        runner(X,N, name);

def runner(X,N, name):
    print("---------------------------------------------------------------------------------------")
    print();
    print("FUNCTION: " + name);
    for x in X:
        for n in N:
           # print("x = " + str(x) + "  n = " +str(n), end="")
            if(name == "sin"):
                esValue = (sigma(x,n,name));
                absError = (esValue -math.sin(x))
                relError = absError / math.sin(x);
                print("x = {:<8}  n = {:<5}  | Taylor Sine {:<24} Exact Sine {:<24}  | Abs Error {:<32} Rel Error{:<32}".format(x,n,esValue, math.sin(x), absError,relError))
            else:
                print("else");





def sigma(x, n, name):
    sum =0;
    for k in range(0, n+1):
        if(name=="sin"):
            sum+= ((pow(-1,k) / math.factorial(2*k+1)) * pow(x, 2*k+1))
        elif(name=="cos"):
            sum+=((pow(-1,k) / math.factorial(2*k)) * pow(x, 2*k))
        elif(name=="exp"):
            sum+=(pow(x, k) / math.factorial(k))
        elif(name=="ln"):
            if(x<1):
                sum+=-( math.pow(x,n)/n);
    return sum;

def kthDerivativeSIN(k):

    if((k%4)==0):
        return 0;
    elif((k%4==1)):
        return 1
    elif((k%4)==2):
        return 0
    elif((k%4)==3):
        return -1;


def kthDerivativeCOS(k):
    if((k%4)==0):
        return 1;
    elif((k%4==1)):
        return 0
    elif((k%4)==2):
        return -1
    elif((k%4)==3):
        return 0

def kthDerivativeEXP(k):
    return 1;


main();







