import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 12
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'

full_data = [1, 20, 18, 1, 1, 17, 21, 20, 23, 22, 17, 1, 18, 45, 15, 20, 23, 21, 19, 20, 15, 19, 22, 5, 16, 20, 17, 16, 19, 20, 17, 18, 15, 19, 18, 19, 23, 18, 19, 22, 1, 16, 20, 19, 19, 1, 1, 8, 19, 20, 19, 23, 1, 1, 20, 16, 17, 18, 18, 17, 17, 17, 18, 17, 21, 21, 11, 21, 17, 20, 18, 19, 20, 1, 20, 22, 16, 1, 19, 1, 24, 18, 1, 13, 18, 1, 20, 1, 20, 18, 1, 17, 18, 1, 19, 17, 18, 20, 17, 17, 11, 19, 15, 1, 1, 20, 18, 1, 18, 16, 15, 17, 19, 12, 19, 17, 22, 19, 17, 1, 16, 17, 18, 26, 1, 1, 17, 17, 24, 1, 20, 17, 20, 21, 22, 17, 13, 19, 19, 19, 21, 14, 20, 17, 17, 1, 18, 18, 20, 1, 24, 25, 17, 17, 19, 17, 20, 17, 16, 20, 19, 16, 21, 22, 16, 1, 3, 17, 19, 18, 16, 1, 19, 18, 18, 15, 16, 17, 21, 16, 17, 15, 18, 23, 19, 4, 18, 14, 22, 22, 17, 10, 1, 1, 17, 1, 18, 20, 16, 20, 21, 20, 15, 23, 17, 19, 22, 14, 24, 14, 17, 15, 21, 17, 1, 19, 17, 1, 19, 15, 14, 15, 13, 15, 16, 19, 13, 16, 19, 19, 1, 1, 18, 17, 17, 20, 18, 13, 21, 20, 15, 11, 15, 19, 15, 22, 9, 5, 1, 22, 28, 18, 20, 15, 15, 16, 29, 21, 18, 14, 16, 18, 16, 17, 13, 20, 20, 18, 17, 19, 7, 20, 14, 27, 7, 20, 18, 18, 22, 17, 17, 14, 16, 19, 5, 49, 21, 17, 15, 1, 20, 20, 15, 18, 18, 19, 22, 18, 19, 20, 4, 16, 17, 17, 21, 17, 14, 21, 17, 24, 17, 16, 19, 18, 15, 1, 19, 17, 19, 16, 19, 20, 13, 19, 20, 17, 22, 19, 1, 18, 17, 17, 15, 1, 16, 16, 19, 21, 18, 21, 18, 21, 21, 1, 20, 18, 21, 5, 15, 1, 19, 19, 1, 19, 17, 1, 1, 1, 19, 17, 21, 22, 19, 15, 18, 15, 19, 20, 18, 19, 17, 15, 19, 17, 13, 20, 17, 20, 17, 19, 19, 1, 15, 17, 17, 22, 19, 1, 1, 17, 17, 1, 1, 10, 17, 21, 9, 21, 1, 1, 20, 20, 1, 17, 5, 1, 5, 15, 18, 12, 21, 22, 21, 1, 21, 17, 18, 19, 16, 19, 17, 17, 15, 14, 1, 19, 1, 17, 1, 1, 20, 3, 16, 20, 16, 18, 17, 15, 13, 19, 20, 22, 1, 18, 19, 18, 21, 18, 17, 23, 16, 18, 15, 16, 20, 17, 15, 19, 1, 1, 20, 19, 15, 18, 19, 17, 17, 16, 1, 21, 19, 17, 20, 21, 21, 18, 20, 1, 17, 22, 23, 1, 14, 18, 23, 14, 16, 18, 17, 20, 14, 19, 18, 16, 4, 1, 14, 1, 15, 1, 19, 19, 18, 18, 15, 15, 1, 21, 15, 19, 20, 21, 1, 17, 15, 17, 23, 17, 18, 3, 15, 16, 16, 1, 15, 19, 18, 17, 22, 18, 17, 5, 17, 15, 19, 15, 4, 15, 17, 21, 15, 1, 1, 14, 16, 16, 15, 18, 1, 19, 9, 16, 19, 12, 19, 17, 16, 19, 18, 17, 16, 18, 22, 20, 17, 17, 19, 16, 18, 21, 16, 1, 17, 17, 1, 15, 20, 18, 15, 1, 1, 17, 23, 16, 20, 11, 21, 17, 15, 20, 19, 21, 18, 1, 21, 20, 1, 1, 14, 19, 20, 5, 15, 20, 16, 16, 20, 18, 19, 24, 22, 20, 19, 18, 17, 15, 16, 19, 21, 19, 1, 8, 17, 16, 1, 1, 1, 22, 22, 20, 20, 18, 5, 18, 20, 24, 19, 1, 17, 20, 21, 23, 16, 21, 16, 13, 1, 16, 19, 16, 18, 17, 21, 15, 1, 21, 1, 1, 18, 1, 17, 1, 14, 18, 19, 18, 19, 21, 1, 21, 9, 1, 19, 15, 17, 16, 11, 17, 16, 21, 19, 21, 23, 16, 4, 20, 18, 17, 17, 19, 24, 19, 16, 1, 15, 24, 18, 21, 20, 13, 17, 19, 18, 18, 21, 20, 1, 16, 1, 20, 17, 12, 17, 10, 11, 15, 15, 17, 13, 19, 19, 21, 1, 3, 7, 17, 20, 16, 13, 11, 16, 18, 19, 23, 21, 49, 22, 16, 21, 19, 19, 17, 14, 5, 14, 16, 17, 19, 18, 11, 16, 21, 16, 1, 20, 23, 19, 1, 17, 14, 1, 17, 19, 20, 23, 19, 20, 1, 18, 18, 11, 15, 15, 19, 16, 20, 18, 18, 15, 15, 22, 17, 15, 17, 22, 20, 18, 16, 1, 1, 1, 22, 17, 18, 19, 20, 22, 13, 20, 1, 17, 16, 14, 1, 13, 17, 1, 13, 1, 17, 18, 18, 18, 15, 1, 1, 17, 22, 15, 19, 19, 21, 20, 19, 18, 22, 17, 9, 1, 15, 1, 1, 17, 11, 1, 17, 17, 19, 22, 17, 18, 16, 17, 22, 1, 17, 20, 1, 15, 1, 17, 11, 15, 21, 26, 18, 29, 18, 1, 19, 21, 23, 3, 15, 18, 14, 23, 19, 24, 19, 21, 18, 21, 16, 17, 21, 21, 24, 5, 22, 1, 9, 21, 20, 20, 1, 17, 24, 1, 18, 19, 20, 19, 15, 19, 1, 19, 19, 5, 9, 15, 5, 22, 20, 13, 17, 1, 1, 17, 18, 1, 16, 21, 19, 3, 22, 17, 22, 18, 19, 17, 16, 14, 1, 19, 21, 28, 23, 24, 1, 15, 13, 16, 20, 16, 18, 18, 1, 16, 9, 11, 1, 19, 16, 18, 19, 11, 25, 23, 1, 16, 22, 18, 19, 17, 19, 19, 20, 1, 21, 23, 23, 1, 7, 18, 15, 1, 3, 16, 17, 20, 16, 1, 18, 17, 1, 19, 17, 13, 1, 16, 20, 19, 15, 19, 19, 16, 1, 15, 17, 1, 5, 17, 1, 1, 17, 18, 26, 19, 1, 1, 18, 21, 1, 15, 1, 21, 17, 1, 19, 17, 11, 1, 15, 5, 21, 17, 23, 1, 19, 5, 18, 1, 15, 16, 18, 1, 17, 18, 5, 17, 18, 1, 1, 21, 21, 9, 19, 21, 11, 19, 16, 49, 1, 13, 5, 15, 1, 1, 1]


y, binEdges = np.histogram(full_data, bins=20, density=True)
bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
plt.plot(bincenters, y, 'k')
plt.tick_params(axis='both', which='both', top='off', right='off')

med = 17
plt.vlines(med, 0., 1., 'r', '--', label='Median = {0}'.format(int(med)))
plt.ylim(0, np.max(y))

plt.ylabel('Probability Density\n', fontsize=14)
plt.xlabel('Number of Harmonics', fontsize=14)

legend = plt.legend(fontsize=14, loc=0)
legend.get_frame().set_linewidth(0.)

plt.tight_layout()

plt.savefig('Final_Plots/Harmonic_Hist.pdf')