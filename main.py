from json import *
from Bio import Align


def initailize(path1, path2):
    with open(path1, 'r') as js:
        gd = load(js)
    with open(path2, 'r') as js:
        md = load(js)
    return gd, md


def convert(gd, md):
    gl, ml = [], []
    for k1, v1 in gd.items():
        gl.append(v1)
    for k2, v2 in md.items():
        ml.append(v2)
    return gl, ml


def align_two(s1, s2):
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    alignments = aligner.align(s1, s2)
    return alignments


def align_full(gl, ml):
    fl = []
    for g in gl:
        for m in ml:
            fl.append('Aligned: ' + g + ' and ' + m + "\n")
            als = align_two(g, m)
            for a in als:
                fl.append(a)
    return fl


def writing(expath, fl):
    f = open(expath, 'w')
    for el in fl:
        f.write(str(el))
    f.close()
