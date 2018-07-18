#https://projecteuler.net/problem=630
s0 = 290797
cords = []
SlopeAndIntercepts = []
UniqueLines = []
total = 0
#calculate Sn+1
def calcSn(s,n):
    if n == 0:
        tn = (s % 2000) - 1000
        return tn
    else:
        t = (s * s) % 50515093
        return calcSn(t,n-1)
#calc Tn points
def calcTn(numPoints):
    temp=[]
    for a in range(1,numPoints * 2 + 1):
        t = calcSn(s0,a)
        if a % 2 == 0:
           temp.append(t)
           cords.append(temp)
           temp = []
        else:
            temp.append(t)

#calculate total number of lines
#all lines from one point to another
#this is M(L)
def allLines():
    total = 0
    for t in range(0,len(cords)-1):
        for s in range(t+1,len(cords)):
            if(t != s):
                total +=1
    return total
#I think if two lines have the same slope and intercept they are the same line? 
def equationLine(x1,y1,x2,y2):
    #print(str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2))
    temp = []
    #solve for m

    if(x1 != x2):
        m =float( float((y2 - y1)) / float((x2 - x1)))
    else:
        m =0
    b = y1 - (m * x1)
    
    #print("m = " + str(m) + ", b= " + str(b))
    temp.append(m)
    temp.append(b)
   # print(temp)
    SlopeAndIntercepts.append(temp)

#gets the m and b of all lines
def getEquations():
    for t in range(0,len(cords)-1):
        for s in range(t+1,len(cords)):
          # print(str(cords[t][0]) + "," + str(cords[t][1]) + "," + str(cords[s][0]) + "," + str(cords[s][1]))
            equationLine(cords[t][0],cords[t][1],cords[s][0],cords[s][1])

#gets the number of unique equations from getEquations
def uniqueEquations():
    total = allLines()
    remove = []
    for t in range(0,len(SlopeAndIntercepts)-1):
        for s in range(t+1,len(SlopeAndIntercepts)):
            if(SlopeAndIntercepts[t][0] == SlopeAndIntercepts[s][0] and SlopeAndIntercepts[t][1] == SlopeAndIntercepts[s][1]):
                remove.append(s)
                total -= 1


    
    global UniqueLines
    UniqueLines = [i for j, i in enumerate(SlopeAndIntercepts) if j not in remove]
    
    
def FindIntersections():
    right = 0;
    wrong = 0; 
    print("Lines: " +str(len(UniqueLines)))
    for a in range(0,len(UniqueLines)-1):
        for b in range(a+1,len(UniqueLines)):
            if(Calculateintersections(UniqueLines[a],UniqueLines[b])):
                right += 1
            else:
                wrong += 1
    print("Intersections:" + str(right*2) + "\nWrong: " + str(wrong))

def Calculateintersections(LineA,LineB):           
    m1 = LineA[0]
    b1 = LineA[1]
    m2 = LineB[0]
    b2 = LineB[1]

    if(m1 != m2):#parrelel
       # print("m1" + str(m1) + "m2" + str(m2))
        return True
    else:
        return False




def main():
    calcTn(100)
    getEquations()
    #print(SlopeAndIntercepts)
    uniqueEquations()
    FindIntersections()
main()
