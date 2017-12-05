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

plt.plot(Data['width'], Data['Area_Length_Ratio'], '.b')

slope, intercept, r_value, _, _ = stats.linregress(Data['width'],
                                                   Data['Area_Length_Ratio'])
plt.text(5, 80, 'R squared: {}'.format(round(r_value**2, 3), fontsize=12))

x = np.arange(160)
y = slope * x + intercept
plt.plot(x, y, 'k--')

plt.xlabel('Width (m)')
plt.ylabel('Area/Length (m)')
plt.savefig('width_comparison.png')
