import spatial_efd as EFD
import matplotlib.pyplot as plt
import numpy as np
import DataLoader
from matplotlib import rcParams
import get_downslope_orientation as gdo


rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 14

A = []

# use a fixed no of harmonics
MaxHarmonic = 17

headers, Data = DataLoader.LoadData('Data/Mid_Data_Final_veg_curv.csv')
sf = EFD.LoadGeometries('Data/Mid_Hollows.shp')

# below here is the real processing of the shapes, above is data i/o

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

ax = plt.subplot(111)
ax.axis('equal')
ax.plot(a, b, 'k', linewidth=2.)
ax.plot(c, d, 'k', linewidth=1., alpha=0.5)
ax.plot(e, f, 'k', linewidth=1., alpha=0.5, label=r'$\pm$ 1 std dev')
plt.title('Average hollow shape', fontsize=12)

ax.set_xticklabels([])
ax.set_yticklabels([])

plt.tick_params(axis='both', which='both', bottom='off', top='off',
                left='off', right='off')

legend = plt.legend(bbox_to_anchor=(1.1, 0), fontsize=12)
legend.get_frame().set_linewidth(0.)


def mm_to_inch(mm):
    return mm * 0.0393700787

fig = plt.gcf()

# set the size of the plot to be saved. These are the JGR sizes:
# quarter page = 95*115
# half page = 190*115 (horizontal) 95*230 (vertical)
# full page = 190*230
fig.set_size_inches(mm_to_inch(190), mm_to_inch(190))

plt.savefig('Final_Plots/Full_Hollow_Shape.pdf')
