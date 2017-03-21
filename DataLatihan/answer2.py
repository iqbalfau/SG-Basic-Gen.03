data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
        x = []
        with open(data1) as data :
            for line in data :
                    x = line.split()
        return x

a = readData(data1)
b = readData(data2) 
c = []
for i in a :
        
        count = 0
        for x in b:
                if (i == x): 
                        count += 1
        for y in c:
                if (y == i):
                        count=0
        if (count!=0):
                c.append(i)        
        
c = ' '.join(c)

print(c) 
