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
from matplotlib.patches import Polygon

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

    sf = shp.Reader('Data/Escarpment_Hollows.shp')
    polygons = []
    for shape in sf.shapes():
        q = []
        for point in shape.points:

            # convert shapeile data into raster coords
            x = point[0] - xll
            y = (-1 * point[1]) + yll + y_max
            q.append((x, y))

        polygons.append(q)

    for p in polygons:
        poly = Polygon(p, True, facecolor=(1., 0., 0., 0.35),
                       edgecolor=(0., 0., 0., 0.75), linewidth=0.5,
                       rasterized=True)
        ax2.add_patch(poly)

    sf = shp.Reader('Data/Non_Escarpment_Hollows_selection.shp')

    polygons = []
    for shape in sf.shapes():

        q = []
        for point in shape.points:

            # convert shapeile data into raster coords
            x = point[0] - xll
            y = (-1 * point[1]) + yll + y_max
            q.append((x, y))

        polygons.append(q)

    for p in polygons:
        poly2 = Polygon(p, True, facecolor=(0., 0., 1., 0.35),
                        edgecolor=(0., 0., 0., 0.75), linewidth=0.5,
                        rasterized=True)
        ax2.add_patch(poly2)

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

    plt.xlim(500, 3200)
    plt.ylim(y_center + 1800, y_center - 10)

    plt.xlabel('Easting ($km$)')
    plt.ylabel('Northing ($km$)')

    box = ax2.get_position()
    ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    legend = ax2.legend([poly, poly2],
                        ['Escarpment\nhollows', 'Non-Escarpment\nhollows'],
                        loc='center left', bbox_to_anchor=(.99, 0.5),
                        fontsize=10, handlelength=0.7)

    frame = legend.get_frame()
    frame.set_linewidth(0.)
    frame.set_facecolor('none')

    plt.subplots_adjust(left=-0.07, right=1., top=0.94, bottom=0.16)
    plt.savefig('Final_Plots/Hollows_map.pdf')


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
