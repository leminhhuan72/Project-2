import opensimplex
import sys
import random

wh = 128
t = [[0]*wh for i in range(wh)]

opensimplex.random_seed()

differentRegion = []

for i in range (1,wh-1):
    for j in range (1,wh-1):
        v = opensimplex.noise2(i*0.0625,j*0.0625)
        v = v if v > 0 else v * -1
        t[i][j] = round(v*10)
        if t[i][j] not in differentRegion:
            differentRegion.append(t[i][j])

print(differentRegion)

Tx = round(random.uniform(1,wh-2))
Ty = round(random.uniform(1,wh-2))
while(t[Tx][Ty]==0):
    Tx = round(random.uniform(1,wh-2))
    Ty = round(random.uniform(1,wh-2))



# for i in range (wh):
#     for j in range (wh):
#         pr = random.random()*100
#         if  pr > 99 and t[i][j] != 0 and i!=Tx and j!=Ty:
#             t[i][j] = str(t[i][j])+'P'
#             #print(pr)

# opensimplex.random_seed()

for i in range(wh):
    for j in range(wh):
        m = opensimplex.noise2(i*0.0625,j*0.0625)
        m = m if m > 0 else m * -1
        if m*10 > 9 and t[i][j]!=0 and i!=Tx and j!=Ty:
            t[i][j] = str(t[i][j])+'M'
    
Px = round(random.uniform(1,wh-2))
Py = round(random.uniform(1,wh-2))
prison_no = random.randint(4,round(wh / 4))
while(prison_no!=0):
    if t[Px][Py]!=0 and Px!=Tx and Py!=Ty and len(str(t[Px][Py]))==1:
        t[Px][Py] = str(t[Px][Py])+'P'
        prison_no -= 1
    Px = round(random.uniform(1,wh-2))
    Py = round(random.uniform(1,wh-2))

r = random.randint(2,5)
release = r + 2


print('\n'.join([';'.join([str(cell) for cell in row]) for row in t]))

original_stdout = sys.stdout # Save a reference to the original standard output

output_name = 'MAP'+str(wh)+'.txt'
with open(output_name, 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(f'{wh} {wh}')
    print(f'{r}\n{release}')
    print(f'{len(differentRegion)}')
    print(f'{Tx} {Ty}')
    print('\n'.join([';'.join([str(cell) for cell in row]) for row in t]))
    sys.stdout = original_stdout # Reset the standard output to its original value