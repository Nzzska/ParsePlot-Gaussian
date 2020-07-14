#Programa skirta isrinkti informacija apie suzadinatas busenas is Gaussian ".log" failu
import os
import numpy as np
import matplotlib.pyplot as plt
#################################
base=list()
e1=list()
e2=list()
e3=list()
osc1=list()
osc2=list()
osc3=list()
#################################
def ParseLogs(fdir):
    for filename in os.listdir(fdir):
        if filename.endswith('.log'):
            with open(os.path.join(fdir,filename)) as fhandle:
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
                        osc1.append(osc[1])
                    if lines.startswith(' Excited State   2'):
                        lines.strip()
                        words=lines.split()
                        e2.append(words[4])
                        osc=words[8].split('=')
                        osc2.append(osc[1])
                    if lines.startswith(' Excited State   3'):
                        lines.strip()
                        words=lines.split()
                        e3.append(words[4])
                        osc=words[8].split('=')
                        osc3.append(osc[1])
    baseline=min(base)
    for x in range(0,len(base)) :
        base[x]=base[x]-baseline
        e1[x]=float(e1[x])+base[x]
        e2[x]=float(e2[x])+base[x]
        e3[x]=float(e3[x])+base[x]
        osc1[x]=float(osc1[x])
        osc2[x]=float(osc2[x])
        osc3[x]=float(osc3[x])
    return base, e1, e2, e3, osc1, osc2, osc3

def eplot(base, e1, e2, e3, osc1, osc2, osc3):
    deg = np.arange(0.0, 375.0, 15.0)
    #figure 1
    plt.figure(1)
    plt.plot(deg, base, label='ground state')
    plt.plot(deg, e1, label='excited state 1')
    plt.plot(deg, e2, label ='excited state 2')
    plt.plot(deg, e3, label='excited state 3')
    legend=plt.legend()
    plt.xlabel('Dehydral angle (deg)')
    plt.ylabel('Energy (eV)')
    plt.title('Excited states')
    plt.grid(True)
    plt.savefig("ExcitedStates.png")
    #figure 2
    plt.figure(2)
    plt.plot(deg, osc1, label='orciliator 1')
    plt.plot(deg, osc2, label='orciliator 2')
    plt.plot(deg, osc3, label='orciliator 3')
    legend=plt.legend()
    plt.xlabel('Dehydral angle (deg)')
    plt.ylabel('Oscilliator strength ')
    plt.title('Oscilliator strength')
    plt.grid(True)
    plt.savefig("Oscilliatoriai.png")
    return 0
#################################
#DATA PARSING
filedir = input('iveskite direktorija: ')
(base, e1, e2, e3, osc1, osc2, osc3)=ParseLogs(filedir)
#DATA PLOTTING
eplot(base, e1, e2, e3, osc1, osc2, osc3)
