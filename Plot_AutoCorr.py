import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from DataLoader import LoadData

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 14
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'

colors = ['k', 'r']
styles = ['-', '--']
label = [['Area', 'Width'], ['Escarpment area', 'Non-escarpment area']]
files = [['area_ac.csv', 'width_ac.csv'],
         ['esc_area_ac_small.csv', 'non_esc_area_ac.csv']]
sub_label = ['a', 'b']

for a in xrange(2):

    ax = plt.subplot(1, 2, a + 1)

    for i, filename in enumerate(files[a]):

        Headers, Data = LoadData(filename)

        plt.plot(Data['distclass'] / 2., Data['coef'], colors[i],
                 linewidth=2.0, linestyle=styles[i], label=label[a][i])

    legend = plt.legend(loc=2)
    legend.get_frame().set_linewidth(0.)

    plt.xlabel('Search radius ($m$)')
    plt.ylabel('Moran\'s I statistic')

    plt.ylim(-1., 1.)

    if a:
        plt.xlim(0, 1150)
    else:
        plt.xlim(0, 2500)
        plt.arrow(1500, 0.2, 0.0, 0.4, fc="k", ec="k",
                  head_width=100, head_length=0.1, linewidth=2.)

        plt.arrow(1500, -0.2, 0.0, -0.4, fc="k", ec="k",
                  head_width=100, head_length=0.1, linewidth=2.)

        plt.annotate('Increasing clustering', xy=(1500, 0.8), xycoords='data',
                     fontsize=14, horizontalalignment='center',
                     verticalalignment='bottom')

        plt.annotate('Random\n\ndistribution', xy=(1500, 0.0), xycoords='data',
                     fontsize=14, horizontalalignment='center',
                     verticalalignment='center')

        plt.annotate('Increasing dispersion', xy=(1500, -0.8), xycoords='data',
                     fontsize=14, horizontalalignment='center',
                     verticalalignment='top')

    ax.set_yticks(ax.get_yticks()[::2])

    plt.annotate(sub_label[a], xy=(0.95, 0.97),
                 xycoords='axes fraction', fontsize=14,
                 horizontalalignment='left', verticalalignment='top')


plt.tick_params(axis='both', which='both', top='off', right='off')
plt.tight_layout()


def mm_to_inch(mm):
    return mm * 0.0393700787

fig = plt.gcf()

# set the size of the plot to be saved. These are the JGR sizes:
# quarter page = 95*115
# half page = 190*115 (horizontal) 95*230 (vertical)
# full page = 190*230
fig.set_size_inches(mm_to_inch(163 * 2), mm_to_inch(122))

plt.savefig('Final_Plots/Merged_AutoCorr.pdf')
