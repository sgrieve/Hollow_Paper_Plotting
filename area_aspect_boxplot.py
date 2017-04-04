import numpy as np
import matplotlib.pyplot as plt
from DataLoader import LoadData
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 14
rcParams['boxplot.medianprops.color'] = 'r'

Headers, Data = LoadData('Data/Mid_Data_Final_veg_curv.csv')

color = ['r', 'g', 'b']
labels = ['Area ($m^{2}$)', 'Aspect ($^\circ$)']

plt.ylabel(labels[0])
plt.xlabel(labels[1])

low = 0.
high = 10.

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
l = []
m = []
n = []
o = []
p = []
q = []
r = []

for asp, are in zip(Data['Aspect'], Data['Area']):
    if (asp > 0) and (asp <= 20):
        a.append(are)
    elif (asp > 20) and (asp <= 40):
        b.append(are)
    elif (asp > 40) and (asp <= 60):
        c.append(are)
    elif (asp > 60) and (asp <= 80):
        d.append(are)
    elif (asp > 80) and (asp <= 100):
        e.append(are)
    elif (asp > 100) and (asp <= 120):
        f.append(are)
    elif (asp > 120) and (asp <= 140):
        g.append(are)
    elif (asp > 140) and (asp <= 160):
        h.append(are)
    elif (asp > 160) and (asp <= 180):
        i.append(are)
    elif (asp > 180) and (asp <= 200):
        j.append(are)
    elif (asp > 200) and (asp <= 220):
        k.append(are)
    elif (asp > 220) and (asp <= 240):
        l.append(are)
    elif (asp > 240) and (asp <= 260):
        m.append(are)
    elif (asp > 260) and (asp <= 280):
        n.append(are)
    elif (asp > 280) and (asp <= 300):
        o.append(are)
    elif (asp > 300) and (asp <= 320):
        p.append(are)
    elif (asp > 320) and (asp <= 340):
        q.append(are)
    elif (asp > 340) and (asp <= 360):
        r.append(are)

binned = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r]


plt.boxplot(binned, whis=1., sym='+', )

ax = plt.gca()

ax.locator_params(tight=True, nbins=6)
labels = [item.get_text() for item in ax.get_xticklabels()]
labels = ax.get_xticks().tolist()
labels = [(int(l) * 20) - 10 for l in labels]

ax.set_xticklabels(labels)

plt.tight_layout()

plt.savefig('Final_Plots/Area_Aspect_boxplot.pdf')
