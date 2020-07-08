#logs/turn0.log < Testuosim
#Ieskosime Excited State   1/2/3 Eiluciu 
#SCF Done:  E(RB3LYP) =  -2086.72472540 <- Nesuzadintos busenos energija
import os
import numpy as np
import matplotlib.pyplot as plt

base=list()
e1=list()
e2=list()
e3=list()
osc1=list()
osc2=list()
osc3=list()

#DATA PARSING

print("startas")

for filename in os.listdir('logs/'):
    if filename.endswith('.log'):
        with open(os.path.join('logs/',filename)) as fhandle:
            for lines in fhandle:
                if lines.startswith(' SCF Done:  E(RB3LYP) ='):
                    lines.strip()
                    words=lines.split()
                    energija=float(words[4]) * (-1) * 27.211386245988
                    base.append(energija)
                if lines.startswith(' Excited State   1'):
                    lines.strip()
                    words=lines.split()
                    e1.append(words[4])
                    osc=words[8].split('=')
                    osc1.append(osc)
                if lines.startswith(' Excited State   2'):
                    lines.strip()
                    words=lines.split()
                    e2.append(words[4])
                    osc=words[8].split('=')
                    osc2.append(osc)
                if lines.startswith(' Excited State   3'):
                    lines.strip()
                    words=lines.split()
                    e3.append(words[4])
                    osc=words[8].split('=')
                    osc3.append(osc)
baseline=min(base)
for x in range(0,len(base)) :
    base[x]=base[x]-baseline
    e1[x]=float(e1[x])+base[x]
    e2[x]=float(e2[x])+base[x]
    e3[x]=float(e3[x])+base[x]
    
#DATA PLOTTING

deg = np.arange(0.0, 375.0, 15.0)
fig, ax = plt.subplots()
ax.plot(deg, base, label='ground state')
ax.plot(deg, e1, label='excited state 1')
ax.plot(deg, e2, label ='excited state 2')
ax.plot(deg, e3, label='excited state 3')
legend=ax.legend()
plt.xlabel('Dehydral angle (deg)')
plt.ylabel('Energy (eV)')
plt.title('Excited states')
plt.grid(True)
plt.savefig("ExcitedStates.png")
plt.show()