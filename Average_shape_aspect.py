import string
import spatial_efd as EFD
import matplotlib.pyplot as plt
import numpy as np
import DataLoader
from matplotlib import rcParams


rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 14

A = []
B = []

sub_label = list(string.ascii_lowercase)[:2]

# use a fixed no of harmonics
MaxHarmonic = 17

sf = EFD.LoadGeometries('Data/Mid_Hollows.shp')

filename = 'Data/Mid_Data_Final_veg_curv.csv'
_, _, _, E, W = DataLoader.SegmentDataByAspect(filename)

# below here is the real processing of the shapes, above is data i/o

# loop over individual polygons in a multipart shapefile
for shaperec in sf:
    if shaperec.record in E['ID']:

        # Convert the shape instance into a format that EFD can use
        x, y, NormCentroid = EFD.ProcessGeometryNorm(shaperec)

        # Compute coefficients using the required number of harmonics and
        # normalize them
        coeffs = EFD.CalculateEFD(x, y, MaxHarmonic)
        coeffs, _ = EFD.normalize_efd(coeffs, size_invariant=True)

        A.append(coeffs)

    elif shaperec.record in W['ID']:

        # Convert the shape instance into a format that EFD can use
        x, y, NormCentroid = EFD.ProcessGeometryNorm(shaperec)

        # Compute coefficients using the required number of harmonics and
        # normalize them
        coeffs = EFD.CalculateEFD(x, y, MaxHarmonic)
        coeffs, _ = EFD.normalize_efd(coeffs, size_invariant=True)

        B.append(coeffs)

titles = ['Eastern aspect', 'Western aspect']

print (len(A), len(B))

for i, q in enumerate([A, B]):

    avg = EFD.AverageCoefficients(q)
    sd = EFD.AverageSD(q, avg)

    a, b = EFD.inverse_transform(avg, harmonic=MaxHarmonic)
    c, d = EFD.inverse_transform(avg + sd, harmonic=MaxHarmonic)
    e, f = EFD.inverse_transform(avg - sd, harmonic=MaxHarmonic)

    ax = plt.subplot(2, 1, i + 1)
    ax.axis('equal')
    ax.plot(a, b, 'k', linewidth=2.)
    ax.plot(c, d, 'k', linewidth=1., alpha=0.5)
    ax.plot(e, f, 'k', linewidth=1., alpha=0.5, label=r'$\pm$ 1 std dev')
    plt.title(titles[i], fontsize=12)

    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.tick_params(axis='both', which='both', bottom='off', top='off',
                    left='off', right='off')
    if (i == 1):
        legend = plt.legend(bbox_to_anchor=(1.1, 0), fontsize=12)
        legend.get_frame().set_linewidth(0.)

    plt.annotate(sub_label[i], xy=(0.95, 0.97),
                 xycoords='axes fraction', fontsize=12,
                 horizontalalignment='left', verticalalignment='top')


def mm_to_inch(mm):
    return mm * 0.0393700787

fig = plt.gcf()

# set the size of the plot to be saved. These are the JGR sizes:
# quarter page = 95*115
# half page = 190*115 (horizontal) 95*230 (vertical)
# full page = 190*230
fig.set_size_inches(mm_to_inch(95), mm_to_inch(230))

plt.savefig('Final_Plots/Apect_Hollow_Shape.pdf')
