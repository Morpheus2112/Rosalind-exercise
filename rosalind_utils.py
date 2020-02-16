# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:30:14 2017

@author: Memphis
"""

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_rna

GENCODE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


def reverse_complement(seq):
    """Given a DNA sequence, return its reverse complement"""
    return Seq(seq).reverse_complement().tostring()

def transcribe(dna_seq):
    """Transcribe DNA sequence into mRNA sequence"""
    return Seq(dna_seq, generic_dna).transcribe().tostring()
    
def translate(rna_seq):
    """Translate RNA sequence to amino acid sequence"""
    mrna = Seq(rna_seq, generic_rna)
    return mrna.translate().tostring()

def read_fasta(fasta_file):
    """Read fasta file and return the list of records, consisting of
    description and sequence"""
    handle = open(fasta_file)
    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()
    return [(rec.description, rec.seq.tostring()) for rec in records]

def gc_content(seq):
    """GC content of the sequence"""
    return float(seq.count('C') + seq.count('G')) / len(seq)

def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)

def choose(n,k):
    return fac(n) / fac(n-k) / fac(k)

def choose_large(n,k):
    """n choose k for large values of n and k.
    Not the best solution, but enough for now.
    """
    if k > n/2:
        return choose_large(n, n-k)
    i = n-k+1
    j = 2
    ret = 1
    while i <= n:
        ret *= i
        i += 1
        while j <= k and ret % j == 0:
            ret /= j
            j += 1
    assert j >= k
    return ret

def perm(n,k):
    return fac(n) / fac(n-k)

def hamming_distance(s,t):
    """Hamming distance"""
    return sum(1 if na!=nb else 0 for na,nb in zip(s,t))

def edit_distance_helper(s,t, gap_pen=1, sub_pen=1):
    """Given two strings s and t, find the edit distance, the minimum number of edit
    operations needed to transform s into t, where an edit operation is defined as
    the substitution, insertion or deletion of a single symbol
    """
    m = len(s)
    n = len(t)
    C = [[None for i in range(n+1)] for j in range(m+1)]
    for i in xrange(m+1):
        C[i][0] = i
    for j in xrange(n+1):
        C[0][j] = j
        
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            C[i][j] = min(C[i][j-1] + gap_pen,
                          C[i-1][j] + gap_pen,
                          C[i-1][j-1] + (sub_pen if s[i-1] != t[j-1] else 0))
    return C

def edit_distance(s,t):
    C = edit_distance_helper(s,t)
    return C[-1][-1]

def edit_distance_backtrack(C,s,t, used_gap_pen=1, used_sub_pen=1):
    """Given the scoring table C, strings s and t, find one of the best
    alignments."""
    alignment_a = ""
    alignment_b = ""
    i,j = len(s), len(t)
    while i > 0 and j > 0:
        if C[i][j] == C[i-1][j-1] and s[i-1] == t[j-1]:
            alignment_a += s[i-1]
            alignment_b += t[j-1]
            i -= 1
            j -= 1
        elif C[i][j] == C[i-1][j] + used_gap_pen:
            alignment_a += s[i-1]
            alignment_b += '-'
            i -= 1
        elif C[i][j] == C[i][j-1] + used_gap_pen:
            alignment_a += '-'
            alignment_b += t[j-1]
            j -= 1
        else: # if s[i-1] != t[j-1]
            alignment_a += s[i-1]
            alignment_b += t[j-1]
            i -= 1
            j -= 1
    while i>0:
        alignment_a += s[i-1]
        alignment_b += '-'
        i -= 1
    while j>0:
        alignment_a += '-'
        alignment_b += t[j-1]
        j -= 1

    return alignment_a[::-1], alignment_b[::-1]


def lcsq(s, t):
    """
    http://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    
    Given two strings s and t, find the longest common subsequence
    of s and t. Return the table that is used for each step of calculation.
    """
    m = len(s)
    n = len(t)
    C = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if s[i-1] == t[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C

def lcsq_len(C):
    """The length of the longest subsequence"""
    return C[-1][-1]

def lcsq_backtrack(C, s, t, i, j):
    """Given the scoring table C, strings s and t, find one of the longest common
    subsequences. Initial call of this function has i=len(s) and j=len(t)"""
    if i==0 or j==0:
        return ""
    elif s[i-1] == t[j-1]:
        return lcsq_backtrack(C, s, t, i-1, j-1) + s[i-1]
    else:
        if C[i][j-1] > C[i-1][j]:
            return lcsq_backtrack(C, s, t, i, j-1)
        else:
            return lcsq_backtrack(C, s, t, i-1, j)
        
def lcsq_backtrack_all(C, s, t, i, j):
    """Given the scoring table C, strings s and t, find all longest common
    subsequences. Initial call of this functions has i=len(s) and j=len(t)"""
    if i==0 or j==0:
        return {""}
    elif s[i-1] == t[j-1]:
        return {Z + s[i-1] for Z in lcsq_backtrack_all(C, s, t, i-1, j-1)}
    else:
        R = set()
        if C[i][j-1] >= C[i-1][j]:
            R = lcsq_backtrack_all(C, s, t, i, j-1)
        if C[i-1][j] >= C[i][j-1]:
            R = R.union(lcsq_backtrack_all(C, s, t, i-1, j))
        return R

def longest_common_substring(s, t):
    """Given two strings s and t, find the longest substring.
    Not to be confuest with subsequence.
    http://en.wikipedia.org/wiki/Subsequence#Substring_vs._subsequence
    """
    L = [[0 for i in range(len(t))] for j in range(len(s))]
    z = 0
    ret = set()
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    L[i][j] = 1
                else:
                    L[i][j] = L[i-1][j-1] + 1
                if L[i][j] > z:
                    z = L[i][j]
                    ret = {s[i-z+1:i+1]}
                elif L[i][j] == z:
                    ret = ret.union({s[i-z+1:i+1]})
            else:
                L[i][j] = 0
    return ret

def LGIS(nums):
    """Given a list of numbers, find the longest increasing sequence"""
    L = [None for i in xrange(len(nums))]
    P = [None for i in xrange(len(nums))]
    for i in xrange(len(nums)):
        L[i] = 1  # longest increasing seq that ends in L[i]
        P[i] = -1 # pointer to reconstruct the sequence
        for j in xrange(i):
            if nums[j] < nums[i] and L[j] + 1 > L[i]:
                P[i] = j
                L[i] = L[j] + 1
    index = L.index(max(L))
    seq = [nums[index]]
    while P[index] > -1:
        index = P[index]
        seq.append(nums[index])
    seq.reverse()
    return seq