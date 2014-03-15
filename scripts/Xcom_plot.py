import matplotlib
matplotlib.use('QT4Agg')
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['axes.titlesize'] = 14
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 14
matplotlib.rcParams['ytick.labelsize'] = 14
matplotlib.rcParams['legend.fontsize'] = 14
import matplotlib.pyplot

import re

infile = open('Xcom_data.dat')

energy = []
compton = []
photo = []
pair = []
total = []

for l in infile.readlines():
    match = re.match('(\S+) (\S+) (\S+) (\S+) (\S+)', l)
    energy.append(match.group(1))
    compton.append(match.group(2))
    photo.append(match.group(3))
    pair.append(match.group(4))
    total.append(match.group(5))

matplotlib.pyplot.figure(figsize=(6,7))
matplotlib.pyplot.plot(energy, compton, label = 'Compton Scattering')
matplotlib.pyplot.plot(energy, photo, label = 'Photoelectric Absorption')
matplotlib.pyplot.plot(energy, pair, label = 'Pair Production in Nuclear Field')
matplotlib.pyplot.plot(energy, total, label = 'Total Attenuation (w/o Coherent Scattering)', lw = 3)
matplotlib.pyplot.loglog()
matplotlib.pyplot.legend(loc = 'upper right')
matplotlib.pyplot.grid()
matplotlib.pyplot.gca().set_xlabel('Gamma Energy (MeV)')
matplotlib.pyplot.gca().set_ylabel('Attenuation in Xenon (cm$^2$/g)')
matplotlib.pyplot.axvline(2.4567, 0, 1, color = 'black', linestyle = '--')
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig('XrayAttenuationXenon.pdf')

