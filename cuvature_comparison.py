import string
import shapefile as shp
import matplotlib.pyplot as plt
import matplotlib as mpl
from rasterstats import zonal_stats
from matplotlib import rcParams


rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 14

curvature = '/home/sgrieve/Hollow_Paper_Plotting/Data/curvature.tif'
hollows = '/home/sgrieve/Hollow_Paper_Plotting/Data/Plot_Hollows.shp'

sf = shp.Reader(hollows)
stats = zonal_stats(hollows, curvature, raster_out=True, nodata=-9999)

sub_label = list(string.ascii_lowercase)[:2]

fig, axes = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=False)

for i, ax in enumerate(axes.flat):
    array = stats[i]['mini_raster_array']
    im = ax.imshow(array, cmap=plt.cm.seismic, vmin=-0.08, vmax=0.08)
    ax.axis('equal')

    if i:
        ax.set_ylim(-1, 116)
    else:
        ax.set_ylim(116, -1)

        ax.plot([0, 20], [105, 105], 'k-', linewidth=5)
        ax.annotate('20 m', xy=(10, 108),
                    xycoords='data', fontsize=14,
                    horizontalalignment='center', verticalalignment='top')

    ax.set_xticklabels([])
    ax.set_yticklabels([])

    ax.tick_params(axis='both', which='both', bottom='off', top='off',
                   left='off', right='off')

    ax.annotate(sub_label[i], xy=(0.05, 0.97),
                xycoords='axes fraction', fontsize=16,
                horizontalalignment='left', verticalalignment='top')


fig.subplots_adjust(bottom=0.175, top=0.975)
cbar_ax = fig.add_axes([0.15, 0.075, 0.725, 0.04])
colorbar = fig.colorbar(im, cax=cbar_ax, orientation='horizontal',
                        ticks=[-0.08, 0, 0.08])

colorbar.ax.set_xticklabels(['Convex', 'Planar', 'Concave'])
colorbar.outline.set_visible(False)
colorbar.ax.tick_params(axis='x', which='both', bottom='off', top='off')


def mm_to_inch(mm):
    return mm * 0.0393700787

# set the size of the plot to be saved. These are the JGR sizes:
# quarter page = 95*115
# half page = 190*115 (horizontal) 95*230 (vertical)
# full page = 190*230
fig.set_size_inches(mm_to_inch(190), mm_to_inch(115))

plt.savefig('Final_Plots/Hollow_comparison.pdf')
