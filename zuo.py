import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag

dane = pd.read_csv("dane04.csv", delimiter=',', engine='python')

mrugniecia=dane["dwa"][:7552]
cyfranamonitorze=dane["szesc"]

czestProbkowania = 200
czas = int(len(mrugniecia)/czestProbkowania)
t = np.linspace(0, czas, czas * czestProbkowania)

przefiltrowany1= ag.pasmowozaporowy(mrugniecia, czestProbkowania, 49, 51)
przefiltrowany2= ag.pasmowoprzepustowy(przefiltrowany1, czestProbkowania, 1, 50)

mors= []

i=0

while i <len(mrugniecia):
    if mrugniecia[i] > 0.05:
        mors.append(cyfranamonitorze[i])
        i +=100
    else:
        i +=1

print(mors)
