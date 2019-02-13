# Arikuzzaman Idrisy
# CSC 301 Numerical Analysis Assignment 06

import math

initVel = 0
initPos = -math.pi/4
g = 32.17

halfStepSize = 1;
timeArray=0;
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

def Force(pos):
    print("Force Function")
    return -g*sin(pos)

def Velocity(time):
    print("Velocity Function")
    global timeArray
    if(time<=0):
        return 0
    else:
        return Velocity(timeArray[time-halfStepSize]) + Force(Position(time))*halfStepSize
def Position(time):
    print("Position Function")
    global timeArray
    if(time<=0):
        return -math.pi/4
    else:
       # print("index" +str(time-halfStepSize))
        print(timeArray[time-halfStepSize])
        return Position(timeArray[time-halfStepSize]) + Velocity(timeArray[time+halfStepSize])*2*halfStepSize

def nextVelocity(vT,xT,time):
    return vT+Force(xT)*halfStepSize

def nextPosition(xT,vT,time):
    return xT + vT*2*halfStepSize
def main():
    # halfStepSize = 1;
    global timeArray
    halfStepCount = 10
    timeArray = listGen(0,halfStepCount,halfStepSize)
    #print(timeArray)
    # Each element in this array actually represents a half step. So time Array is an Array of half steps
    posArray =[initPos]
    velArray = [0]
    forceArray= [Force(initPos)]
    # print(Position(timeArray[1]))#-Position(timeArray[0]))
    # print(Velocity(timeArray[1]))
    
    for i in range(1,len(timeArray)):
        prevInd = i-halfStepSize
        print(prevInd)

        velArray.append(nextVelocity(velArray[prevInd],posArray[prevInd],i))
        print(posArray[prevInd],velArray[i])
        posArray.append(nextPosition(posArray[prevInd],velArray[i],i))
        velArray.append((nextVelocity(velArray[i],posArray[i],i)))#i+1 element of velArray
        '''
        if(i==1):
            velArray.append(nextVelocity(velArray[prevInd],posArray[prevInd],i))
            posArray.append(nextPosition(posArray[prevInd],velArray[i],i))
            velArray.append(nextVelocity(velArray[i],posArray[i],i))
        
        else:
            #velArray.append(nextVelocity(velArray[prevInd],posArray[prevInd-1],i))
            posArray.append(nextPosition(posArray[prevInd-1],velArray[i],i))
            velArray.append(nextVelocity(velArray[i],posArray[prevInd],i))
            '''
            
        #posArray.append(nextPosition(posArray[i],velArray[i+1],i))
        '''
        posArray.append(Position(i))
        print("PosArray: " + str(posArray[i]))
        velArray.append(Velocity(i))
        print("VelArray: " + str(velArray[i]))
        forceArray.append(Force(i))
        print(forceArray[i])
        '''
    
    print(posArray)
    # print(velArray)
    #print(forceArray)

    # initForce = Force(Position(0))





main()
