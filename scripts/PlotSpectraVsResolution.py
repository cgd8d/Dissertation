'''
Just a rough idea, since lots of things in the analysis can change;
generally to show how close our backgrounds are to a linear dependence on resolution.
'''

import sys
if len(sys.argv) > 1:
    # We're on a batch machine; interpret the arguments, save the output to a file.
    import ROOT
    ROOT.gROOT.SetBatch()
    ROOT.gSystem.Load("libEXOCalibUtilities")
    if sys.argv[1] == 'Th':
        MCfiles = '/nfs/slac/g/exo_data4/users/FittingMC/2013_09_20/AllVessel_Th232.root'
    elif sys.argv[1] == 'U':
        MCfiles = '/nfs/slac/g/exo_data4/users/FittingMC/2013_09_20/AllVessel_U238.root'
    elif sys.argv[1] == 'Xe':
        MCfiles = '/nfs/slac/g/exo_data4/users/FittingMC/2013_09_20/ActiveLXe_Xe137.root'
    else:
        raise ValueError("Unrecognized source.")

    mcfile = ROOT.TFile(MCfiles)
    mctree = mcfile.Get("mcTree")

    event = ROOT.EXOEventSummary()
    ROOT.EXOEventSummary.SetFiducialVolumeDBFlavor("2013-0nu")

    res = float(sys.argv[2])
    ROI = (2456.7*(1. - 2*res), 2456.7*(1. + 2*res))

    ofile = ROOT.TFile(sys.argv[1] + '_' + sys.argv[2] + '.root', "recreate")
    spectrum_hist = ROOT.TH1D("hist_%s_%s" % (sys.argv[1], sys.argv[2]), "", 500, 2200., 2700.)
    mctree.Draw("energy_mc*(1 + %f*EXOMiscUtil::GetGaussVar())>>hist_%s_%s" % (res, sys.argv[1], sys.argv[2]),
                "nsc == 1 && @pcd_energy.size() > 0 && abs(multiplicity-1.) < 0.001 && !isMissingPosition && " + event.isFiducialStr())
    spectrum_hist.Write()
    ofile.Close()

else:
    # This is the script which manages the job.
    import subprocess
    for res in ['0.0', '0.001', '0.002', '0.003', '0.004', '0.005', '0.006', '0.007', '0.008', '0.009', '0.01', '0.011', '0.012', '0.013', '0.014', '0.015', '0.016', '0.017', '0.018', '0.019', '0.02', '0.021', '0.022', '0.023', '0.024', '0.025', '0.026', '0.027', '0.028', '0.029', '0.03']:
        subprocess.call(['bsub', '-q', 'long', '-R', 'rhel50', '-o', 'Th_%s.out' % res, 'wrap_python.sh', 'PlotSpectraVsResolution.py', 'Th', res])
        subprocess.call(['bsub', '-q', 'long', '-R', 'rhel50', '-o', 'U_%s.out' % res, 'wrap_python.sh', 'PlotSpectraVsResolution.py', 'U', res])
        subprocess.call(['bsub', '-q', 'long', '-R', 'rhel50', '-o', 'Xe_%s.out' % res, 'wrap_python.sh', 'PlotSpectraVsResolution.py', 'Xe', res])
