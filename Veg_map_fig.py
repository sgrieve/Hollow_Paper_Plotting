import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import LSDPlottingTools as LSDP
from LSDPlottingTools import colours
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 14


DataDirectory = "Data/"
filename = DataDirectory + "DEM.bil"
drapename = DataDirectory + "Vegetation.tif"

drape_array = LSDP.ReadRasterArrayBlocks(drapename)

cmap = colours.discrete_colourmap(4, 'Greens')

labels = ['A', 'B', 'C', 'D']
labels_ = ['A: Cove\nhardwood', 'B: Mixed\ndeciduous', 'C: Xeric\noak-pine',
           'D: Northern\nhardwood']

fig = LSDP.DrapedOverHillshade_Categories(filename, drape_array, 4, (0., 3.),
                                          thiscmap='gray',
                                          drape_cmap=cmap,
                                          drape_alpha=0.5,
                                          ShowDrapeColorbar=True,
                                          drape_cbarlabel='Vegetation classes',
                                          category_labels=labels)

plt.annotate('b', xy=(-20., 1.08), xycoords='axes fraction', fontsize=30,
             horizontalalignment='left', verticalalignment='top')

ax = plt.subplot(121)

p1 = (0., 1065.)
p2 = (3500., 1182.)
p3 = (7812.5, 1322.)
p4 = (10001., 1322.)
p5 = (0., 600.)
p6 = (3500., 600.)
p7 = (5250., 600.)
p8 = (6562.5, 720.)
p9 = (7375., 755.)
p10 = (7812.5, 839.)
p11 = (10001., 600.)
p12 = (10001., 1400.)
p13 = (0., 1400.)
p14 = (6562.5, 1287.)


def process_to_plot(input_coords):

    x = [a[0] for a in input_coords]
    y = [a[1] for a in input_coords]
    return x, y

x, y = process_to_plot([p1, p2, p14, p3, p4])
plt.plot(x, y, 'k-', linewidth=2.)

x, y = process_to_plot([p6, p2])
plt.plot(x, y, 'k-', linewidth=2.)

x, y = process_to_plot([p3, p10, p9, p8, p7])
plt.plot(x, y, 'k-', linewidth=2.)

plt.ylim(ymin=600.)
plt.xlim(xmax=10001)

plt.xlabel('Terrain shape index')
plt.ylabel('Elevation (m)')
plt.locator_params(nbins=4)

coords = [[p1, p2, p6, p5], [p2, p6, p7, p8, p9, p10, p3, p14],
          [p7, p8, p9, p10, p3, p4, p11], [p1, p2, p14, p3, p4, p12, p13]]

# label coordinates
xs = [365, 4250, 6700, 1400]
ys = [950, 950, 700, 1325]

for i, c in enumerate(coords):
    polygon = Polygon(c, True)
    polygon.set_color(cmap(i))
    ax.add_patch(polygon)
    plt.annotate(labels_[i], xy=(xs[i], ys[i]), xycoords='data', fontsize=16,
                 horizontalalignment='left', verticalalignment='top')


plt.annotate('a', xy=(-0.32, 1.055), xycoords='axes fraction', fontsize=30,
             horizontalalignment='left', verticalalignment='top')

plt.xlim(xmin=0.)

plt.tight_layout()

plt.savefig('Final_Plots/vegetation.pdf')
