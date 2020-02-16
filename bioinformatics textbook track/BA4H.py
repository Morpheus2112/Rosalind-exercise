# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:17:09 2018

@author: Memphis
"""
from collections import Counter
import operator
import math
import sys
import random
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

def protein_dna_count(s):
    count = 1
    for c in s:
        count *= sum(map(lambda e: e == c, rna_codon.values()))
    return count

def protein_translation(s):
    '''
    translate RNA text into peptide text
    '''
    global rna_codon
    it = (s[i:3+i] for i in range(0, len(s), 3))
    t = ''.join(map(lambda e: rna_codon.setdefault(e,''), it))
    return t
  
#def peptide_encoding(dna,peptide):
#    '''
#    Find substrings of a genome encoding a given amino acid sequence
#    '''
#    seq = []
#    def search_seq(text, reverse = False):
#        ttext = protein_translation(text)
#        for i in range(len(ttext) - len(peptide) + 1):
#            if (ttext[i:i+len(peptide)] == peptide):
#                substr = text[i*3:i*3+len(peptide)*3].replace('U', 'T')
#                if reverse: substr = reverse_complement(substr)
#                seq.append(substr)
#    rna = dna.replace('T', 'U')
#    rrna = reverse_complement(dna).replace('T', 'U')
#    search_seq(rna)
#    search_seq(rrna, reverse = True)  
#    search_seq(rna[1:])
#    search_seq(rrna[1:], reverse = True)        
#    search_seq(rna[2:])    
#    search_seq(rrna[2:], reverse = True)
#    return seq
   
def peptide_masses(peptide):
    '''
    convert peptite string to a list of masses
    '''
    global amino_acid_mass
    return map(lambda k:amino_acid_mass[k],list(peptide))

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

def get_spectrum(peptide, cyclic = True):
    '''
    Generate the theoretical spectrum of a cyclic peptide.
    '''
    if (type(peptide) == str):
        return peptide_mass_spectrum(peptide_masses(peptide), cyclic)
    else:
        return peptide_mass_spectrum(peptide, cyclic)


def counting_peptides_with_given_mass(mass):
    '''
    compute the number of peptides of given total mass.
    '''
    aam = sorted(list(set(amino_acid_mass.values())), reverse = True)
    md = {0:1}
    for i in range(min(aam), mass+1):
        for m in aam:
            if i-m in md:
                md[i] = md[i-m] + md.get(i,0)
    return md[mass]

def linear_subpeptide_count(n):
    '''
    compute the number of subpeptides of a given peptide length.
    '''
    return 1 + (n+1)*n/2

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


def leaderboard_trim(leaderboard, spectrum, N):
    '''
    output the N highest-scoring linear peptides on Leaderboard lp
    with respect to Spectrum
    '''
    # need for trimming ?
    if len(leaderboard)<=N:
        return leaderboard
    
    #build a dict of peptide:score
    d = {tuple(e): peptide_scoring(e, spectrum, cyclic = False) for e in leaderboard }
    ll = sorted(d, key=d.get, reverse = True)
    min_score = d[ll[N-1]]
    tp = []
    for e in ll:
        if (d[e]>=min_score):
            tp.append(list(e))
        else:
            # cut off loop optimization
            return tp
    return tp

def leaderboard_cyclopeptide_sequencing(spectrum, N, M = 20, convolution = False):
    '''
    find all peptides approximatively consistent 
    with a given spectrum
    '''
    lp = [[]]
    top = []
    top_score = 0
    spectrum.sort(reverse = True)
    lmass = None
    if not convolution:
        lmass = list(set(amino_acid_mass.values()))
    else:
        #build a specific alphabet from the convoluted spectrum
        candidate = [k for k in spectral_convolution(spectrum) if k>= 57 and k <= 200]
        dconv = Counter(candidate)
        lconv = sorted(dconv.items(), key=operator.itemgetter(1), reverse = True)
        min_freq = 0
        lmass = []
        for (k, v) in lconv:
            if (M > 0):
                lmass.append(k)
                min_freq = v
                M -= 1
            elif (M == 0) and (v == (min_freq)):
                #handle ties
                lmass.append(k)
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
                p_score = peptide_scoring(p, spectrum, cyclic = True)
                if p_score >= top_score:
                    top_score = p_score
                    top = p
            elif sum(p) > parent_mass:
                lp.remove(p)
        lp = leaderboard_trim(lp, spectrum, N)
    return top           

def peptide_scoring(peptide, spectrum, cyclic = True):
    '''
    Compute the score of a cyclic peptide against a spectrum.
    '''
    lsp = get_spectrum(peptide, cyclic = cyclic)
    spectrum.sort()
    lsp.sort()
    score = 0
    i = 0
    j = 0
    while i < len(lsp) and j < len(spectrum):
        if (spectrum[j] == lsp[i]):
            j += 1
            i += 1
            score +=1
        elif (spectrum[j] > lsp[i]):
            i += 1
        else:
            j += 1
    return score

def spectral_convolution(spectrum):
    spectrum.sort()
    conv = []
    n = len(spectrum)
    for i in range(n):
        for j in range(i+1,n):
            diff = spectrum[j]-spectrum[i]
            if diff > 0:
                conv.append(diff)
    return conv



#s = '465 473 998 257 0 385 664 707 147 929 87 450 748 938 998 768 234 722 851 113 700 957 265 284 250 137 317 801 128 820 321 612 956 434 534 621 651 129 421 337 216 699 347 101 464 601 87 563 738 635 386 972 620 851 948 200 156 571 551 522 828 984 514 378 363 484 855 869 835 234 1085 764 230 885'
fname = 'rosalind_ba4h.txt'
lines = list(l for l in open(fname))
s = lines[0]
conv = sorted(spectral_convolution(map(int,s.split(' '))))
#print ' '.join(map(str,conv))
sss =  Counter(conv)
t = []
for key, value in sss.most_common():
    t += [key,] * value
result =  " ".join(map(str,t))
