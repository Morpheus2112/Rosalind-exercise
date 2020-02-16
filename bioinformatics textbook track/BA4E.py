# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:51:17 2018

@author: palan
"""

rna_codon = {'AAA' : 'K', 'AAC' : 'N', 'AAG' : 'K','AAU' : 'N','ACA' : 'T', 'ACC' : 'T', 'ACG' : 'T',
    'ACU' : 'T', 'AGA' : 'R', 'AGC' : 'S', 'AGG' : 'R', 'AGU' : 'S', 'AUA' : 'I', 'AUC' : 'I',
    'AUG' : 'M', 'AUU' : 'I', 'CAA' : 'Q' ,'CAC' : 'H', 'CAG' : 'Q', 'CAU' : 'H', 'CCA' : 'P',
    'CCC' : 'P', 'CCG' : 'P', 'CCU' : 'P', 'CGA' : 'R', 'CGC' : 'R', 'CGG' : 'R', 'CGU' : 'R',
    'CUA' : 'L', 'CUC' : 'L', 'CUG' : 'L', 'CUU' : 'L', 'GAA' : 'E', 'GAC' : 'D', 'GAG' : 'E',
    'GAU' : 'D', 'GCA' : 'A', 'GCC' : 'A', 'GCG' : 'A', 'GCU' : 'A', 'GGA' : 'G', 'GGC' : 'G',
    'GGG' : 'G', 'GGU' : 'G', 'GUA' : 'V', 'GUC' : 'V', 'GUG' : 'V', 'GUU' : 'V', 'UAA' : '-',
    'UAC' : 'Y', 'UAG' : '-', 'UAU' : 'Y', 'UCA' : 'S', 'UCC' : 'S', 'UCG' : 'S', 'UCU' : 'S',
    'UGA' : '-', 'UGC' : 'C', 'UGG' : 'W', 'UGU' : 'C', 'UUA' : 'L', 'UUC' : 'F', 'UUG' : 'L',
    'UUU' : 'F'}

amino_acid_mass = {'G' : 57, 'A' : 71, 'S' : 87, 'P' : 97, 'V' : 99, 'T' : 101, 'C' : 103,
    'I' : 113, 'L' : 113, 'N' : 114, 'D' : 115, 'K' : 128, 'Q' : 128, 'E' : 129,'M' : 131,
    'H' : 137, 'F' : 147, 'R' : 156, 'Y' : 163, 'W' : 186}

def peptide_mass_spectrum(pmass, cyclic = True):
    ''' 
    convert list of peptide masses to spectrum
    '''
    s = [0, ]
    ll = list(pmass)    
    n = len(pmass)
    it = None
    if cyclic:
        ll.extend(pmass[:-1])
        s.append(sum(pmass))
        it = [(i,j) for i in range(n) for j in range (i+1,i+n)]
    else:
        it = [(i,j) for i in range(n) for j in range (i+1,n+1)]
        
    for (i,j) in it:
            subpeptide_mass = sum(ll[i:j])
            s.append(subpeptide_mass)
    
    return sorted(s)



def spectrum_consistent(p,s, cyclic = False):
    lsp = peptide_mass_spectrum(p, cyclic = cyclic)
    for i in lsp:
        if not i in s:
            return False
    return True


def cyclopeptide_sequencing(spectrum):
    '''
    find all peptides consistent with a given spectrum
    '''
    lp = [[]]
    res =  []
    lmass = list(set(amino_acid_mass.values()))
    spectrum.sort(reverse = True)
    parent_mass = max(spectrum)
    def expand(a):
        exp = []
        for i in a:
            for j in lmass:
                p = list(i)
                p.append(j)
                exp.append(p)
        return exp
    while lp:
        lp = expand(lp)
        for p in list(lp):
            if sum(p) == parent_mass:
                if spectrum_consistent(p, spectrum, cyclic = True):
                    res.append(p)
                lp.remove(p)
            elif not spectrum_consistent(p, spectrum):
                lp.remove(p)
    return res  




i = '0 71 71 97 97 99 113 129 147 147 170 184 194 200 210 218 226 246 281 294 297 299 307 317 323 331 365 378 393 394 396 428 436 446 464 464 478 493 507 507 525 535 543 575 577 578 593 606 640 648 654 664 672 674 677 690 725 745 753 761 771 777 787 801 824 824 842 858 872 874 874 900 900 971'
i = '0 113 128 186 241 299 314 427'

fname = 'rosalind_ba4e.txt'
lines = list(l for l in open(fname))
i = lines[0]
lsp = map(int,i.split(' '))
seq = cyclopeptide_sequencing(lsp)
print ' '.join(map(lambda k : '-'.join(map(str,k)),seq))