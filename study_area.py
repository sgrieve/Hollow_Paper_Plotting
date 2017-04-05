# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib.cm as cmx
from matplotlib import rcParams
import raster_plotter_simple as raster
import shapefile as shp
from mpl_toolkits.axes_grid.inset_locator import inset_axes

# Set up fonts for plots
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 12
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['figure.subplot.left'] = 0.005
rcParams['figure.subplot.top'] = 0.95
rcParams['figure.subplot.right'] = 0.95


def mm_to_inch(mm):
    return mm * 0.0393700787


def Draw_Outline(Country_Outline, State_Borders, Points, hillshade_file):

    fig = plt.figure()
    fig.set_size_inches(mm_to_inch(190), mm_to_inch(200))

    ax = fig.add_subplot(211)

    sf = shp.Reader('Data/CountyBoundary_UTM.shp')

    for shape in sf.shapes():
        x = []
        y = []
        for point in shape.points:
            x.append(point[0])
            y.append(point[1])
        plt.plot(x, y, 'k-', linewidth=0.5, alpha=0.25)

    sf = shp.Reader('Data/NC_UTM.shp')

    for shape in sf.shapes():
        x = []
        y = []
        for point in shape.points:
            x.append(point[0])
            y.append(point[1])
        plt.plot(x, y, 'k-', linewidth=1)

    sf = shp.Reader('Data/Macon_Boundary.shp')

    for shape in sf.shapes():
        x = []
        y = []
        for point in shape.points:
            x.append(point[0])
            y.append(point[1])
        plt.plot(x, y, 'r-', linewidth=2)

    plt.title('North Carolina, USA')

    plt.annotate('a', xy=(0.11, 0.97),
                 xycoords='axes fraction', fontsize=16,
                 horizontalalignment='left', verticalalignment='top')

    # suppress the ticks and labels
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')

    inset = inset_axes(ax, width=1.75, height=1.75, bbox_to_anchor=(0.94, 0.72),
                 bbox_transform=fig.transFigure)

    # suppress the ticks and labels
    inset.xaxis.set_visible(False)
    inset.yaxis.set_visible(False)
    # inset.axis('off')
    inset.set_aspect('equal', adjustable='box')

    sf = shp.Reader(Country_Outline)

    for shape in sf.shapes():
        x = []
        y = []
        for point in shape.points:
            x.append(point[0])
            y.append(point[1])
        plt.plot(x, y, 'k-', linewidth=1)

    sf = shp.Reader(State_Borders)

    for shape in sf.shapes():
        x = []
        y = []
        for point in shape.points:
            x.append(point[0])
            y.append(point[1])
        plt.plot(x, y, 'k-', linewidth=0.5, alpha=0.25)

    sf = shp.Reader('Data/NC.shp')

    for shape in sf.shapes():
        x = []
        y = []
        for point in shape.points:
            x.append(point[0])
            y.append(point[1])
        plt.plot(x, y, 'r-', linewidth=1)

    ax2 = fig.add_subplot(212)

    # get data
    hillshade, hillshade_header = raster.read_flt(hillshade_file)

    # ignore nodata values
    hillshade = np.ma.masked_where(hillshade == -9999, hillshade)

    x_max = hillshade_header[0]
    x_min = 0
    y_max = hillshade_header[1]
    y_min = 0

    # plot the hillshade on the axes
    plt.imshow(hillshade, vmin=0, vmax=255, cmap=cmx.gray)

    # now get the tick marks
    n_target_tics = 4
    xlocs, ylocs, new_x_labels, new_y_labels = raster.format_ticks_for_UTM_imshow(hillshade_header, x_max, x_min, y_max, y_min, n_target_tics)

    new_x_labels = [l[0:-3] for l in new_x_labels]
    new_y_labels = [l[0:-3] for l in new_y_labels]

    plt.xticks(xlocs, new_x_labels, rotation=60)
    plt.yticks(ylocs, new_y_labels)

    x_center = int(x_max / 2.)
    y_center = int(y_max / 2.)

    plt.xlim(x_center - 3000, x_center + 3000)
    plt.ylim(y_center + 2000, y_center - 2000)

    plt.xlabel('Easting ($km$)')
    plt.ylabel('Northing ($km$)')
    plt.title('Coweeta, NC')

    plt.annotate('b', xy=(-0.1, 1.1),
                 xycoords='axes fraction', fontsize=16,
                 horizontalalignment='left', verticalalignment='top')


    tmp1 = ax.transData.transform([-83.4428, 35.12])
    x, y = fig.transFigure.inverted().transform(tmp1)

    # Convert axes coords for the corners of the subplot into display coords
    # then convert those display coords into figure coords for plotting the line
    x1, y1 = fig.transFigure.inverted().transform(ax2.transAxes.transform([0.181, 1.]))
    x2, y2 = fig.transFigure.inverted().transform(ax2.transAxes.transform([0.816, 1.]))

    line = matplotlib.lines.Line2D((x, x1),
                                   (y, y1),
                                   transform=fig.transFigure, color='k')
    fig.lines.append(line)

    line = matplotlib.lines.Line2D((x, x2),
                                   (y, y2),
                                   transform=fig.transFigure, color='k')
    fig.lines.append(line)

    plt.savefig('Final_Plots/Study_Area.pdf')


def Make_The_Figure():
    """
    All filenames and paths to data are modifed here in this wrapper
    """

    HS_file = 'Data/NC_HS.flt'
    State_Borders = 'Data/explode_project.shp'
    Country_Outline = 'Data/polygon_project.shp'
    Points = 'Data/points.shp'

    Draw_Outline(Country_Outline, State_Borders, Points, HS_file)


Make_The_Figure()
