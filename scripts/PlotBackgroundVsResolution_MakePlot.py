import matplotlib
matplotlib.use('QT4Agg')
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['axes.titlesize'] = 14
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 14
matplotlib.rcParams['ytick.labelsize'] = 14
matplotlib.rcParams['legend.fontsize'] = 14
import matplotlib.pyplot

label_dict = {'Th' : 'Th-232', 'Xe' : 'Xe-137', 'U' : 'U-238'}

values = dict()
for isotope in ['Th', 'Xe', 'U']:
    values[isotope] = dict()
    values[isotope]['res'] = []
    values[isotope]['bkgd'] = []

    for res in ['0.0', '0.001', '0.002', '0.003', '0.004', '0.005', '0.006', '0.007', '0.008', '0.009', '0.01', '0.011', '0.012', '0.013', '0.014', '0.015', '0.016', '0.017', '0.018', '0.019', '0.02', '0.021', '0.022', '0.023', '0.024', '0.025', '0.026', '0.027', '0.028', '0.029', '0.03']:
        values[isotope]['res'].append(100*float(res))
        log_file = open('BackgroundsVsResFiles/' + isotope + '_' + res + '.log')
        bkgd = float(log_file.read())
        values[isotope]['bkgd'].append(bkgd)
        if res == '0.016': norm_bkgd = bkgd
    for i in range(len(values[isotope]['bkgd'])): values[isotope]['bkgd'][i] /= norm_bkgd

    matplotlib.pyplot.plot(values[isotope]['res'], values[isotope]['bkgd'], label = label_dict[isotope])

legend = matplotlib.pyplot.legend(loc = 'upper left')
matplotlib.pyplot.grid()
matplotlib.pyplot.gca().set_xlim(0,2.5)
matplotlib.pyplot.gca().set_ylim(0,4)
matplotlib.pyplot.gca().set_xlabel('Resolution ($\sigma/E$, %) at 2457 keV')
matplotlib.pyplot.gca().set_ylabel('Background Rates in $2\sigma$ Region of Interest (arbitrary units)')
matplotlib.pyplot.gcf().tight_layout()
for label in legend.get_lines():
    label.set_linewidth(2)
#matplotlib.pyplot.gca().set_yscale('log')
matplotlib.pyplot.gcf().subplots_adjust(left=0.1)
matplotlib.pyplot.savefig('BackgroundsVsRes.pdf')
