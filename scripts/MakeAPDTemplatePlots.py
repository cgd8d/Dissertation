import ROOT
ROOT.gROOT.SetBatch()
ROOT.gSystem.Load("libEXOUtilities")
ROOT.gStyle.SetOptStat(0)

c = ROOT.TCanvas()
transfer = ROOT.EXOTransferFunction()
transfer.AddDiffStageWithTime(10*ROOT.CLHEP.microsecond)
transfer.AddDiffStageWithTime(10*ROOT.CLHEP.microsecond)
transfer.AddDiffStageWithTime(300*ROOT.CLHEP.microsecond)
transfer.AddIntegStageWithTime(3*ROOT.CLHEP.microsecond)
transfer.AddIntegStageWithTime(3*ROOT.CLHEP.microsecond)

wf = ROOT.EXODoubleWaveform()
length = 200
factor = 10
wf.SetSamplingPeriod(ROOT.CLHEP.microsecond/factor)
wf.SetLength(factor*length)
wf.SetTOffset(-50*ROOT.CLHEP.microsecond)
for i in range(factor*50): wf[i] = 0
for i in range(factor*50, factor*length): wf[i] = 1

hist_unshaped = ROOT.TH1D("apd_unshaped", "Unshaped APD Signal", factor*length, 0., length)
wf.LoadIntoHist(hist_unshaped)
transfer.Transform(wf)
wf /= transfer.GetGain()
hist_shaped = ROOT.TH1D("apd_shaped", "Shaped APD Signal", factor*length, 0., length)
wf.LoadIntoHist(hist_shaped)

hist_unshaped.SetTitle("Unshaped APD Signal")
hist_unshaped.GetYaxis().SetTickLength(0)
hist_unshaped.GetYaxis().SetLabelOffset(999)
hist_unshaped.GetYaxis().SetTitle("Arbitrary Units")
hist_unshaped.GetYaxis().SetRangeUser(-0.5, 1.5)
hist_unshaped.GetXaxis().SetTitleSize(0.04)
hist_unshaped.GetYaxis().SetTitleSize(0.04)
hist_unshaped.GetXaxis().SetTitleFont(42)
hist_unshaped.GetYaxis().SetTitleFont(42)

hist_shaped.SetTitle("Shaped APD Signal")
hist_shaped.GetYaxis().SetRangeUser(-0.5, 1.5)
hist_shaped.GetXaxis().SetTitleSize(0.04)
hist_shaped.GetYaxis().SetTitleSize(0.04)
hist_shaped.GetXaxis().SetTitleFont(42)
hist_shaped.GetYaxis().SetTitleFont(42)

hist_unshaped.Draw("9L")
c.SaveAs("UnshapedAPDWaveform.png")

hist_shaped.Draw("9L")
arrow = ROOT.TArrow(-10, 0, -10, 1, 0.03, "<|>")
arrow.Draw()
text = ROOT.TText(-15, 0.5, "Scaled to 1")
text.SetTextAngle(90)
text.SetTextSize(0.04)
text.SetTextAlign(22)
text.SetTextFont(42)
text.Draw()
c.SaveAs("ShapedAPDWaveform.png")

