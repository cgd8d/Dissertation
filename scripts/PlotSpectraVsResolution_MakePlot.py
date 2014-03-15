import ROOT
import matplotlib
matplotlib.use('QT4Agg')
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['axes.titlesize'] = 14
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 14
matplotlib.rcParams['ytick.labelsize'] = 14
matplotlib.rcParams['legend.fontsize'] = 14
import matplotlib.pyplot

values = {}
for isotope in ['Th', 'U']:
    values[isotope] = {}
    weights = {}
    max_content = 0.
    for res in ['0.004', '0.008', '0.012', '0.016', '0.02']:
        values[isotope][res] = []
        ifile = ROOT.TFile("SpectraVsResFiles/%s_%s.root" % (isotope, res))
        ihist = ifile.Get("hist_%s_%s" % (isotope, res))
        #max_content = 0.
        for i in range(500):
            max_content = max(ihist.GetBinContent(i+1), max_content)
        #weights[res] = 0.09/max_content
        for i in range(500):
            values[isotope][res] += [2200.5 + i]*int(ihist.GetBinContent(i+1)+0.5)
    for res in ['0.004', '0.008', '0.012', '0.016', '0.02']: weights[res] = 0.09/max_content

    matplotlib.pyplot.clf()
    matplotlib.pyplot.figure(figsize=(6,8))

    matplotlib.pyplot.subplot(511)
    matplotlib.pyplot.hist(values[isotope]['0.02'], bins = 50, histtype = 'step', weights = [weights['0.02']]*len(values[isotope]['0.02']))
    matplotlib.pyplot.gca().set_yscale('log')
    matplotlib.pyplot.gca().set_ylim(0.005, 1)
    matplotlib.pyplot.gca().set_xticklabels([])
    matplotlib.pyplot.axvline(2456.7*(1.-2*0.02), 0, 1, color = 'r')
    matplotlib.pyplot.axvline(2456.7*(1.+2*0.02), 0, 1, color = 'r')
    matplotlib.pyplot.text(2220, 0.4, "$2\%$ $\sigma/E$ at 2457 keV")
    matplotlib.pyplot.gca().set_ylabel('Rate (a.u.)')
    matplotlib.pyplot.grid()

    matplotlib.pyplot.subplot(512)
    matplotlib.pyplot.hist(values[isotope]['0.016'], bins = 50, histtype = 'step', weights = [weights['0.016']]*len(values[isotope]['0.016']))
    matplotlib.pyplot.gca().set_yscale('log')
    matplotlib.pyplot.gca().set_ylim(0.005, 1)
    matplotlib.pyplot.gca().set_xticklabels([])
    matplotlib.pyplot.axvline(2456.7*(1.-2*0.016), 0, 1, color = 'r')
    matplotlib.pyplot.axvline(2456.7*(1.+2*0.016), 0, 1, color = 'r')
    matplotlib.pyplot.text(2220, 0.4, "$1.6\%$ $\sigma/E$ at 2457 keV")
    matplotlib.pyplot.gca().set_ylabel('Rate (a.u.)')
    matplotlib.pyplot.grid()

    matplotlib.pyplot.subplot(513)
    matplotlib.pyplot.hist(values[isotope]['0.012'], bins = 50, histtype = 'step', weights = [weights['0.012']]*len(values[isotope]['0.012']))
    matplotlib.pyplot.gca().set_yscale('log')
    matplotlib.pyplot.gca().set_ylim(0.005, 1)
    matplotlib.pyplot.gca().set_xticklabels([])
    matplotlib.pyplot.axvline(2456.7*(1.-2*0.012), 0, 1, color = 'r')
    matplotlib.pyplot.axvline(2456.7*(1.+2*0.012), 0, 1, color = 'r')
    matplotlib.pyplot.text(2220, 0.4, "$1.2\%$ $\sigma/E$ at 2457 keV")
    matplotlib.pyplot.gca().set_ylabel('Rate (a.u.)')
    matplotlib.pyplot.grid()

    matplotlib.pyplot.subplot(514)
    matplotlib.pyplot.hist(values[isotope]['0.008'], bins = 50, histtype = 'step', weights = [weights['0.008']]*len(values[isotope]['0.008']))
    matplotlib.pyplot.gca().set_yscale('log')
    matplotlib.pyplot.gca().set_ylim(0.005, 1)
    matplotlib.pyplot.gca().set_xticklabels([])
    matplotlib.pyplot.axvline(2456.7*(1.-2*0.008), 0, 1, color = 'r')
    matplotlib.pyplot.axvline(2456.7*(1.+2*0.008), 0, 1, color = 'r')
    matplotlib.pyplot.text(2220, 0.4, "$0.8\%$ $\sigma/E$ at 2457 keV")
    matplotlib.pyplot.gca().set_ylabel('Rate (a.u.)')
    matplotlib.pyplot.grid()

    matplotlib.pyplot.subplot(515)
    matplotlib.pyplot.hist(values[isotope]['0.004'], bins = 50, histtype = 'step', weights = [weights['0.004']]*len(values[isotope]['0.004']))
    matplotlib.pyplot.gca().set_yscale('log')
    matplotlib.pyplot.gca().set_ylim(0.005, 1)
    matplotlib.pyplot.gca().set_xlabel('Energy (keV)')
    matplotlib.pyplot.axvline(2456.7*(1.-2*0.004), 0, 1, color = 'r')
    matplotlib.pyplot.axvline(2456.7*(1.+2*0.004), 0, 1, color = 'r')
    matplotlib.pyplot.text(2220, 0.4, "$0.4\%$ $\sigma/E$ at 2457 keV")
    matplotlib.pyplot.gca().set_ylabel('Rate (a.u.)')
    matplotlib.pyplot.grid()

    matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.savefig('%s_Spectra_vs_Res.pdf' % isotope)
