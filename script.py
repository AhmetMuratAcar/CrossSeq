# Color key:
# UTRs: un-highlighted
# Different: red
# Same: green
# Same codon encoded by different nucleotides: yellow
from SequenceClass import Sequence
from App import *


# def comparer(seq1, seq2):
#     """Compares the two given sequences. Return differences between the two."""
#     # Maybe use zip function?
#     # pprint(list(zip(first_seq, second_seq)))
#     On submit run a for loop that generates a Sequence object for each seq submitted.
#     Run the class functions for each sequence object as shown below in main and second seq calls.
#     Then make a function that compares the coding seq of each object to the main seq coding seq.
#     pass


main_file = "Testing Sequences/Oryza_sativa.fasta"
second_file = "Testing Sequences/Arabidopsis_thaliana.fasta"

# main_seq = Sequence()
# second_seq = Sequence()

# Main seq calls
# main_seq.parse_fasta(main_file)
# main_seq.id_retrieve()
# main_seq.seq_retrieve()
# main_seq.find_start_stop()

# Second seq calls
# second_seq.parse_fasta(second_file)
# second_seq.id_retrieve()
# second_seq.seq_retrieve()
# second_seq.find_start_stop()

# comparer(main_seq.codingSeq, second_seq.codingSeq)

# root.mainloop()
