# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 23:08:33 2018

@author: Memphis
"""

from collections import Counter




m = 17
n = 399
s = '0 101 113 113 114 128 128 128 128 128 137 137 137 163 186 227 229 241 241 250 256 256 265 265 274 277 287 300 314 355 366 369 369 378 387 390 393 393 414 415 415 437 442 483 494 506 506 515 518 521 527 543 543 550 551 552 555 620 622 634 643 646 655 656 664 664 671 678 680 680 692 735 748 777 783 783 784 792 792 793 806 808 808 808 829 849 905 905 911 920 920 920 921 921 921 930 936 936 992 1012 1033 1033 1033 1035 1048 1049 1049 1057 1058 1058 1064 1093 1106 1149 1161 1161 1163 1170 1177 1177 1185 1186 1195 1198 1207 1219 1221 1286 1289 1290 1291 1298 1298 1314 1320 1323 1326 1335 1335 1347 1358 1399 1404 1426 1426 1427 1448 1448 1451 1454 1463 1472 1472 1475 1486 1527 1541 1554 1564 1567 1576 1576 1585 1585 1591 1600 1600 1612 1614 1655 1678 1704 1704 1704 1713 1713 1713 1713 1713 1727 1728 1728 1740 1841'
spectrum = map(int,s.split(' '))
 
#m=18
#n=364
# 
#spectrum=[735, 71, 1176, 822, 1392, 542, 634, 919, 449, 257, 229, 285, 97, 1229, 317, 443, 257, 705, 257, 1339, 859, 501, 1362, 818, 546, 113, 1307, 574, 430, 687, 1022, 806, 414, 816, 501, 1422, 728, 1362, 101, 1436, 317, 1008, 163, 891, 1273, 131, 1063, 574, 806, 242, 758, 228, 1236, 1176, 1135, 244, 186, 1176, 578, 418, 128, 1493, 1123, 1364, 630, 392, 1236, 944, 264, 919, 1120, 675, 321, 1307, 1050, 951, 370, 559, 1330, 1079, 1022, 972, 129, 1264, 471, 863, 57, 1249, 788, 1365, 691, 549, 1172, 859, 388, 1236, 1075, 1101, 788, 471, 131, 947, 705, 934, 521, 992, 1105, 485, 687, 358, 388, 0, 915, 1105, 671, 317, 802, 765, 373, 1208, 1396, 448, 602, 220, 992, 1251, 1044, 154, 1045, 634, 677, 1265, 1380, 186]
# 
__AMINOACID_INTEGER_MASS__={"G": 57,
"A": 71,
"S": 87,
"P": 97,
"V": 99,
"T": 101,
"C": 103,
"I": 113,
"L": 113,
"N": 114,
"D": 115,
"K": 128,
"Q": 128,
"E": 129,
"M": 131,
"H": 137,
"F": 147,
"R": 156,
"Y": 163,
"W": 186}
 
def convolutional_cyclopeptide_sequencing(spectrum,N,M):
    ''' (listof int), int, int -> (list of str),(listof int)
    consumes a listo of integers representing an spectrum, an int N for the maximum number of elements in the leaderboard 
    and an integer M for the number of masses to be used and produces a list of peptides in mass format and their scores after solving
    the following problem:
 
    CONVOLUTIONCYCLOPEPTIDESEQUENCING.
 
    Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
 
    Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the 
    convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).
    '''
    counts=Counter(spectral_convolution(spectrum)).items()
    counts_with_mass_in_range=[m for m in counts if m[0] >=57 and m[0] <=200]
    masses=sorted(counts_with_mass_in_range,key= lambda x:x[1],reverse=True)
    cut=masses[M-1][1]
    top_m_masses=[m[0] for m in masses if m[1] >=cut]
 
 
    return cyclopeptide_sequencing_noisy(spectrum, N,aa_masses=top_m_masses)
 
def cyclopeptide_sequencing_noisy(linear_spectrum, N,aa_masses=__AMINOACID_INTEGER_MASS__.values()):
    ''' (listof number), int [,(listof int)]  -> (list of str),(listof int)
    consumes an empirical spectrum and a maximum leaderboard length and produces list of strings with 
    the peptides which theoretical spectrum has the highest score with respect to linear_spectrum
 
    the string peptides are given in mass format:
 
    51-114-74-...
 
 
 
    Optionally a list of amnoacid masses can be given
 
    if N >0 then the functions tries to solve the following problem
 
    Cyclopeptide Sequencing Problem (for noisy spectra): Find a cyclic peptide having maximum score against
     an experimental spectrum.
     Input: A collection of integers Spectrum.
     Output: A cyclic peptide Peptide maximizing Score(Peptide, Spectrum) over all peptides Peptide such
     that Mass(Peptide) is equal to ParentMass(Spectrum).
 
     In this case it also returns a list of scores
 
 
    '''
 
    parent_mass=max(linear_spectrum)
 
 
    def cut(leaderboard):
 
        if len(leaderboard) > N:
            sl=sorted(leaderboard,key=lambda x:x[2],reverse=True)
            cut_score=sl[N-1][2]
            leaderboard=[p for p in sl if p[2]>=cut_score]
 
        return leaderboard
 
 
 
    S=list(set(aa_masses))
    peptides=[tuple([[],0,0])]
    output=[]
    while len(peptides) >0:
 
 
        new_peptides=[]
        remove=[]
        for p in peptides:
            remove.append(p)
            for aa in S:
                new_p=tuple(list(p[0])+[aa])
                new_p_mass=compute_peptide_mass(new_p,masses=True)
                new_p_score=peptide_spectrum_score(new_p,linear_spectrum,masses=True)
                new_peptides.append((new_p,new_p_mass,new_p_score))
 
        for p in remove:
            peptides.remove(p)
 
        peptides+=new_peptides
        remove=[] 
        new_peptides=[]       
        for p in peptides:
 
            if p[1]==parent_mass:
                if len(output) >0:
                    if  p[2] == output[0][2]:
                        output.append(p)
 
                    elif p[2] > output[0][2]:
                        output=[p]
 
                else:
                    output=[p]
 
            elif p[1]> parent_mass:
                remove.append(p)
 
        for p in remove:
            peptides.remove(p)
        remove=[]                    
 
        peptides=cut(peptides)
 
 
 
 
    return [peptide2mass_string(p[0],masses=True) for p in output],[p[2] for p in output]
 
def spectral_convolution(spectrum):
    ''' (listof int) -> (listof int)
    Spectral Convolution Problem: Compute the convolution of a spectrum.
     Input: A collection of integers Spectrum.
     Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should
     appearexactly k times; you may return the elements in any order.
    '''
    convolution=[]
    for i in range(len(spectrum)):
        for j in range(i+1,len(spectrum)):
            convolution.append(abs(spectrum[i]-spectrum[j]))
 
    return  [c for c in convolution if c>0]
 
def compute_peptide_mass(pept,masses=False):
    '''AminoacisString -> int
    consumes a peptide and produces its theoretical mass
    '''
    if masses:
        return sum(pept)         
    else:
        return sum([__AMINOACID_INTEGER_MASS__[aa] for aa in pept])
 
def peptide_spectrum_score(peptide,spectrum,masses=False):
    ''' AminoacidString, (listof int) -> int
 
    Given a cyclic peptide Peptide and a spectrum Spectrum, we define Score(Peptide, Spectrum) as 
     the number of masses shared between Cyclospectrum(Peptide) and Spectrum. For example if
 
    Spectrum = {0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484}
 
    then Score(NQEL, Spectrum) = 11
 
 
    '''
    cs=compute_spectrum(peptide,circular=True,masses=masses)
    intersection=Counter(spectrum) & Counter(cs)
    return len([e for e in intersection.elements()])
 
def compute_spectrum(peptide, circular=False,masses=False):
    ''' AminoacidString [,Boolean]-> (listof number)
 
    Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a  peptide.
     Input: An amino acid string Peptide.
     Output: spectrum(Peptide).
 
     The theoretical spectrum of a  peptide Peptide, denoted Cyclospectrum(Peptide), 
     is the collection of all of the masses of its subpeptides, in addition to the mass 0 and the 
     mass of the entire peptide. Note that the theoretical spectrum may contain duplicate elements
 
     if circular is True, then the peptide is cyclic
 
    '''
 
 
    spectrum=[compute_peptide_mass(subpept,masses=masses) for subpept in subpeptides(peptide,circular=circular,masses=masses)]
    spectrum.insert(0,0)
    spectrum.append(compute_peptide_mass(peptide,masses=masses))
    spectrum.sort()
 
 
 
    return spectrum
 
def subpeptides(peptide,circular=False,masses=False):
    ''' AminoacidString [,boolean] -> (listof AminoaidString)
    consumes a aminoacid string (peptide) and produces a list of all possible subpeptides
 
    if circular is True, then the peptide is cyclic
    '''
 
    subpept=[]
    for size in range(1,len(peptide)):
        for pos in range(len(peptide)):
            if pos+size <= len(peptide):                
                subpept.append(peptide[pos:pos+size])
            elif circular:
                final_size=len(peptide)-pos
                remaining=size-final_size
                subpept.append(peptide[pos:]+peptide[:remaining])
    if masses:
        subpept=[tuple(p) for p in subpept]
    return subpept
 
def peptide2mass_string(peptide,masses=False):
    ''' AminoacidString -> str
    consumes a peptide and produces a string in the format
    M1-M2-M3-...
 
    where M1, M2, ... are the string version of the aminoacid masses
    '''
    if masses:
        return "-".join([str(m) for m in peptide])
    else:
        return "-".join([str(m) for m in [__AMINOACID_INTEGER_MASS__[aa] for aa in peptide]])
 
 
print convolutional_cyclopeptide_sequencing(spectrum,n,m)