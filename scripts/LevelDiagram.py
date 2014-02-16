import matplotlib.pyplot

Levels = [
('Sn', 50, -56.2990, 'beta'),
('Sb', 51, -64.5250, 'beta'),
('Te', 52, -74.4790, 'beta'),
('I', 53, -79.5721, 'beta'),
('Xe', 54, -86.4291, 'betabeta'),
('Cs', 55, -86.3390, 'beta'),
('Ba', 56, -88.8872, None),
('La', 57, -86.0369, 'ec'),
('Ce', 58, -86.4736, 'ecec'),
('Pr', 59, -81.3289, 'ec'),
('Nd', 60, -79.1992, 'ec'),
('Pm', 61, -71.1979, 'ec'),
('Sm', 62, -66.8108, 'ec'),
('Eu', 63, -56.1040, 'ec'),
('Gd', 64, -48.9220, 'ec'),
('Tb', 65, -35.8900, 'ec')
]

def GetEntryForAtom(atom):
    for i in range(len(Levels)):
        if Levels[i][0] == atom: return i
def GetEntryForZ(z):
    for i in range(len(Levels)):
        if Levels[i][1] == z: return i

UpperLimit = -75

vals = []

for level in Levels:
    if level[2] > UpperLimit: continue
    vals.append([float(level[1]), float(level[1])+1])
    vals.append([level[2], level[2]])

vals_tuple = tuple(vals)

matplotlib.pyplot.plot(*vals_tuple, color='black', lw=3)

for level in Levels:
    if level[2] > UpperLimit: continue
    matplotlib.pyplot.annotate(level[0],
                               (float(level[1]) + 0.5, level[2] + 0.4),
                               ha = "center")

    if level[3] == 'beta':
        entryOfDaughter = GetEntryForZ(level[1]+1)
        matplotlib.pyplot.annotate(u'\u03B2',
                                   (float(level[1]) + 1, level[2]),
                                   xytext = (float(level[1] + 1 + Levels[entryOfDaughter][1])/2, level[2] - 2),
                                   arrowprops = dict(arrowstyle="<-"),
                                   ha = "center")

    if level[3] == 'betabeta':
        entryOfDaughter = GetEntryForZ(level[1]+2)
        matplotlib.pyplot.annotate(u'\u03B2\u03B2',
                                   (float(level[1]) + 1, level[2]),
                                   xytext = (float(level[1] + 1 + Levels[entryOfDaughter][1])/2, level[2] - 2),
                                   arrowprops = dict(arrowstyle="<-"),
                                   ha = "center")

    if level[3] == 'ec':
        entryOfDaughter = GetEntryForZ(level[1]-1)
        matplotlib.pyplot.annotate(u'\u03B5',
                                   (float(level[1]), level[2]),
                                   xytext = (float(level[1] + Levels[entryOfDaughter][1] + 1)/2, level[2] - 2),
                                   arrowprops = dict(arrowstyle="<-"),
                                   ha = "center")

    if level[3] == 'ecec':
        entryOfDaughter = GetEntryForZ(level[1]-2)
        matplotlib.pyplot.annotate(u'\u03B5\u03B5',
                                   (float(level[1]), level[2]),
                                   xytext = (float(level[1] + Levels[entryOfDaughter][1] + 1)/2, level[2] - 2),
                                   arrowprops = dict(arrowstyle="<-"),
                                   ha = "center")

matplotlib.pyplot.xlabel('Z (# Protons)')
matplotlib.pyplot.ylabel(u'\u0394E (MeV)')
matplotlib.pyplot.savefig('LevelDiagram.png')




