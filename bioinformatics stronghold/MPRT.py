# -*- coding: utf-8 -*- 

"""
Problem
To allow for the presence of its varying forms, a protein motif is represented
by a shorthand as follows: [XY] means either X or Y and {X} means any amino acid
except X. For example, the N-glycosylation motif is written as N{P}[ST]{P}.
You can see the complete description and features of a particular protein by its
access ID uniprot_id in the UniProt database, by inserting the ID number into
http://www.uniprot.org/uniprot/uniprot_id Alternatively, you can obtain a
protein sequence in FASTA format by following
http://www.uniprot.org/uniprot/uniprot_id.fasta For example, the data for
protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given
access ID followed by a list of locations in the protein string where the motif
can be found.
Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

import sys
sys.path.append('../')
import rosalind_utils
import re
import urllib2
from Bio import SeqIO

def search_motif(prot_seq):
    """Search protein motif in the sequence"""
    motif = r'(?=N[^P][ST][^P])'
    return [m.start()+1 for m in re.finditer(motif, prot_seq)]

def download_uniprot_fasta(uniprot_id):
    url = "http://www.uniprot.org/uniprot/%s.fasta" % uniprot_id
    response = urllib2.urlopen(url)
    recs = [rec for rec in  SeqIO.parse(response, "fasta")]
    return recs

def mprt_helper(uniprot_id):
    recs = download_uniprot_fasta(uniprot_id)
    rec = recs[0]
    matches = search_motif(rec.seq.tostring())
    if matches:
        print uniprot_id
        print ' '.join(map(str, matches))
            
def mprt():
    uniprot_ids = [line.strip() for line in open("rosalind_mprt.txt").readlines()]
    for uid in uniprot_ids:
        mprt_helper(uid)

mprt()