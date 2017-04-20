import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from DataLoader import LoadData

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 12
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'


Headers, LowData = LoadData('Data/Low_Data_Final_veg_curv.csv')
_, MidData = LoadData('Data/Mid_Data_Final_veg_curv.csv')
_, HiData = LoadData('Data/Hi_Data_Final_veg_curv.csv')

sub_label = [''] + list(string.ascii_lowercase)[:6]
color = ['r', 'k', 'b']
Labels = ['Lower bound', 'Middle bound', 'Upper bound']
Units = ['($m^{2}$)', '($m/m$)', '($\%$)',
         '($m$)', '($m$)', '($m$)']

xmins = [0., 0., -0.08, -0.02, 0., 0.]


count = 1

for h, u in zip(Headers[1:3] + ('Curv_pc', 'width', 'Length', 'Relief', '')[:-1], Units):

    ax = plt.subplot(3, 2, count)
    plt.tick_params(axis='both', which='both', top='off', right='off')

    for i, d in enumerate([LowData, MidData, HiData]):

        y, binEdges = np.histogram(d[h], bins=100, density=True)
        bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
        plt.plot(bincenters, y, color[i], label=Labels[i])

    if (count == 3):
        plt.ylabel('Probability Density\n\n', fontsize=14)

    if (count == 4):
        plt.xlabel(('{0} {1}').format('Width', u), fontsize=14)
    elif (count == 3):
        plt.xlabel(('{0} {1}').format('Percentage concave area', u),
                   fontsize=14)
    else:
        plt.xlabel(('{0} {1}').format(h.replace('_', ' '), u), fontsize=14)

    if (count == 1):
        legend = plt.legend(fontsize=14, loc=9)
        legend.get_frame().set_linewidth(0.)

    plt.annotate(sub_label[count], xy=(0.95, 0.97),
                 xycoords='axes fraction', fontsize=16,
                 horizontalalignment='left', verticalalignment='top')

    ax.locator_params(tight=True, nbins=4)

    plt.xlim(xmin=xmins[count - 1])
    plt.ylim(ymin=0.)

    count += 1


def mm_to_inch(mm):
    return mm * 0.0393700787

fig = plt.gcf()

# set the size of the plot to be saved. These are the JGR sizes:
# quarter page = 95*115
# half page = 190*115 (horizontal) 95*230 (vertical)
# full page = 190*230
fig.set_size_inches(mm_to_inch(163 * 2), mm_to_inch(122 * 2))
plt.tight_layout()

plt.savefig('Final_Plots/6_Panel_Hist.pdf')
