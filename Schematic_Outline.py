import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import rcParams
import matplotlib.patches as mpatches
from matplotlib.legend_handler import HandlerPatch
import shapefile as shp
from DataLoader import LoadData
from get_downslope_orientation import (downslope_orientation, rotatePoint,
                                       getBBox)

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 18


def make_legend_arrow(legend, orig_handle, xdescent, ydescent, width, height,
                      fontsize):
    '''
    http://stackoverflow.com/a/22349717/1627162
    '''

    return mpatches.FancyArrow(0, 0.5 * height, width, 0,
                               length_includes_head=True,
                               head_width=0.75 * height)

TraceFile = 'Data/Mid_Intersect.shp'
Headers, MidData = LoadData('Data/Mid_Data_Final_veg_curv.csv')
sf = shp.Reader('Data/Mid_Hollows.shp')


for shaperec in sf.shapeRecords():
    if shaperec.record[0] == 246:

        itemindex = np.where(MidData['ID'] == shaperec.record[0])
        rotation = downslope_orientation(TraceFile, shaperec.record[0])

        fig = plt.figure(figsize=(1, 2))
        fig.set_size_inches(20, 10)
        gs1 = gridspec.GridSpec(1, 2)

        ax1 = plt.subplot(gs1[0])
        plt.axis('on')
        ax1.axis('equal')

        x = []
        y = []
        new_x = []
        new_y = []
        rxs = []
        rys = []

        for point in shaperec.shape.points:
            x.append(point[0])
            y.append(point[1])

        # Find the centroid of the bounding box
        xwidth, ywidth, xmin, ymin = getBBox(x, y)
        centroid = ((xwidth / 2.) + xmin, (ywidth / 2.) + ymin)

        for nx, ny in zip(x, y):
            rx, ry = rotatePoint(centroid, (nx, ny), 0.)
            rxs.append(rx)
            rys.append(ry)

        # find longest axis of rotated shape
        rxwidth, rywidth, rxmin, rymin = getBBox(rxs, rys)
        if (rxwidth > rywidth):
            normshape = rxwidth
        elif (rywidth >= rxwidth):
            normshape = rywidth

        new_x = [(value - rxmin) / normshape for value in rxs]
        new_y = [(value - rymin) / normshape for value in rys]
        plt.fill(new_x, new_y, color='k', linewidth=0.)
        pt = plt.scatter((centroid[0] - rxmin) / normshape,
                         (centroid[1] - rymin) / normshape, color='r',
                         marker='x', zorder=2, s=100, linewidth=3)

        mbr = plt.vlines(0., 0., rywidth / normshape, zorder=10000, color='r',
                         linewidth='2', linestyle='dashed')
        plt.vlines(rxwidth / normshape, 0., rywidth / normshape, zorder=10000,
                   color='r', linewidth='2', linestyle='dashed')
        plt.hlines(rywidth / normshape, 0., rxwidth / normshape, zorder=10000,
                   color='r', linewidth='2', linestyle='dashed')
        plt.hlines(0., 0., rxwidth / normshape, zorder=10000, color='r',
                   linewidth='2', linestyle='dashed')

        plt.annotate('$x_{len}$', xy=((rxwidth / normshape) / 2., 0.),
                     fontsize=24, horizontalalignment='center', xycoords='data',
                     verticalalignment='top', color='r')

        label_x = (rxwidth / normshape) + ((rxwidth / normshape) * 0.05)
        plt.annotate('$y_{len}$', xy=(label_x, (rywidth / normshape) / 2.),
                     fontsize=24, horizontalalignment='center', xycoords='data',
                     verticalalignment='center', color='r', rotation=90)

        plt.arrow(-0.125, 0.85, 0.0, 0.1, fc="k", ec="k",
                  head_width=0.025, head_length=0.025, linewidth=2., zorder=100)

        plt.annotate('N', xy=(-0.1, 0.85), xycoords='data',
                     fontsize=18, horizontalalignment='center',
                     verticalalignment='bottom')

        plt.annotate('a', xy=(0.765, 1.), xycoords='data',
                     fontsize=20, horizontalalignment='left',
                     verticalalignment='bottom')

        downslope = plt.arrow(0.38, 0.8, 0.1, 0.15, fc="b", ec="b",
                              head_width=0.025, head_length=0.025, linewidth=2.,
                              zorder=100)

        plt.xlim(-0.2, 0.8)
        plt.ylim(0., 1.)
        plt.xlabel('Dimensionless $x$ coordinate')
        plt.ylabel('Dimensionless $y$ coordinate')

        ax1.set_xticklabels([])
        ax1.set_yticklabels([])

        plt.tick_params(axis='both', which='both', bottom='off', top='off',
                        left='off', right='off')

        ax2 = plt.subplot(gs1[1])
        plt.axis('on')
        ax2.set_xticklabels([])
        ax2.set_yticklabels([])
        ax2.axis('equal')

        x = []
        y = []
        new_x = []
        new_y = []
        rxs = []
        rys = []

        for point in shaperec.shape.points:
            x.append(point[0])
            y.append(point[1])

        # Find the centroid of the bounding box
        xwidth, ywidth, xmin, ymin = getBBox(x, y)
        centroid = ((xwidth / 2.) + xmin, (ywidth / 2.) + ymin)

        for nx, ny in zip(x, y):
            rx, ry = rotatePoint(centroid, (nx, ny), rotation + 180.)
            rxs.append(rx)
            rys.append(ry)

        # find longest axis of rotated shape
        rxwidth, rywidth, rxmin, rymin = getBBox(rxs, rys)
        if (rxwidth > rywidth):
            normshape = rxwidth
        elif (rywidth >= rxwidth):
            normshape = rywidth

        new_x = [(value - rxmin) / normshape for value in rxs]
        new_y = [(value - rymin) / normshape for value in rys]
        plt.xlim(-0.2, 0.8)
        plt.ylim(0., 1.)

        plt.xlabel('Dimensionless $x$ coordinate')
        plt.ylabel('Dimensionless $y$ coordinate')

        plt.tick_params(axis='both', which='both', bottom='off', top='off',
                        left='off', right='off')

        plt.fill(new_x, new_y, color='k', linewidth=0.)

        plt.arrow(-0.125, 0.85, 0.0, 0.1, fc="k", ec="k", label='Test',
                  head_width=0.025, head_length=0.025, linewidth=2.,
                  zorder=100)

        plt.annotate('N', xy=(-0.1, 0.85), xycoords='data',
                     fontsize=18, horizontalalignment='center',
                     verticalalignment='bottom')

        plt.annotate('b', xy=(0.765, 1.), xycoords='data',
                     fontsize=20, horizontalalignment='left',
                     verticalalignment='bottom')

        plt.arrow(0.38, 0.2, 0., -0.12, fc="b", ec="b",
                  head_width=0.025, head_length=0.025, linewidth=2.,
                  zorder=100)

        # Build the legend
        labels = ['Downslope Direction', 'Minimum bounding rectangle',
                  'Centroid $(x_{MBR}$, $y_{MBR})$']
        markers = [downslope, mbr, pt]

        legend = plt.legend(markers, labels, handler_map={mpatches.FancyArrow:
                            HandlerPatch(patch_func=make_legend_arrow), },
                            scatterpoints=1, fontsize=14, loc=3)

        legend.get_frame().set_linewidth(0.)

        plt.savefig('Final_Plots/Schematic_Rotation.pdf')
