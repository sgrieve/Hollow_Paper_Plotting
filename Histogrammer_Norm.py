import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from DataLoader import LoadData

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 10
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'

sub_label = [''] + list(string.ascii_lowercase)[:6]
color = ['r', 'k', 'b']
Labels = ['Lower bound', 'Middle bound', 'Upper bound']

Headers, MidData = LoadData('Data/Mid_Data_Final_veg_curv.csv')
_, LowData = LoadData('Data/Low_Data_Final_veg_curv.csv')
_, HiData = LoadData('Data/Hi_Data_Final_veg_curv.csv')
Landscape = np.fromfile('Data/Landscape_Aspects.txt', sep=' ')

ax = plt.subplot(3, 1, 1)
plt.tick_params(axis='both', which='both', top='off', right='off')
for i, d in enumerate([LowData, MidData, HiData]):

    y, binEdges = np.histogram(d['Aspect'], bins=100, density=True)
    bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
    plt.plot(bincenters, y, color[i], label=Labels[i])

plt.ylabel('Probability Density', color='w')
legend = plt.legend()
legend.get_frame().set_linewidth(0.)
plt.xlim(0, 360)
ax.locator_params(tight=True, nbins=4)

plt.annotate(sub_label[1], xy=(0.0075, 0.97),
             xycoords='axes fraction', fontsize=12,
             horizontalalignment='left', verticalalignment='top')

ax = plt.subplot(3, 1, 2)
plt.tick_params(axis='both', which='both', top='off', right='off')
y, binEdges = np.histogram(Landscape, bins=100, density=True)
bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
plt.plot(bincenters, y, 'k', label='Landscape Aspect')

plt.ylabel('Probability Density\n')
legend = plt.legend()
legend.get_frame().set_linewidth(0.)
plt.xlim(0, 360)
ax.locator_params(tight=True, nbins=4)

plt.annotate(sub_label[2], xy=(0.0075, 0.97),
             xycoords='axes fraction', fontsize=12,
             horizontalalignment='left', verticalalignment='top')

ax = plt.subplot(3, 1, 3)
plt.tick_params(axis='both', which='both', top='off', right='off')
y, binEdges = np.histogram(MidData['Aspect'], bins=100, density=True)
y_land, binEdges = np.histogram(Landscape, bins=100, density=True)
bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
plt.plot(bincenters, y - y_land, 'k', label='Detrended Aspect')

plt.hlines(0, 0, 360, linestyles='dashed', linewidth=2.)
plt.xlim(0, 360)

ax.locator_params(tight=True, nbins=4)

plt.annotate(sub_label[3], xy=(0.0075, 0.97),
             xycoords='axes fraction', fontsize=12,
             horizontalalignment='left', verticalalignment='top')

legend = plt.legend()
legend.get_frame().set_linewidth(0.)
plt.ylabel('Probability Density', color='w')
plt.xlabel('Aspect ($^\circ$)')

plt.tight_layout()

plt.savefig('Final_Plots/Normed_Hist_3_Panel.pdf')
