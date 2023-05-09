from matplotlib import pyplot as plt

f = open('nup5_-arch_data.txt', "r")
a=[]
i=0
while True:
    line = f.readline()
    if not line:
        break
    if line.count("0") > 0:
        a.append(line)
        i=i+1
f.close
data = [0 for k in range(573)]
for i in range(len(a)):
    z=a[i].split("\t") #z-список элементов строки
    from_to=z[4].split("-")
    for k in range(int(from_to[0]),int(from_to[1]),1):
        data[k]+=float(z[2])
plt.plot(data)
plt.xlabel('Аминокислотная позиция')
plt.ylabel('Суммарный индекс β-арок')
plt.show()
