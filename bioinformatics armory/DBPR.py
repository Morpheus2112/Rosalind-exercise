from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw('A6V398')
record = SwissProt.read(handle)

print "\n".join([reference[2][2:] for reference in record.cross_references if "P:" in reference[2]])