import spatial_efd as EFD
import matplotlib.pyplot as plt
import numpy as np
import DataLoader
import string
from matplotlib import rcParams
import get_downslope_orientation as gdo


rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 14

sub_label = list(string.ascii_lowercase)[:3]

A = []

# use a fixed no of harmonics
MaxHarmonic = 17

headers, Data = DataLoader.LoadData('Data/Mid_Data_Final_veg_curv.csv')
sf = EFD.LoadGeometries('Data/Mid_Hollows.shp')

# loop over individual polygons in a multipart shapefile
for shaperec in sf:

    # get the index of the data in order to find the X,Y outlet coords
    q = [i for i, a in enumerate(list(Data['ID'])) if a == shaperec.record[0]]

    if q:
        point = (Data['X'][q], Data['Y'][q])
        _, _, Centroid = EFD.ProcessGeometry(shaperec)
        rotation = gdo.AngleBetween(Centroid, point)

        # Convert the shape instance into a format that EFD can use
        x, y, NormCentroid = EFD.ProcessGeometryNorm(shaperec)

        # Perform a spatial rotation to have the hollow point south
        x, y = EFD.RotateContour(x, y, rotation, NormCentroid)

        # Compute coefficients using the required number of harmonics and
        # normalize them
        coeffs = EFD.CalculateEFD(x, y, MaxHarmonic)
        coeffs, _ = EFD.normalize_efd(coeffs, size_invariant=True)
        A.append(coeffs)

avg = EFD.AverageCoefficients(A)
sd = EFD.AverageSD(A, avg)

a, b = EFD.inverse_transform(avg, harmonic=MaxHarmonic)
c, d = EFD.inverse_transform(avg + sd, harmonic=MaxHarmonic)
e, f = EFD.inverse_transform(avg - sd, harmonic=MaxHarmonic)

ax = plt.subplot(221)
ax.axis('equal')
ax.plot(a, b, 'k', linewidth=2.)
ax.plot(c, d, 'k', linewidth=1., alpha=0.5)
ax.plot(e, f, 'k', linewidth=1., alpha=0.5, label=r'$\pm$ 1 std dev')
plt.title('Average basin shape', fontsize=12)

ax.set_xticklabels([])
ax.set_yticklabels([])

plt.tick_params(axis='both', which='both', bottom='off', top='off',
                left='off', right='off')

plt.annotate(sub_label[0], xy=(0.95, 0.97),
             xycoords='axes fraction', fontsize=12,
             horizontalalignment='left', verticalalignment='top')

# ------------------------------------------------------------------------------

A = []

sf = EFD.LoadGeometries('Data/Escarpment_Hollows.shp')

# loop over individual polygons in a multipart shapefile
for shaperec in sf:

    # get the index of the data in order to find the X,Y outlet coords
    q = [i for i, a in enumerate(list(Data['ID'])) if a == shaperec.record[0]]

    if q:
        point = (Data['X'][q], Data['Y'][q])
        _, _, Centroid = EFD.ProcessGeometry(shaperec)
        rotation = gdo.AngleBetween(Centroid, point)

        # Convert the shape instance into a format that EFD can use
        x, y, NormCentroid = EFD.ProcessGeometryNorm(shaperec)

        # Perform a spatial rotation to have the hollow point south
        x, y = EFD.RotateContour(x, y, rotation, NormCentroid)

        # Compute coefficients using the required number of harmonics and
        # normalize them
        coeffs = EFD.CalculateEFD(x, y, MaxHarmonic)
        coeffs, _ = EFD.normalize_efd(coeffs, size_invariant=True)
        A.append(coeffs)

avg = EFD.AverageCoefficients(A)
sd = EFD.AverageSD(A, avg)

a, b = EFD.inverse_transform(avg, harmonic=MaxHarmonic)
c, d = EFD.inverse_transform(avg + sd, harmonic=MaxHarmonic)
e, f = EFD.inverse_transform(avg - sd, harmonic=MaxHarmonic)

ax = plt.subplot(222)
ax.axis('equal')
ax.plot(a, b, 'k', linewidth=2.)
ax.plot(c, d, 'k', linewidth=1., alpha=0.5)
ax.plot(e, f, 'k', linewidth=1., alpha=0.5, label=r'$\pm$ 1 std dev')
plt.title('Escarpment basin shape', fontsize=12)

ax.set_xticklabels([])
ax.set_yticklabels([])

plt.tick_params(axis='both', which='both', bottom='off', top='off',
                left='off', right='off')

plt.annotate(sub_label[1], xy=(0.95, 0.97),
             xycoords='axes fraction', fontsize=12,
             horizontalalignment='left', verticalalignment='top')

# ------------------------------------------------------------------------------

A = []

sf = EFD.LoadGeometries('Data/Non_Escarpment_Hollows.shp')

# loop over individual polygons in a multipart shapefile
for shaperec in sf:

    # get the index of the data in order to find the X,Y outlet coords
    q = [i for i, a in enumerate(list(Data['ID'])) if a == shaperec.record[0]]

    if q:
        point = (Data['X'][q], Data['Y'][q])
        _, _, Centroid = EFD.ProcessGeometry(shaperec)
        rotation = gdo.AngleBetween(Centroid, point)

        # Convert the shape instance into a format that EFD can use
        x, y, NormCentroid = EFD.ProcessGeometryNorm(shaperec)

        # Perform a spatial rotation to have the hollow point south
        x, y = EFD.RotateContour(x, y, rotation, NormCentroid)

        # Compute coefficients using the required number of harmonics and
        # normalize them
        coeffs = EFD.CalculateEFD(x, y, MaxHarmonic)
        coeffs, _ = EFD.normalize_efd(coeffs, size_invariant=True)
        A.append(coeffs)

avg = EFD.AverageCoefficients(A)
sd = EFD.AverageSD(A, avg)

a, b = EFD.inverse_transform(avg, harmonic=MaxHarmonic)
c, d = EFD.inverse_transform(avg + sd, harmonic=MaxHarmonic)
e, f = EFD.inverse_transform(avg - sd, harmonic=MaxHarmonic)

ax = plt.subplot(224)
ax.axis('equal')
ax.plot(a, b, 'k', linewidth=2.)
ax.plot(c, d, 'k', linewidth=1., alpha=0.5)
ax.plot(e, f, 'k', linewidth=1., alpha=0.5, label=r'$\pm$ 1 std dev')
plt.title('Non-escarpment basin shape', fontsize=12)

ax.set_xticklabels([])
ax.set_yticklabels([])

plt.tick_params(axis='both', which='both', bottom='off', top='off',
                left='off', right='off')

plt.annotate(sub_label[2], xy=(0.95, 0.97),
             xycoords='axes fraction', fontsize=12,
             horizontalalignment='left', verticalalignment='top')

ax = plt.subplot(223)

# build a fake third panel with some data so we can place the legend there

ax.axis('off')

plt.xlim(5, 10)
plt.ylim(5, 10)

ax.plot(e, f, 'k', linewidth=1., alpha=0.5, label=r'$\pm$ 1 std dev')

legend = plt.legend(loc=9, fontsize=12)
legend.get_frame().set_linewidth(0.)


def mm_to_inch(mm):
    return mm * 0.0393700787

fig = plt.gcf()

# set the size of the plot to be saved. These are the JGR sizes:
# quarter page = 95*115
# half page = 190*115 (horizontal) 95*230 (vertical)
# full page = 190*230
fig.set_size_inches(mm_to_inch(190), mm_to_inch(190))

plt.savefig('Final_Plots/Escarpment_Hollow_Shape.pdf')
