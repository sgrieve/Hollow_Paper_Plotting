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
label = ['Area', 'Length']

for i, filename in enumerate(['Data/Area_AutoCorr.csv',
                              'Data/Length_AutoCorr.csv']):

    Headers, Data = LoadData(filename)

    plt.plot(Data['distclass'][:38] / 2., Data['coef'][:38], colors[i],
             linewidth=2.0, linestyle=styles[i], label=label[i])

legend = plt.legend(loc=2)
legend.get_frame().set_linewidth(0.)

plt.xlabel('Search radius ($m$)')
plt.ylabel('Moran\'s I statistic')

plt.ylim(-1., 1.)
plt.xlim(0, 3350)


plt.arrow(2700, 0.2, 0.0, 0.4, fc="k", ec="k",
          head_width=100, head_length=0.1, linewidth=2.)

plt.arrow(2700, -0.2, 0.0, -0.4, fc="k", ec="k",
          head_width=100, head_length=0.1, linewidth=2.)

plt.annotate('Increasing clustering', xy=(2700, 0.8), xycoords='data',
             fontsize=14, horizontalalignment='center',
             verticalalignment='bottom')

plt.annotate('Random\n\ndistribution', xy=(2700, 0.0), xycoords='data',
             fontsize=14, horizontalalignment='center',
             verticalalignment='center')

plt.annotate('Increasing dispersion', xy=(2700, -0.8), xycoords='data',
             fontsize=14, horizontalalignment='center',
             verticalalignment='top')

plt.tick_params(axis='both', which='both', top='off', right='off')
plt.tight_layout()

ax = plt.gca()

ax.set_xticks(ax.get_xticks()[::2])
ax.set_yticks(ax.get_yticks()[::2])

plt.savefig('Final_Plots/Merged_AutoCorr.pdf')
