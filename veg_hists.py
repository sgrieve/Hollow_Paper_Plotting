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

colors = ['r', 'g', 'b', 'k']

Headers, Data = LoadData('Data/Mid_Data_Final_veg_curv.csv')

sub_label = [''] + list(string.ascii_lowercase)[:4]

# 'ID', 'Area', 'Slope', 'Aspect', 'X', 'Y', 'Curvature', 'PlanCurvature', 'Length', 'Area_Length_Ratio', 'Axis_Slope', 'Min_Elevation', 'Max_Elevation', 'Relief', 'Veg', 'Curv_pc', 'Plan_Curv_pc')

counts = [342., 26., 552., 133.]

headers = ['Area', 'Slope', 'Aspect', 'Curv_pc']
x_labels = ['Area ($m$)', 'Slope ($m/m$)', 'Aspect ($^\circ$)',
            'Percent concave pixels']
labels = ['Cove hardwood', 'Mixed deciduous', 'Xeric oak-pine',
          'Northern hardwood']

for plt_count in xrange(1, 5):
    a = []
    b = []
    c = []
    d = []

    plt.subplot(2, 2, plt_count)

    for param, v in zip(Data[headers[plt_count - 1]], Data['Veg']):
        if v == 1:
            a.append(param)
        elif v == 2:
            b.append(param)
        elif v == 3:
            c.append(param)
        elif v == 4:
            d.append(param)

    subsets = [a, b, c, d]

    for i in xrange(4):

        y, binEdges = np.histogram(subsets[i], bins=20, density=False)
        bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])

        # This block is removing empty bins to make better looking curves.
        y3 = [(i_, j_) for i_, j_ in enumerate(y) if j_ > 0]
        bincenters = np.array([bincenters[q[0]] for q in y3])
        y = np.array([q[1] for q in y3])

        plt.plot(bincenters, y / counts[i], colors[i], label=labels[i])

    if (plt_count == 1):
        legend = plt.legend(fontsize=10, loc=9)
        legend.get_frame().set_linewidth(0.)

        #fake ylabel to pad plot properly
        plt.ylabel('Probability Density\n', fontsize=12, color='w')

    plt.annotate(sub_label[plt_count], xy=(0.95, 0.97),
                 xycoords='axes fraction', fontsize=12,
                 horizontalalignment='left', verticalalignment='top')


    plt.xlabel(x_labels[plt_count - 1], fontsize=12)

fig = plt.gcf()

fig.text(0.03, 0.5, 'Probability Density', fontsize=12, va='center',
         rotation='vertical')


plt.tight_layout()

plt.savefig('Final_Plots/veg_hist.pdf')
