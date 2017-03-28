data1 = "DataSet.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
data = readData(data1)

hasil = []
hasil2 = []
angka = []
titik = False
for i in data:
        x = i

        if x.isdigit():
                angka.append(x)
                hasil.append('w')
        else:
                if titik == True :
                        y = x[0].upper() + x[1:]
                        titik = False
                        hasil.append(y)
                else:
                        hasil.append(x)
                if x.endswith('.'):
                        titik = True
angka.reverse()
y=0
for i in hasil :
        if i == 'w':
                hasil2.append(angka[y])
                y+=1
        else :
                hasil2.append(i)

hasil2 = ' '.join(hasil2)

print(hasil2)
