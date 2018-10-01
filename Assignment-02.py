import time;

import math


def naiveAlgo(n):

    print("N= 10^" + str(math.log10(n)));
    startTime = time.time();

    partialSum=0;
    for i in range(0,n):
        partialSum = math.pi+partialSum;
        partialSum = math.e + partialSum;
    endTime = time.time();

    exactSum = (n*math.pi)+(n*math.e);
    print("Exact Sum: " + str(exactSum));
    absError = abs(exactSum-partialSum);
    print("Absolute Error: " + str(absError));
    relError = absError/exactSum;
    print("Relative Error: " + str(relError));
    elapsedTime =  endTime-startTime;
    print("Elapsed time for summations: " + str(elapsedTime));
    print("---------------------------------------------------------------------------");


def compSumAlgo(n):

    print("N= 10^" + str(math.log10(n)));
    sum = 0;
    carry = 0;
    carryE = 0;
    startTime = time.time();
    for i in range(0,n):
        #Addition of Pi
        adjustedInput = math.pi - carry;
        tmpSum = sum+adjustedInput;
        carry = (tmpSum-sum)-adjustedInput;

        sum=tmpSum;

        #Addition of e
        adjustedInputE = math.e - carryE;
        tmpSumE = sum+adjustedInputE;
        carryE = (tmpSumE - sum) - adjustedInputE;
        sum = tmpSumE;

    endTime = time.time();
    elapsedTime = endTime - startTime;
    exactSum = (n * math.pi) + (n * math.e);
    print("Exact Sum: " + str(exactSum));
    absError = abs(exactSum - sum);
    print("Absolute Error: " + str(absError));
    relError = absError / exactSum;
    print("Relative Error: " + str(relError));
    elapsedTime = endTime - startTime;
    print("Elapsed time for summations: " + str(elapsedTime));
    print("---------------------------------------------------------------------------");

def runAlgos():

    size = [10**6,10**7,10**8];
    for x in size:
        print("NAIVE ALGO: ");
        naiveAlgo(x);
        print("COMPENSATED ALGO:  ");
        compSumAlgo(x);



runAlgos();
