import os
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from DataLoader import LoadData

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 12
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'


Headers, Data = LoadData('Data/Mid_Data_Final_veg_curv.csv')

Data['width']

widths = []
path = '/home/sgrieve/Hollow_Paper_Plotting/field_data/HIF_2014/'
# Parse the widths from the HIF files
for filename in os.listdir(path):
    with open(path + filename) as f:
        data = f.readlines()
        width = 0
        for d in data:
            if 'NR_WIDTH' in d:
                try:
                    width += float(d.split()[1])
                except:
                    pass
            elif 'NL_WIDTH' in d:
                try:
                    width += float(d.split()[1])
                except:
                    pass
        widths.append(width)

widths = [w for w in widths if w > 0]

tmp = [w for w in Data['width'] if w > 24.]
vals = []
a = np.array(sorted(widths))

for i in xrange(1000000):
    b = np.array(sorted(np.random.choice(tmp, len(widths))))

    # DEM - Field -ve value == field data is an over-estimate
    c = b - a

    vals.append(np.mean(np.abs(c)))

y, binEdges = np.histogram(vals, bins=100, density=True)
bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
plt.plot(bincenters, y, 'k')

med = np.median(vals)
plt.vlines(med, 0., 1., 'r', '--', label='Median = {0} m'.format(round(med, 2)))
plt.ylim(0, np.max(y))

plt.ylabel('Probability Density\n', fontsize=14)
plt.xlabel('Absolute error (m)', fontsize=14)
plt.tick_params(axis='both', which='both', top='off', right='off')
plt.xlim(0, 15)
plt.ylim(0, 0.38)

legend = plt.legend(fontsize=14, loc=0)
legend.get_frame().set_linewidth(0.)

plt.tight_layout()

plt.savefig('Final_Plots/field_comparison.pdf')
