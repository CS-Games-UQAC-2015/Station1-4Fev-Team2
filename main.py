f = open('A-small-practice.in', 'r')
T = int(f.readline()) #number of case
N = 0
L = 0

for i in range(T):
    tmp = f.readline()
    tmp = tmp.split()
    N[i] = int(tmp[0])
    L[i] = int(tmp[1])