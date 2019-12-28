import sys

with open("result.txt") as f:
    data = f.readlines()
    stringdata = ' '.join([line.rstrip() for line in data])
    stringdata = stringdata.replace(" ","")

stringdata = list(stringdata)
realdata = [int(i) for i in stringdata]
TestScore = [0,0,0,0,0,0,0,0]

def rowTest(realdata): 
    i = 0
    k =0
    n = len(realdata)
    for a in range(n//3):
        if((realdata[i] + realdata[i+1]+ realdata[i+2]) == 15):
            i +=3     
            if(i==6 or i ==15 or i == 24 or i ==33  or i==42 or i==51 or i==60 or i == 69):
                TestScore[k] +=25 
                k+=1
                if(i ==69):
                    break          
        else:
            print("Row Test False")


def columnTest(realdata):
    i = 0
    n = len(realdata)
    k=0
    for a in range(n//3):
        if((realdata[i] + realdata[i+3]+ realdata[i+6]) == 15):
            i +=1
            if(i==2 or i ==11 or i == 20 or i == 29 or i==38 or i==47 or i==56):
                i +=7
                TestScore[k] +=25 
                k+=1
            if(i == 65):
                TestScore[7] +=25
                break
        else:
            print("false")
        


def digonalTest(realdata):
    i = 0
    k = 0
    n = len(realdata)
    for a in range(n//3):
        if((realdata[i] + realdata[i+4]+ realdata[i+8]) == 15):
            i +=2
            if((realdata[i] + realdata[i+2]+ realdata[i+4])== 15):
                if(i <= 56):
                    TestScore[k] +=25
                    k +=1
                    i +=7
                    continue
                if(i==65):
                    TestScore[7] +=25
                    break
            else:
                print("Digonal test false")    
        else:
            print("Digonal test false")


def overlapTest(realdata):
    i=0
    k=0
    sum=0
    n = len(realdata)
    for a in range(n//8):
        sum=0
        if(i==71):
            break
        for b in range(9):
            sum += realdata[i]
            if(i==8 or i ==17 or i == 26 or i == 35 or i==44 or i==53 or i==62):
                if(sum ==45):
                    
                    TestScore[k] +=25
                    k+=1
                else:
                    print("Overlap Test False")
            if(i==71):
                TestScore[7] +=25
                break
                
            i += 1
            
rowTest(realdata)
columnTest(realdata)
digonalTest(realdata)
overlapTest(realdata)

for a in TestScore:
    k=0
    if(TestScore[k] !=100):
        print("TEST FALSE")
    else:
        print("TEST TRUE!!")
    