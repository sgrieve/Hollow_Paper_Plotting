import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from DataLoader import LoadData
import string

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 12
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'

Headers, NData = LoadData('Data/Non_Escarpment_Data_width.csv')
_, EData = LoadData('Data/Escarpment_Data_width.csv')

params = ['Area', 'Slope', 'Curv_pc', 'width', 'Length', 'Relief']

ylabels = ['Area ($m^2$)', 'Slope ($m/m$)', 'Percentage concave ($\%$)',
           'Width ($m$)', 'Length ($m$)', 'Relief ($m$)']

sub_label = list(string.ascii_lowercase)[:6]

for n in range(6):

    ax = plt.subplot(3, 2, n + 1)

    plt.boxplot([NData[params[n]], EData[params[n]]], showfliers=False,
                whis=[10, 90])

    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[0] = 'Non Escarpment'
    labels[1] = 'Escarpment'

    ax.set_xticklabels(labels)

    plt.ylabel(ylabels[n])

    plt.annotate(sub_label[n], xy=(0.95, 0.97),
                 xycoords='axes fraction', fontsize=16,
                 horizontalalignment='left', verticalalignment='top')


def mm_to_inch(mm):
    return mm * 0.0393700787

fig = plt.gcf()

# set the size of the plot to be saved. These are the JGR sizes:
# quarter page = 95*115
# half page = 190*115 (horizontal) 95*230 (vertical)
# full page = 190*230
fig.set_size_inches(mm_to_inch(163 * 2), mm_to_inch(122 * 2))
plt.tight_layout()

plt.savefig('Final_Plots/escarpment_box_plots.pdf')
