# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib.cm as cmx
from matplotlib import rcParams
import raster_plotter_simple as raster
from raster_plotter_simple import format_ticks_for_UTM_imshow as fmt_UTM
import shapefile as shp
from mpl_toolkits.axes_grid.inset_locator import inset_axes

# Set up fonts for plots
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 12
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'


def mm_to_inch(mm):
    return mm * 0.0393700787


def Draw_Outline(Country_Outline, State_Borders, Points, hillshade_file):

    fig = plt.figure()
    fig.set_size_inches(mm_to_inch(190), mm_to_inch(115))

    ax2 = fig.add_subplot(111)

    # get data
    hillshade, hillshade_header = raster.read_flt(hillshade_file)

    # ignore nodata values
    hillshade = np.ma.masked_where(hillshade == -9999, hillshade)

    x_max = hillshade_header[0]
    x_min = 0
    y_max = hillshade_header[1]
    y_min = 0
    xll = hillshade_header[2]
    yll = hillshade_header[3]

    # plot the hillshade on the axes
    plt.imshow(hillshade, vmin=0, vmax=255, cmap=cmx.gray)

    # Add in the escarpment outline here

    sf = shp.Reader('Data/test.shp')

    for shape in sf.shapes():
        x = []
        y = []
        for point in shape.points:
            # convert shapeile data into raster coords
            x.append(point[0] - xll)
            y.append((-1 * point[1]) + yll + y_max)
        ax2.plot(x, y, 'r-', linewidth=3, alpha=1)

    # now get the tick marks
    n_target_tics = 4
    xlocs, ylocs, new_x_labels, new_y_labels = fmt_UTM(hillshade_header,
                                                       x_max, x_min,
                                                       y_max, y_min,
                                                       n_target_tics)

    new_x_labels = [l[0:-3] for l in new_x_labels]
    new_y_labels = [l[0:-3] for l in new_y_labels]

    plt.xticks(xlocs, new_x_labels, rotation=60)
    plt.yticks(ylocs, new_y_labels)

    x_center = int(x_max / 2.)
    y_center = int(y_max / 2.)

    x_width = x_max - x_min

    plt.xlim(0, x_center + 3000)
    plt.ylim(y_center + 2000, y_center - 2000)

    plt.xlabel('Easting ($km$)')
    plt.ylabel('Northing ($km$)')

    # NC inset
    inset2 = inset_axes(ax2, width=2., height=2.,
                        bbox_to_anchor=(1.0, 0.8),
                        bbox_transform=fig.transFigure)

    # suppress the ticks and labels
    inset2.xaxis.set_visible(False)
    inset2.yaxis.set_visible(False)
    # inset.axis('off')
    inset2.set_aspect('equal', adjustable='box')

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
        plt.plot(x[0], y[0], 'r.')

    # USA inset
    inset = inset_axes(ax2, width=2., height=2.,
                       bbox_to_anchor=(1., 1.042),
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

    plt.subplots_adjust(left=0., right=1., top=0.94, bottom=0.16)
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
